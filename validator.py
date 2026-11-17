"""Límites defensivos y validación sin ejecutar código del usuario."""
from errors import TranslationError


def validate_source(source):
    if not source or not source.strip():
        raise TranslationError("Escriba o cargue código antes de traducir.")
    if len(source) > 150_000 or len(source.splitlines()) > 3000:
        raise TranslationError("Límite académico: 150 000 caracteres y 3000 líneas.")
    if "\x00" in source:
        raise TranslationError("El texto contiene caracteres nulos.")
