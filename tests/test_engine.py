import ast
import contextlib
import io
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from translator import translate
from file_io import load_code, save_code
from tests.cases import ACADEMIC, PYTHON_CASES, p


def run_fixture(code, inputs=()):
    """Solo ejecuta fixtures de prueba propios; nunca código de la interfaz."""
    stream = io.StringIO()
    with contextlib.redirect_stdout(stream), patch('builtins.input', side_effect=inputs):
        exec(compile(code, '<fixture>', 'exec'), {})
    return stream.getvalue()


class EngineTests(unittest.TestCase):
    def forward(self, text):
        result = translate(text)
        self.assertTrue(result.ok, result.error)
        ast.parse(result.code)
        return result.code

    def reverse(self, text):
        result = translate(text, "Python", "PSeInt")
        self.assertTrue(result.ok, result.error)
        return result.code

    def test_empty(self):
        self.assertFalse(translate(' ').ok)

    def test_direction(self):
        self.assertFalse(translate('x', 'Python', 'Python').ok)

    def test_pse_comments_and_strings(self):
        code = self.forward(p('Escribir "Si Y NO <- //" // hola'))
        self.assertIn('# hola', code)
        self.assertEqual(run_fixture(code), 'Si Y NO <- //\n')

    def test_repeat_once(self):
        code = self.forward(p('Definir n Como Entero\nn <- 0\nRepetir\nn <- n + 1\nHasta Que n = 1\nEscribir n'))
        self.assertEqual(run_fixture(code), '1\n')

    def test_repeat_multiple(self):
        code = self.forward(p('Definir n Como Entero\nRepetir\nn <- n + 1\nHasta Que n >= 3\nEscribir n'))
        self.assertEqual(run_fixture(code), '3\n')

    def test_inclusive_negative(self):
        code = self.forward(p('Definir i Como Entero\nPara i <- 5 Hasta 1 Con Paso -2 Hacer\nEscribir i\nFinPara'))
        self.assertEqual(run_fixture(code), '5\n3\n1\n')

    def test_inclusive_single(self):
        code = self.forward(p('Definir i Como Entero\nPara i <- 2 Hasta 2 Hacer\nEscribir i\nFinPara'))
        self.assertEqual(run_fixture(code), '2\n')

    def test_inputs(self):
        code = self.forward(p('Definir n Como Entero\nDefinir r Como Real\nDefinir s Como Cadena\nLeer n, r, s\nEscribir n, r, s'))
        self.assertEqual(run_fixture(code, ['2','1.5','sí']), '21.5sí\n')

    def test_python_inputs(self):
        code = self.reverse('a = int(input("n: "))\nb = float(input())\nc = input()\nprint(a, b, c)')
        self.assertIn('Definir a Como Entero', code)
        self.assertIn('Escribir Sin Saltar "n: "', code)
        self.assertEqual(run_fixture(self.forward(code), ['2','1.5','sí']), 'n: 2 1.5 sí\n')

    def test_math_all(self):
        code = self.forward(p('Escribir RC(9), ABS(-2), TRUNC(2.8), SEN(0), COS(0), TAN(0), LN(1), EXP(0), 2^3'))
        self.assertEqual(run_fixture(code), '3.0220.01.00.00.01.08\n')

    def test_case_insensitive(self):
        self.assertEqual(run_fixture(self.forward('proceso Demo\nDefinir Valor Como Entero\nVALOR <- 3\nescribir valor\nfinproceso')), '3\n')

    def test_types_defaults(self):
        code = self.forward(p('Definir n Como Entero\nDefinir r Como Real\nDefinir s Como Caracter\nDefinir b Como Logico\nEscribir n, r, s, b'))
        self.assertEqual(run_fixture(code), '00.0False\n')

    def test_empty_block(self):
        self.assertIn('pass', self.forward(p('Si Verdadero Entonces\n// vacío\nFinSi')))

    def test_utf8_files(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'prueba.psc'
            save_code(path, 'Escribir "niño, canción"')
            self.assertEqual(load_code(path), 'Escribir "niño, canción"')
            path.write_bytes(b'\xef\xbb\xbfHola')
            self.assertEqual(load_code(path), 'Hola')

    def test_io_errors(self):
        with self.assertRaises(OSError):
            load_code('ruta_que_no_existe/prueba.py')

    def test_line_diagnostic(self):
        result = translate(p('Dimension a[3]'))
        self.assertFalse(result.ok)
        self.assertIn('línea 2', result.error)
        self.assertEqual(result.code, '')

    def test_auxiliary_collision(self):
        code = self.reverse('ta_indice1 = 9\nfor i in range(2):\n    print(i)\nprint(ta_indice1)')
        self.assertEqual(run_fixture(self.forward(code)), '0\n1\n9\n')

    def test_all_python_math(self):
        source = 'import math\nprint(math.sin(0), math.cos(0), math.tan(0), math.log(1), math.exp(0))'
        self.assertEqual(run_fixture(self.forward(self.reverse(source))), run_fixture(source))

    def test_completed_counter_assignment(self):
        source = p('Definir i, j Como Entero\nPara i <- 1 Hasta 1 Hacer\nFinPara\nPara j <- 1 Hasta 1 Hacer\ni <- 7\nFinPara\nEscribir i')
        self.assertEqual(run_fixture(self.forward(source)), '7\n')


def academic_test(case):
    def test(self):
        _, source, inputs, expected = case
        self.assertEqual(run_fixture(self.forward(source), inputs), expected)
    return test


def python_test(case):
    def test(self):
        _, source, expected = case
        code = self.reverse(source)
        self.assertEqual(run_fixture(self.forward(code)), expected)
        self.assertEqual(run_fixture(source), expected)
    return test


for case in ACADEMIC:
    setattr(EngineTests, 'test_academico_' + case[0], academic_test(case))
for case in PYTHON_CASES:
    setattr(EngineTests, 'test_python_' + case[0], python_test(case))

INVALID_PSE = {
    'tipo_asignacion': p('Definir n Como Entero\nn <- "texto"'),
    'limite_real': p('Definir i Como Entero\nPara i <- 1 Hasta 2.5 Hacer\nFinPara'),
    'condicion_numerica': p('Si 1 Entonces\nFinSi'),
    'leer_contador': p('Definir i Como Entero\nPara i <- 1 Hasta 3 Hacer\nLeer i\nFinPara'),
    'contador_anidado': p('Definir i Como Entero\nPara i <- 1 Hasta 3 Hacer\nPara i <- 1 Hasta 2 Hacer\nFinPara\nFinPara'),
    'cierre': 'Algoritmo A\nSi Verdadero Entonces\nFinAlgoritmo',
    'sin_cierre': 'Algoritmo A\nEscribir 1',
    'sino': p('SiNo'),
    'sino_duplicado': p('Si Verdadero Entonces\nSiNo\nSiNo\nFinSi'),
    'paso_cero': p('Definir i Como Entero\nPara i <- 1 Hasta 3 Con Paso 0 Hacer\nFinPara'),
    'paso_variable': p('Definir i, n Como Entero\nPara i <- 1 Hasta 3 Con Paso n Hacer\nFinPara'),
    'variable_sin_definir': p('x <- 1'),
    'expresion': p('Escribir (1 +'),
    'cadena': p('Escribir "hola'),
    'arreglo': p('Dimension a[3]'),
    'segun': p('Segun n Hacer'),
    'lectura_logica': p('Definir b Como Logico\nLeer b'),
    'funcion_desconocida': p('Escribir sistema(1)'),
    'retorno_no_definido': 'Funcion r <- doble(x)\nFinFuncion\n' + p('Escribir 1'),
    'doble_algoritmo': p('Escribir 1') + p('Escribir 2'),
    'contador_mutado': p('Definir i Como Entero\nPara i <- 1 Hasta 3 Hacer\ni <- 1\nFinPara'),
}
INVALID_PY = {
    'infinito': 'x = 1e999',
    'sintaxis': 'if True\n print(1)',
    'lista': 'x = [1, 2]',
    'clase': 'class A:\n    pass',
    'import': 'import os',
    'comprension': 'x = [i for i in range(2)]',
    'division_entera': 'x = 5 // 2',
    'break': 'while True:\n    break',
    'while_else': 'while False:\n    pass\nelse:\n    pass',
    'return_temprano': 'def f(x):\n    if x > 0:\n        return x\n    return 0',
    'argumentos': 'def f(x=1):\n    return x',
    'print_archivo': 'print(1, file=f)',
    'print_final': 'print(1, end="!")',
    'input_anidado': 'print(input())',
    'and_valores': 'x = 1 and 2',
    'truthiness': 'if 1:\n    print(1)',
    'tipos_cambiantes': 'x = 1\nx = "a"',
    'colision': 'abc = 1\nABC = 2',
    'rangocero': 'for i in range(1, 3, 0):\n    print(i)',
    'range_real': 'for i in range(1.0):\n    print(i)',
    'cadena_escape': 'print("a\\nb")',
    'comparacion_encadenada': 'x = 1 < 2 < 3',
    'string_aritmetica': 'x = "a" * 3',
}


def rejection(source, origin):
    def test(self):
        result = translate(source, origin, 'Python' if origin == 'PSeInt' else 'PSeInt')
        self.assertFalse(result.ok, result.code)
        self.assertEqual(result.code, '')
    return test


for name, source in INVALID_PSE.items():
    setattr(EngineTests, 'test_rechazo_pse_' + name, rejection(source, 'PSeInt'))
for name, source in INVALID_PY.items():
    setattr(EngineTests, 'test_rechazo_py_' + name, rejection(source, 'Python'))
