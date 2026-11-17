"""Archivos UTF-8; la confirmación de sobrescritura pertenece a la GUI."""
from pathlib import Path


def load_code(path):
    return Path(path).read_text(encoding="utf-8-sig")


def save_code(path, code):
    Path(path).write_text(code, encoding="utf-8", newline="\n")
