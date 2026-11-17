"""Expresiones escalares; AST con lista de nodos permitidos."""
import ast
import json
import keyword
import math
import re
from errors import TranslationError, unsupported

MATH = {"abs": "abs", "rc": "sqrt", "sen": "sin", "cos": "cos", "tan": "tan", "ln": "log", "exp": "exp", "trunc": "trunc"}
RESERVED = set("algoritmo proceso finalgoritmo finproceso definir como entero real cadena caracter logico escribir leer si entonces sino finsi mientras hacer finmientras repetir hasta que para con paso finpara funcion finfuncion subproceso finsubproceso verdadero falso y o no mod segun dimension retornar".split())
BUILTINS = set(MATH) | set(MATH.values()) | {"print", "input", "int", "float", "str", "bool", "range", "math"}


def identifier(name, line=1):
    if not re.fullmatch(r"[A-Za-z][A-Za-z_0-9]*", name) or keyword.iskeyword(name) or name.lower() in RESERVED | BUILTINS:
        unsupported(f"Nombre {name!r} reservado o no válido. Use letras ASCII.", line)
    return name


class Expressions:
    def __init__(self, names=None, functions=None):
        self.names = names if names is not None else {}
        self.functions = functions if functions is not None else {}

    def pse(self, items, line):
        replacements = {"=": "==", "<>": "!=", "^": "**", "mod": "%", "y": "and", "o": "or", "no": "not", "verdadero": "True", "falso": "False"}
        converted = []
        for item in items:
            if item[0] in "\"'":
                converted.append(repr(item[1:-1]))
            elif item.lower() in replacements:
                converted.append(replacements[item.lower()])
            elif item.lower() in MATH:
                name = MATH[item.lower()]
                converted.append(name if name == "abs" else "math." + name)
            else:
                converted.append(self.names.get(item.lower(), item))
        try:
            node = ast.parse(" ".join(converted), mode="eval").body
        except (SyntaxError, ValueError) as exc:
            raise TranslationError("Expresión incompleta o no válida.", line) from exc
        self.validate(node, line)
        return ast.unparse(node)

    def validate(self, node, line):
        if isinstance(node, ast.Constant):
            if type(node.value) not in (int, float, str, bool):
                unsupported("Solo se admiten constantes escalares.", line)
            if isinstance(node.value, float) and not math.isfinite(node.value):
                unsupported("Use constantes numéricas finitas.", line)
        elif isinstance(node, ast.Name):
            identifier(node.id, line)
        elif isinstance(node, ast.BinOp) and type(node.op) in (ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Mod, ast.Pow):
            self.validate(node.left, line)
            self.validate(node.right, line)
        elif isinstance(node, ast.UnaryOp) and type(node.op) in (ast.UAdd, ast.USub, ast.Not):
            self.validate(node.operand, line)
        elif isinstance(node, ast.BoolOp):
            for value in node.values:
                self.validate(value, line)
        elif isinstance(node, ast.Compare) and all(type(op) in (ast.Eq, ast.NotEq, ast.Lt, ast.LtE, ast.Gt, ast.GtE) for op in node.ops):
            if len(node.ops) != 1:
                unsupported("Separe las comparaciones encadenadas usando Y/and.", line)
            self.validate(node.left, line)
            self.validate(node.comparators[0], line)
        elif isinstance(node, ast.Call):
            if node.keywords:
                unsupported("No se admiten argumentos con nombre en expresiones.", line)
            name = ast.unparse(node.func)
            arity = {"abs": 1, **{"math." + v: 1 for v in MATH.values() if v != "abs"}, **self.functions}.get(name)
            if arity is None or len(node.args) != arity:
                unsupported(f"Función desconocida o cantidad incorrecta de argumentos: {name}.", line)
            for arg in node.args:
                self.validate(arg, line)
        else:
            unsupported(f"Expresión {type(node).__name__} fuera del subconjunto.", line)

    def python(self, node, line):
        self.validate(node, line)
        if isinstance(node, ast.Constant):
            if isinstance(node.value, str):
                if any(c in node.value for c in ('"', '\\', '\n', '\r', '\t')):
                    unsupported("Cadenas con comillas dobles, escapes o saltos de línea.", line)
                return '"' + node.value + '"'
            if isinstance(node.value, bool):
                return "Verdadero" if node.value else "Falso"
            return repr(node.value)
        if isinstance(node, ast.Name):
            return node.id
        if isinstance(node, ast.BinOp):
            op = {ast.Add: "+", ast.Sub: "-", ast.Mult: "*", ast.Div: "/", ast.Mod: "MOD", ast.Pow: "^"}[type(node.op)]
            return f"({self.python(node.left, line)} {op} {self.python(node.right, line)})"
        if isinstance(node, ast.UnaryOp):
            op = {ast.USub: "-", ast.UAdd: "+", ast.Not: "NO "}[type(node.op)]
            return f"({op}{self.python(node.operand, line)})"
        if isinstance(node, ast.BoolOp):
            return "(" + (" Y " if isinstance(node.op, ast.And) else " O ").join(self.python(v, line) for v in node.values) + ")"
        if isinstance(node, ast.Compare):
            op = {ast.Eq: "=", ast.NotEq: "<>", ast.Lt: "<", ast.LtE: "<=", ast.Gt: ">", ast.GtE: ">="}[type(node.ops[0])]
            return f"({self.python(node.left, line)} {op} {self.python(node.comparators[0], line)})"
        name = ast.unparse(node.func)
        mapped = {"math." + v: k.upper() for k, v in MATH.items()}
        return mapped.get(name, name) + "(" + ", ".join(self.python(a, line) for a in node.args) + ")"
