"""Diagnósticos públicos, independientes de la interfaz."""
class TranslationError(ValueError):
    def __init__(self, message, line=None, category="Sintaxis"):
        self.line, self.category = line, category
        super().__init__(f"{category}" + (f", línea {line}" if line else "") + f": {message}")


def unsupported(message, line=None):
    raise TranslationError(message, line, "No compatible")
