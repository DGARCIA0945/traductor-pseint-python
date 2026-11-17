"""Generación de PSeInt a partir de un AST Python admitido."""
import ast
import io
import tokenize
from errors import TranslationError, unsupported
from expressions import Expressions, identifier


class PythonToPSeInt:
    def translate(self, source):
        try:
            tree = ast.parse(source)
        except SyntaxError as exc:
            raise TranslationError(exc.msg, exc.lineno) from exc
        self.functions, self.returns, self.warnings, self.counter = {}, {}, [], 0
        source_names = [n.id.lower() for n in ast.walk(tree) if isinstance(n, ast.Name)]
        source_names += [n.arg.lower() for n in ast.walk(tree) if isinstance(n, ast.arg)]
        source_names += [n.name.lower() for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]
        self.prefix = "ta_"
        while any(n.startswith(self.prefix) for n in source_names):
            self.prefix += "x"
        result_name = self.prefix + "resultado"
        self.out, self.indent = [], 0
        functions = [n for n in tree.body if isinstance(n, ast.FunctionDef)]
        for fn in functions:
            identifier(fn.name, fn.lineno)
            if fn.name.lower() in (n.lower() for n in self.functions):
                unsupported("Nombres de funciones duplicados o que solo difieren en mayúsculas.", fn.lineno)
            if fn.decorator_list or fn.returns or fn.args.defaults or fn.args.kw_defaults or fn.args.kwonlyargs or fn.args.posonlyargs or fn.args.vararg or fn.args.kwarg or any(a.annotation for a in fn.args.args):
                unsupported("Funciones sin decoradores, anotaciones ni parámetros especiales.", fn.lineno)
            self.functions[fn.name] = len(fn.args.args)
            if any(isinstance(n, ast.Return) for n in ast.walk(fn)):
                if not isinstance(fn.body[-1], ast.Return) or fn.body[-1].value is None or sum(isinstance(n, ast.Return) for n in ast.walk(fn)) != 1:
                    unsupported("Use un único return con valor al final de la función.", fn.lineno)
                self.returns[fn.name] = "Real"
        self.expressions = Expressions(functions=self.functions)
        # Comments survive as a prologue; moving them is explicit in the user guide.
        comments = [tok for tok in tokenize.generate_tokens(io.StringIO(source).readline) if tok.type == tokenize.COMMENT]
        for comment in comments:
            self.emit(f"// Python línea {comment.start[0]}: {comment.string[1:].strip()}")
        for fn in functions:
            self.types = {}
            params = []
            for arg in fn.args.args:
                self.bind(arg.arg, "Real", arg.lineno)
                params.append(arg.arg)
            if params:
                self.warnings.append(f"Línea {fn.lineno}: parámetros de {fn.name} tratados como escalares numéricos; revise los tipos de sus llamadas.")
            body = fn.body[:-1] if fn.name in self.returns else fn.body
            rendered = self.render_body(body)
            if fn.name in self.returns:
                ret = fn.body[-1]
                kind = self.infer(ret.value)
                self.returns[fn.name] = kind
                rendered.append("    " + result_name + " <- " + self.expr(ret.value))
                self.types[result_name] = kind
            self.emit("SubProceso " + (result_name + " <- " if fn.name in self.returns else "") + fn.name + "(" + ", ".join(params) + ")")
            self.indent = 1
            self.declarations(exclude=params)
            self.out.extend(rendered)
            self.indent = 0
            self.emit("FinSubProceso")
            self.emit("")
        self.types = {}
        main = [n for n in tree.body if not isinstance(n, ast.FunctionDef)]
        rendered = self.render_body(main)
        self.emit("Algoritmo ProgramaTraducido")
        self.indent = 1
        self.declarations()
        self.out.extend(rendered)
        self.indent = 0
        self.emit("FinAlgoritmo")
        return "\n".join(self.out) + "\n", self.warnings

    def render_body(self, body):
        previous, level = self.out, self.indent
        self.out, self.indent = [], 1
        for node in body:
            self.statement(node)
        result = self.out
        self.out, self.indent = previous, level
        return result

    def emit(self, text):
        self.out.append("    " * self.indent + text)

    def bind(self, name, kind, line):
        identifier(name, line)
        if name.lower() in (n.lower() for n in self.functions) or any(n.lower() == name.lower() and n != name for n in self.types):
            unsupported("Colisión de nombres: PSeInt no distingue mayúsculas.", line)
        previous = self.types.get(name)
        if previous and previous != kind:
            unsupported(f"La variable {name} cambia de tipo ({previous} a {kind}); use otra variable.", line)
        self.types[name] = kind

    def declarations(self, exclude=()):
        for kind in ("Entero", "Real", "Cadena", "Logico"):
            names = [n for n, t in self.types.items() if t == kind and n not in exclude]
            if names:
                self.emit("Definir " + ", ".join(names) + " Como " + kind)

    def expr(self, node):
        self.infer(node)
        return self.expressions.python(node, node.lineno)

    def infer(self, node):
        line = getattr(node, "lineno", 1)
        self.expressions.validate(node, line)
        if isinstance(node, ast.Constant):
            return {int: "Entero", float: "Real", str: "Cadena", bool: "Logico"}[type(node.value)]
        if isinstance(node, ast.Name):
            if node.id not in self.types:
                raise TranslationError(f"Variable {node.id!r} usada antes de una asignación conocida.", line)
            return self.types[node.id]
        if isinstance(node, ast.BinOp):
            left, right = self.infer(node.left), self.infer(node.right)
            if left not in ("Entero", "Real") or right not in ("Entero", "Real"):
                unsupported("Operaciones aritméticas solo sobre números; no se traduce concatenación ni repetición de cadenas.", line)
            if isinstance(node.op, ast.Pow):
                self.warnings.append(f"Línea {line}: potencia requiere resultado real y finito; no se admiten complejos.")
            nonnegative_power = isinstance(node.op, ast.Pow) and isinstance(node.right, ast.Constant) and type(node.right.value) is int and node.right.value >= 0
            return "Real" if "Real" in (left, right) or isinstance(node.op, ast.Div) or (isinstance(node.op, ast.Pow) and not nonnegative_power) else "Entero"
        if isinstance(node, ast.UnaryOp):
            kind = self.infer(node.operand)
            if isinstance(node.op, ast.Not):
                if kind != "Logico":
                    unsupported("not requiere una expresión lógica explícita.", line)
                return "Logico"
            if kind not in ("Entero", "Real"):
                unsupported("Signo unario solo sobre números.", line)
            return kind
        if isinstance(node, ast.Compare):
            left, right = self.infer(node.left), self.infer(node.comparators[0])
            if left != right and {left, right} != {"Entero", "Real"}:
                unsupported("Comparación entre tipos distintos.", line)
            return "Logico"
        if isinstance(node, ast.BoolOp):
            if any(self.infer(v) != "Logico" for v in node.values):
                unsupported("and/or requieren valores lógicos, no selección de operandos.", line)
            return "Logico"
        name = ast.unparse(node.func)
        for arg in node.args:
            if self.infer(arg) not in ("Entero", "Real"):
                unsupported("Las funciones admitidas reciben argumentos numéricos.", line)
        if name in self.functions:
            if name not in self.returns:
                unsupported("Un subproceso sin retorno no puede usarse como expresión.", line)
            return self.returns[name]
        if name == "math.trunc":
            return "Entero"
        if name == "abs":
            return self.infer(node.args[0])
        return "Real"

    def condition(self, node):
        if self.infer(node) != "Logico":
            unsupported("La condición debe ser lógica: use, por ejemplo, n <> 0 / n != 0.", node.lineno)
        return self.expr(node)

    def block(self, body):
        self.indent += 1
        for node in body:
            self.statement(node)
        self.indent -= 1

    def read_input(self, value, target):
        kind, call = "Cadena", value
        if isinstance(value, ast.Call) and isinstance(value.func, ast.Name) and value.func.id in ("int", "float", "str") and len(value.args) == 1 and not value.keywords:
            kind, call = {"int": "Entero", "float": "Real", "str": "Cadena"}[value.func.id], value.args[0]
        if not isinstance(call, ast.Call) or not isinstance(call.func, ast.Name) or call.func.id != "input":
            return False
        if len(call.args) > 1 or call.keywords:
            unsupported("input admite cero o un mensaje literal.", call.lineno)
        if call.args:
            if not isinstance(call.args[0], ast.Constant) or not isinstance(call.args[0].value, str):
                unsupported("El mensaje de input debe ser una cadena literal.", call.lineno)
            self.emit("Escribir Sin Saltar " + self.expr(call.args[0]))
        self.bind(target, kind, call.lineno)
        self.emit("Leer " + target)
        return True

    def statement(self, n):
        line = n.lineno
        if isinstance(n, ast.Import) and len(n.names) == 1 and n.names[0].name == "math" and n.names[0].asname is None:
            return
        if isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name):
            name = n.targets[0].id
            if self.read_input(n.value, name):
                return
            kind, value = self.infer(n.value), self.expr(n.value)
            self.bind(name, kind, line)
            self.emit(name + " <- " + value)
        elif isinstance(n, ast.AugAssign) and isinstance(n.target, ast.Name):
            value = ast.BinOp(left=ast.Name(id=n.target.id, ctx=ast.Load()), op=n.op, right=n.value)
            ast.copy_location(value.left, n)
            ast.copy_location(value, n)
            kind, rendered = self.infer(value), self.expr(value)
            self.bind(n.target.id, kind, line)
            self.emit(n.target.id + " <- " + rendered)
        elif isinstance(n, ast.Expr) and isinstance(n.value, ast.Call):
            call = n.value
            if isinstance(call.func, ast.Name) and call.func.id == "print":
                sep, end = " ", "\n"
                for kw in call.keywords:
                    if kw.arg not in ("sep", "end") or not isinstance(kw.value, ast.Constant) or not isinstance(kw.value.value, str):
                        unsupported("print solo admite sep y end literales.", line)
                    if kw.arg == "sep":
                        sep = kw.value.value
                    else:
                        end = kw.value.value
                if end not in ("", "\n"):
                    unsupported("print admite end='' o end='\\n'.", line)
                args = []
                for arg in call.args:
                    if args:
                        args.append(self.expressions.python(ast.Constant(value=sep), line))
                    args.append(self.expr(arg))
                self.emit("Escribir " + ("Sin Saltar " if not end else "") + (", ".join(args) if args else '""'))
            elif isinstance(call.func, ast.Name) and call.func.id in self.functions:
                self.expressions.validate(call, line)
                for arg in call.args:
                    if self.infer(arg) not in ("Entero", "Real"):
                        unsupported("Parámetros numéricos únicamente.", line)
                self.emit(self.expressions.python(call, line))
            else:
                unsupported("Llamada no compatible.", line)
        elif isinstance(n, ast.If):
            self.emit("Si " + self.condition(n.test) + " Entonces")
            self.block(n.body)
            if n.orelse:
                self.emit("SiNo")
                self.block(n.orelse)
            self.emit("FinSi")
        elif isinstance(n, ast.While):
            if n.orelse:
                unsupported("while ... else no está implementado.", line)
            self.emit("Mientras " + self.condition(n.test) + " Hacer")
            self.block(n.body)
            self.emit("FinMientras")
        elif isinstance(n, ast.For):
            if n.orelse or not isinstance(n.target, ast.Name) or not isinstance(n.iter, ast.Call) or not isinstance(n.iter.func, ast.Name) or n.iter.func.id != "range" or n.iter.keywords or not 1 <= len(n.iter.args) <= 3:
                unsupported("for requiere range(inicio, fin, paso) sin else.", line)
            args = n.iter.args
            start = args[0] if len(args) > 1 else ast.copy_location(ast.Constant(value=0), n)
            stop = args[1] if len(args) > 1 else args[0]
            step = 1
            if len(args) == 3:
                try:
                    step = ast.literal_eval(args[2])
                except (ValueError, TypeError):
                    unsupported("Paso de range: entero literal no nulo.", line)
                if type(step) is not int or step == 0:
                    unsupported("Paso de range: entero literal no nulo.", line)
            if self.infer(start) != "Entero" or self.infer(stop) != "Entero":
                unsupported("Los límites de range deben ser enteros.", line)
            initial, final = self.expr(start), self.expr(stop)
            self.bind(n.target.id, "Entero", line)
            self.counter += 1
            cursor, limit = f"{self.prefix}indice{self.counter}", f"{self.prefix}limite{self.counter}"
            self.types[cursor] = self.types[limit] = "Entero"
            self.emit(cursor + " <- " + initial)
            self.emit(limit + " <- " + final)
            self.emit(f"Mientras {cursor} {'<' if step > 0 else '>'} {limit} Hacer")
            self.indent += 1
            self.emit(n.target.id + " <- " + cursor)
            for child in n.body:
                self.statement(child)
            self.emit(f"{cursor} <- {cursor} + ({step})")
            self.indent -= 1
            self.emit("FinMientras")
        elif isinstance(n, ast.Pass):
            self.emit("// pass: bloque vacío")
        else:
            unsupported(f"Instrucción Python {type(n).__name__} no implementada.", line)
