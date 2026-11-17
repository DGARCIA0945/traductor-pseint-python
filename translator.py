"""API pública. Las traducciones son atómicas: error implica salida vacía."""
from dataclasses import dataclass, field
from errors import TranslationError
from validator import validate_source
from pseint_to_python import PSeIntToPython
from python_to_pseint import PythonToPSeInt


@dataclass
class TranslationResult:
    code: str = ""
    warnings: list = field(default_factory=list)
    error: str = ""

    @property
    def ok(self):
        return not self.error


def translate(source, origin="PSeInt", destination="Python"):
    try:
        validate_source(source)
        if (origin, destination) == ("PSeInt", "Python"):
            code, warnings = PSeIntToPython().translate(source)
        elif (origin, destination) == ("Python", "PSeInt"):
            code, warnings = PythonToPSeInt().translate(source)
        else:
            raise TranslationError("Seleccione lenguajes distintos: PSeInt y Python.")
        warnings = list(dict.fromkeys(warnings))
        warnings.append("Revise tipos, dominios numéricos y formato de salida. Se valida el subconjunto, no la corrección total del algoritmo; consulte la guía.")
        return TranslationResult(code, warnings)
    except TranslationError as exc:
        return TranslationResult(error=str(exc))
    except (SyntaxError, RecursionError, ValueError, OverflowError) as exc:
        return TranslationResult(error=f"Sintaxis: estructura demasiado compleja o inválida ({type(exc).__name__}).")
