"""Tokenización de PSeInt: nunca sustituye texto dentro de cadenas."""
import ast
import re
from errors import TranslationError

TOKEN = re.compile(r'''\s+|"[^"\n]*"|'[^'\n]*'|\d+(?:\.\d+)?|[A-Za-z_][A-Za-z_0-9]*|<-|<=|>=|<>|!=|[+*/%^=<>(),;\-]''')


def split_comment(line):
    quote = None
    for i, char in enumerate(line):
        if char in "\"'":
            if quote == char:
                quote = None
            elif quote is None:
                quote = char
        if quote is None and line[i:i + 2] == "//":
            return line[:i].strip(), line[i + 2:].strip()
    return line.strip(), None


def tokens(source, line=1):
    out, pos = [], 0
    while pos < len(source):
        match = TOKEN.match(source, pos)
        if not match:
            raise TranslationError(f"Símbolo o cadena no admitida cerca de {source[pos:pos+16]!r}.", line)
        value = match.group()
        if not value.isspace():
            if value[0] in "\"'" and "\\" in value:
                raise TranslationError("Las cadenas PSeInt no admiten escapes en este perfil.", line)
            out.append(value)
        pos = match.end()
    return out


def groups(items, line=1):
    result, current, depth = [], [], 0
    for token in items:
        if token == "," and depth == 0:
            if not current:
                raise TranslationError("Falta una expresión entre comas.", line)
            result.append(current)
            current = []
        else:
            depth += (token == "(") - (token == ")")
            current.append(token)
    if depth != 0 or not current:
        raise TranslationError("Paréntesis o lista de expresiones incompleta.", line)
    return result + [current]


def string_value(value):
    # PSeInt strings are literal; Python literal_eval is intentionally not used here.
    return value[1:-1]
