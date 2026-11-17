"""Ejecuta unittest y genera evidencia reproducible en docs/."""
import ast
import datetime
import inspect
import json
import platform
import time
import unittest
from pathlib import Path
from translator import translate
from tests.cases import ACADEMIC, PYTHON_CASES
from tests.test_engine import INVALID_PSE, INVALID_PY, run_fixture

BASE = Path(__file__).resolve().parent


class RecordedResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.records = []

    def record(self, test, state, detail=''):
        method = getattr(test, test._testMethodName)
        self.records.append({'nombre': test.id(), 'estado': state, 'resultado_obtenido': detail or 'Todas las aserciones del caso se cumplieron.', 'codigo_y_resultado_esperado': inspect.getsource(method)})

    def addSuccess(self, test):
        super().addSuccess(test)
        self.record(test, 'APROBADO')

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.record(test, 'FALLO', self._exc_info_to_string(err, test))

    def addError(self, test, err):
        super().addError(test, err)
        self.record(test, 'ERROR', self._exc_info_to_string(err, test))

    def addSkip(self, test, reason):
        super().addSkip(test, reason)
        self.record(test, 'NO EJECUTADO', reason)


def main():
    docs = BASE/'docs'
    docs.mkdir(exist_ok=True)
    suite = unittest.defaultTestLoader.discover(str(BASE/'tests'), top_level_dir=str(BASE))
    started = time.perf_counter()
    with (docs/'unittest.log').open('w', encoding='utf-8') as stream:
        result = unittest.TextTestRunner(stream=stream, verbosity=2, resultclass=RecordedResult).run(suite)
    evidence = []
    for name, source, inputs, expected in ACADEMIC:
        translated = translate(source)
        actual = run_fixture(translated.code, inputs) if translated.ok else translated.error
        evidence.append(dict(nombre=name, origen='PSeInt', entrada=source, datos=inputs, salida_esperada=expected, salida_obtenida=actual, codigo_generado=translated.code, estado='APROBADO' if expected == actual else 'FALLO'))
    for name, source, expected in PYTHON_CASES:
        translated = translate(source, 'Python', 'PSeInt')
        back = translate(translated.code) if translated.ok else translated
        actual = run_fixture(back.code) if back.ok else back.error
        evidence.append(dict(nombre=name, origen='Python', entrada=source, salida_esperada=expected, salida_obtenida=actual, codigo_generado=translated.code, estado='APROBADO' if expected == actual else 'FALLO'))
    for origin, cases in [('PSeInt', INVALID_PSE), ('Python', INVALID_PY)]:
        for name, source in cases.items():
            translated = translate(source, origin, 'Python' if origin == 'PSeInt' else 'PSeInt')
            evidence.append(dict(nombre='rechazo_'+origin+'_'+name, origen=origin, entrada=source, salida_esperada='Diagnóstico y código de salida vacío', salida_obtenida=translated.error, codigo_generado=translated.code, estado='APROBADO' if not translated.ok and not translated.code else 'FALLO'))
    data = dict(fecha=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-5))).isoformat(), python=platform.python_version(), sistema=platform.platform(), pruebas=result.testsRun, fallos=len(result.failures), errores=len(result.errors), omitidas=len(result.skipped), segundos=round(time.perf_counter()-started, 3), casos=result.records, traducciones=evidence)
    (docs/'resultados_pruebas.json').write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
    lines = ['# Informe de pruebas ejecutadas', '', f"Fecha (UTC-5): {data['fecha']}", f"Entorno: Python {data['python']} / {data['sistema']}", '', f"Pruebas: {data['pruebas']}; fallos: {data['fallos']}; errores: {data['errores']}; omitidas: {data['omitidas']}.", '', 'Los casos Python se comparan con su ejecución original y con una traducción de ida y vuelta. Esto NO sustituye la prueba con el intérprete oficial PSeInt. No se dispone de él en este entorno. La GUI se prueba con Tk real y diálogos de archivos simulados. No se ejecuta código arbitrario desde la aplicación.', '', '## Casos unitarios e integración', '']
    for row in result.records:
        lines += [f"### {row['nombre']}", f"Estado: {row['estado']}", '', 'Código de prueba (incluye entrada y aserciones esperadas):', '```python', row['codigo_y_resultado_esperado'].rstrip(), '```', 'Resultado obtenido: ' + row['resultado_obtenido'], '']
    lines += ['## Evidencia de traducción por programa', '']
    for row in evidence:
        lines += [f"### {row['nombre']} ({row['origen']})", 'Estado: ' + row['estado'], 'Entrada:', '```', row['entrada'].rstrip(), '```', 'Resultado esperado:', '```', row['salida_esperada'], '```', 'Resultado obtenido:', '```', row['salida_obtenida'], '```', 'Código generado:', '```', row['codigo_generado'].rstrip(), '```', '']
    (docs/'INFORME_PRUEBAS.md').write_text('\n'.join(lines), encoding='utf-8')
    print(json.dumps({k:v for k,v in data.items() if k not in ('casos','traducciones')}, ensure_ascii=False))
    return 0 if result.wasSuccessful() and all(r['estado']=='APROBADO' for r in evidence) else 1


if __name__ == '__main__':
    raise SystemExit(main())
