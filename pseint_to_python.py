"""Analizador por líneas y pila de bloques para el perfil académico."""
import ast
import re
from errors import TranslationError, unsupported
from expressions import Expressions, identifier
from lexer import tokens, split_comment, groups
from python_to_pseint import PythonToPSeInt

TYPES = {"entero": ("int", "0"), "real": ("float", "0.0"), "cadena": ("str", "''"), "caracter": ("str", "''"), "logico": ("bool", "False")}


class PSeIntToPython:
    def translate(self, source):
        self.out, self.stack, self.indent, self.names, self.types = [], [], 0, {}, {}
        self.functions, self.warnings, self.line, self.algorithm = {}, [], 1, False
        self.closed, self.ret = False, None
        self.return_types = {}
        for no, raw in enumerate(source.splitlines(), 1):
            code, _ = split_comment(raw)
            match = re.fullmatch(r"(?:Funcion|SubProceso)\s+(?:(\w+)\s*<-\s*)?(\w+)\s*\((.*?)\)\s*;?", code, re.I)
            if match:
                name = identifier(match[2], no)
                if name.lower() in (n.lower() for n in self.functions):
                    raise TranslationError("Función duplicada.", no)
                self.functions[name] = len(match[3].split(',')) if match[3].strip() else 0
                if match[1]:
                    self.return_types[name] = "Real"
        for self.line, raw in enumerate(source.splitlines(), 1):
            code, comment = split_comment(raw)
            if comment is not None:
                self.emit("# " + comment)
            if not code:
                continue
            items = tokens(code, self.line)
            if items[-1:] == [";"]:
                items.pop()
            if not items:
                continue
            self.statement(items)
        if self.stack:
            raise TranslationError(f"Falta cerrar el bloque {self.stack[-1]['kind']} iniciado en la línea {self.stack[-1]['line']}.", self.line)
        if not self.algorithm or not self.closed:
            raise TranslationError("Incluya Algoritmo/FinAlgoritmo o Proceso/FinProceso.", self.line)
        code = "import math\n\n" + "\n".join(self.out).rstrip() + "\n"
        ast.parse(code)
        return code, self.warnings

    def emit(self, text):
        self.out.append("    " * self.indent + text)

    def expr(self, items):
        names = {**{n.lower(): n for n in self.functions}, **self.names}
        value = Expressions(names, self.functions).pse(items, self.line)
        for node in ast.walk(ast.parse(value, mode="eval")):
            if isinstance(node, ast.Name) and node.id not in set(self.names.values()) | set(self.functions) | {"math", "abs"}:
                raise TranslationError(f"Variable {node.id!r} sin Definir.", self.line)
        return value

    def kind(self, value):
        checker = PythonToPSeInt()
        checker.expressions = Expressions(functions=self.functions)
        checker.functions, checker.returns, checker.warnings = self.functions, self.return_types, self.warnings
        kinds = {"entero": "Entero", "real": "Real", "cadena": "Cadena", "caracter": "Cadena", "logico": "Logico"}
        checker.types = {name: kinds.get(self.types.get(key), "Real") for key, name in self.names.items()}
        node = ast.parse(value, mode="eval").body
        ast.increment_lineno(node, self.line - 1)
        return checker.infer(node)

    def condition(self, items):
        value = self.expr(items)
        if self.kind(value) != "Logico":
            unsupported("La condición debe ser lógica; use una comparación explícita.", self.line)
        return value

    def var(self, name):
        if name.lower() not in self.names:
            raise TranslationError(f"Variable {name!r} sin Definir.", self.line)
        return self.names[name.lower()]

    def push(self, kind, text=None):
        if text:
            self.emit(text)
        self.stack.append({"kind": kind, "line": self.line, "start": len(self.out), "else": False})
        if kind not in ("algoritmo", "proceso"):
            self.indent += 1

    def ensure_body(self, block):
        if not any(s.strip() and not s.lstrip().startswith("#") for s in self.out[block['start']:]):
            self.emit("pass")

    def top(self, kinds):
        if not self.stack or self.stack[-1]['kind'] not in kinds:
            raise TranslationError("Cierre o alternativa sin el bloque de apertura correspondiente.", self.line)
        return self.stack[-1]

    def statement(self, t):
        word, low = t[0].lower(), [x.lower() for x in t]
        if word in ("funcion", "subproceso"):
            if self.stack or self.algorithm:
                unsupported("Coloque las funciones antes del algoritmo principal.", self.line)
            match = re.fullmatch(r"(?:funcion|subproceso)\s+(?:(\w+)\s*<-\s*)?(\w+)\s*\((.*?)\)", " ".join(t), re.I)
            if not match:
                raise TranslationError("Use Funcion resultado <- nombre(parametros).", self.line)
            self.names, self.types, self.ret = {}, {}, match[1]
            params = [p.strip() for p in match[3].split(',')] if match[3].strip() else []
            for p in params:
                identifier(p, self.line)
                if p.lower() in self.names:
                    raise TranslationError("Parámetro duplicado.", self.line)
                self.names[p.lower()] = p
            if self.ret:
                identifier(self.ret, self.line)
                if self.ret.lower() in self.names:
                    raise TranslationError("El retorno debe ser distinto de los parámetros.", self.line)
            self.push(word, f"def {match[2]}({', '.join(params)}):")
            return
        if word in ("algoritmo", "proceso"):
            if self.stack or self.algorithm or len(t) != 2:
                raise TranslationError("Se permite un único algoritmo principal con nombre.", self.line)
            identifier(t[1], self.line)
            self.algorithm = True
            self.names, self.types, self.ret = {}, {}, None
            self.push(word)
            return
        if not self.stack:
            raise TranslationError("Instrucción fuera de un algoritmo o función.", self.line)
        endings = {"finalgoritmo": "algoritmo", "finproceso": "proceso", "finfuncion": "funcion", "finsubproceso": "subproceso", "finsi": "si", "finmientras": "mientras", "finpara": "para"}
        if word in endings:
            if len(t) != 1:
                raise TranslationError("Texto adicional tras el cierre.", self.line)
            block = self.top({endings[word]})
            if word in ("finfuncion", "finsubproceso") and self.ret:
                self.emit("return " + self.var(self.ret))
            if endings[word] not in ("algoritmo", "proceso"):
                self.ensure_body(block)
                self.indent -= 1
            else:
                self.closed = True
            self.stack.pop()
            return
        if word == "definir":
            if len(self.stack) != 1:
                unsupported("Declare variables al nivel principal de cada algoritmo o función.", self.line)
            if len(t) < 4 or low[-2] != "como" or low[-1] not in TYPES:
                raise TranslationError("Use Definir a, b Como Entero/Real/Cadena/Caracter/Logico.", self.line)
            for part in groups(t[1:-2], self.line):
                if len(part) != 1:
                    raise TranslationError("Nombre de variable no válido.", self.line)
                name = identifier(part[0], self.line)
                if name.lower() in self.names or name.lower() in (n.lower() for n in self.functions):
                    raise TranslationError("Nombre ya declarado o usado por una función.", self.line)
                self.names[name.lower()], self.types[name.lower()] = name, low[-1]
                if self.ret and name.lower() == self.ret.lower():
                    fn = next((s.strip().split('(')[0][4:] for s in reversed(self.out) if s.startswith('def ')), None)
                    if fn:
                        self.return_types[fn] = {"entero": "Entero", "real": "Real", "cadena": "Cadena", "caracter": "Cadena", "logico": "Logico"}[low[-1]]
                self.emit(name + " = " + TYPES[low[-1]][1])
            return
        if word == "escribir":
            start, end = (3, "''") if low[1:3] == ["sin", "saltar"] else (1, "'\\n'")
            args = [self.expr(part) for part in groups(t[start:], self.line)]
            for arg in args:
                self.kind(arg)
            self.emit(f"print({', '.join(args)}, sep='', end={end})")
            return
        if word == "leer":
            for part in groups(t[1:], self.line):
                if len(part) != 1:
                    unsupported("Leer solo admite variables escalares.", self.line)
                name = self.var(part[0])
                if any(b.get('counter') == name for b in self.stack):
                    unsupported("Leer no puede modificar un contador de Para activo.", self.line)
                kind = self.types.get(name.lower())
                if kind is None or kind == "logico":
                    unsupported("Leer necesita un tipo declarado Entero, Real o Cadena; no admite Logico.", self.line)
                conversion = TYPES[kind][0]
                self.emit(f"{name} = " + ("input()" if conversion == "str" else f"{conversion}(input())"))
            return
        if word == "si":
            if low[-1] != "entonces":
                raise TranslationError("Falta Entonces.", self.line)
            self.push("si", "if " + self.condition(t[1:-1]) + ":")
            return
        if word == "sino":
            block = self.top({"si"})
            if len(t) != 1 or block['else']:
                raise TranslationError("SiNo duplicado o con texto adicional.", self.line)
            self.ensure_body(block)
            self.indent -= 1
            self.emit("else:")
            self.indent += 1
            block.update({"else": True, "start": len(self.out)})
            return
        if word == "mientras":
            if low[-1] != "hacer":
                raise TranslationError("Falta Hacer.", self.line)
            self.push("mientras", "while " + self.condition(t[1:-1]) + ":")
            return
        if word == "repetir" and len(t) == 1:
            self.push("repetir", "while True:")
            return
        if low[:2] == ["hasta", "que"]:
            self.top({"repetir"})
            self.emit("if " + self.condition(t[2:]) + ":")
            self.emit("    break")
            self.indent -= 1
            self.stack.pop()
            return
        if word == "para":
            if len(t) < 7 or t[2] != "<-" or "hasta" not in low or low[-1] != "hacer":
                raise TranslationError("Use Para i <- inicio Hasta fin [Con Paso entero] Hacer.", self.line)
            index = low.index("hasta")
            end = low.index("con") if "con" in low else len(t) - 1
            step = 1
            if end != len(t) - 1:
                if low[end:end+2] != ["con", "paso"] or not re.fullmatch(r"[+-]?\d+", "".join(t[end+2:-1])):
                    unsupported("El paso debe ser un entero literal distinto de cero.", self.line)
                step = int("".join(t[end+2:-1]))
            if step == 0:
                raise TranslationError("El paso no puede ser cero.", self.line)
            name = self.var(t[1])
            if any(b.get('counter') == name for b in self.stack):
                unsupported("Use contadores diferentes para ciclos Para anidados.", self.line)
            if self.types.get(name.lower()) != "entero":
                unsupported("El contador de Para debe declararse Entero.", self.line)
            start, stop = self.expr(t[3:index]), self.expr(t[index+1:end])
            if self.kind(start) != "Entero" or self.kind(stop) != "Entero":
                unsupported("Los límites de Para deben ser enteros.", self.line)
            self.push("para", f"for {name} in range({start}, ({stop}) {'+' if step > 0 else '-'} 1, {step}):")
            self.stack[-1]['counter'] = name
            self.warnings.append(f"Línea {self.line}: Para usa límites enteros evaluados una vez; no modifique el contador ni dependa de su valor al salir.")
            return
        if len(t) > 2 and t[1] == "<-":
            name = self.var(t[0])
            if any(b.get('counter') == name for b in self.stack):
                unsupported("No modifique un contador de Para dentro del ciclo.", self.line)
            value = self.expr(t[2:])
            kind, target = self.kind(value), self.kind(name)
            if kind != target and not (target == "Real" and kind == "Entero"):
                unsupported(f"Asignación incompatible: {name} es {target}, la expresión es {kind}.", self.line)
            self.emit(name + " = " + value)
            return
        # A standalone procedure call must be a whitelisted call, not a bare expression.
        if len(t) > 2 and t[1] == "(" and t[0].lower() in (n.lower() for n in self.functions):
            value = self.expr(t)
            if not isinstance(ast.parse(value, mode="eval").body, ast.Call):
                unsupported("Se esperaba una llamada a subproceso.", self.line)
            self.emit(value)
            return
        unsupported(f"Instrucción {t[0]!r} no reconocida.", self.line)
