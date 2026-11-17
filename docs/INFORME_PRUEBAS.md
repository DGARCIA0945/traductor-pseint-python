# Informe de pruebas ejecutadas

Fecha (UTC-5): 2026-10-27T13:35:15.284490-05:00
Entorno: Python 3.12.14 / Windows-11-10.0.26200-SP0

Pruebas: 93; fallos: 0; errores: 0; omitidas: 0.

Los casos Python se comparan con su ejecución original y con una traducción de ida y vuelta. Esto NO sustituye la prueba con el intérprete oficial PSeInt. No se dispone de él en este entorno. La GUI se prueba con Tk real y diálogos de archivos simulados. No se ejecuta código arbitrario desde la aplicación.

## Casos unitarios e integración

### tests.test_engine.EngineTests.test_academico_01_hola_mundo
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        _, source, inputs, expected = case
        self.assertEqual(run_fixture(self.forward(source), inputs), expected)
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_academico_02_suma
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        _, source, inputs, expected = case
        self.assertEqual(run_fixture(self.forward(source), inputs), expected)
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_academico_03_promedio
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        _, source, inputs, expected = case
        self.assertEqual(run_fixture(self.forward(source), inputs), expected)
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_academico_04_par_impar
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        _, source, inputs, expected = case
        self.assertEqual(run_fixture(self.forward(source), inputs), expected)
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_academico_05_mayor
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        _, source, inputs, expected = case
        self.assertEqual(run_fixture(self.forward(source), inputs), expected)
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_academico_06_alternativas
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        _, source, inputs, expected = case
        self.assertEqual(run_fixture(self.forward(source), inputs), expected)
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_academico_07_tabla
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        _, source, inputs, expected = case
        self.assertEqual(run_fixture(self.forward(source), inputs), expected)
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_academico_08_suma_ciclo
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        _, source, inputs, expected = case
        self.assertEqual(run_fixture(self.forward(source), inputs), expected)
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_academico_09_factorial
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        _, source, inputs, expected = case
        self.assertEqual(run_fixture(self.forward(source), inputs), expected)
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_academico_10_funcion
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        _, source, inputs, expected = case
        self.assertEqual(run_fixture(self.forward(source), inputs), expected)
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_all_python_math
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test_all_python_math(self):
        source = 'import math\nprint(math.sin(0), math.cos(0), math.tan(0), math.log(1), math.exp(0))'
        self.assertEqual(run_fixture(self.forward(self.reverse(source))), run_fixture(source))
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_auxiliary_collision
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test_auxiliary_collision(self):
        code = self.reverse('ta_indice1 = 9\nfor i in range(2):\n    print(i)\nprint(ta_indice1)')
        self.assertEqual(run_fixture(self.forward(code)), '0\n1\n9\n')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_case_insensitive
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test_case_insensitive(self):
        self.assertEqual(run_fixture(self.forward('proceso Demo\nDefinir Valor Como Entero\nVALOR <- 3\nescribir valor\nfinproceso')), '3\n')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_completed_counter_assignment
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test_completed_counter_assignment(self):
        source = p('Definir i, j Como Entero\nPara i <- 1 Hasta 1 Hacer\nFinPara\nPara j <- 1 Hasta 1 Hacer\ni <- 7\nFinPara\nEscribir i')
        self.assertEqual(run_fixture(self.forward(source)), '7\n')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_direction
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test_direction(self):
        self.assertFalse(translate('x', 'Python', 'Python').ok)
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_empty
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test_empty(self):
        self.assertFalse(translate(' ').ok)
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_empty_block
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test_empty_block(self):
        self.assertIn('pass', self.forward(p('Si Verdadero Entonces\n// vacío\nFinSi')))
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_inclusive_negative
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test_inclusive_negative(self):
        code = self.forward(p('Definir i Como Entero\nPara i <- 5 Hasta 1 Con Paso -2 Hacer\nEscribir i\nFinPara'))
        self.assertEqual(run_fixture(code), '5\n3\n1\n')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_inclusive_single
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test_inclusive_single(self):
        code = self.forward(p('Definir i Como Entero\nPara i <- 2 Hasta 2 Hacer\nEscribir i\nFinPara'))
        self.assertEqual(run_fixture(code), '2\n')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_inputs
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test_inputs(self):
        code = self.forward(p('Definir n Como Entero\nDefinir r Como Real\nDefinir s Como Cadena\nLeer n, r, s\nEscribir n, r, s'))
        self.assertEqual(run_fixture(code, ['2','1.5','sí']), '21.5sí\n')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_io_errors
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test_io_errors(self):
        with self.assertRaises(OSError):
            load_code('ruta_que_no_existe/prueba.py')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_line_diagnostic
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test_line_diagnostic(self):
        result = translate(p('Dimension a[3]'))
        self.assertFalse(result.ok)
        self.assertIn('línea 2', result.error)
        self.assertEqual(result.code, '')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_math_all
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test_math_all(self):
        code = self.forward(p('Escribir RC(9), ABS(-2), TRUNC(2.8), SEN(0), COS(0), TAN(0), LN(1), EXP(0), 2^3'))
        self.assertEqual(run_fixture(code), '3.0220.01.00.00.01.08\n')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_pse_comments_and_strings
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test_pse_comments_and_strings(self):
        code = self.forward(p('Escribir "Si Y NO <- //" // hola'))
        self.assertIn('# hola', code)
        self.assertEqual(run_fixture(code), 'Si Y NO <- //\n')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_python_anidados
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        _, source, expected = case
        code = self.reverse(source)
        self.assertEqual(run_fixture(self.forward(code)), expected)
        self.assertEqual(run_fixture(source), expected)
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_python_asignacion
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        _, source, expected = case
        code = self.reverse(source)
        self.assertEqual(run_fixture(self.forward(code)), expected)
        self.assertEqual(run_fixture(source), expected)
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_python_comentario
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        _, source, expected = case
        code = self.reverse(source)
        self.assertEqual(run_fixture(self.forward(code)), expected)
        self.assertEqual(run_fixture(source), expected)
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_python_elif
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        _, source, expected = case
        code = self.reverse(source)
        self.assertEqual(run_fixture(self.forward(code)), expected)
        self.assertEqual(run_fixture(source), expected)
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_python_for_contador_mutable
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        _, source, expected = case
        code = self.reverse(source)
        self.assertEqual(run_fixture(self.forward(code)), expected)
        self.assertEqual(run_fixture(source), expected)
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_python_for_limite_mutable
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        _, source, expected = case
        code = self.reverse(source)
        self.assertEqual(run_fixture(self.forward(code)), expected)
        self.assertEqual(run_fixture(source), expected)
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_python_for_negativo
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        _, source, expected = case
        code = self.reverse(source)
        self.assertEqual(run_fixture(self.forward(code)), expected)
        self.assertEqual(run_fixture(source), expected)
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_python_for_positivo
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        _, source, expected = case
        code = self.reverse(source)
        self.assertEqual(run_fixture(self.forward(code)), expected)
        self.assertEqual(run_fixture(source), expected)
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_python_for_vacio
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        _, source, expected = case
        code = self.reverse(source)
        self.assertEqual(run_fixture(self.forward(code)), expected)
        self.assertEqual(run_fixture(source), expected)
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_python_funcion
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        _, source, expected = case
        code = self.reverse(source)
        self.assertEqual(run_fixture(self.forward(code)), expected)
        self.assertEqual(run_fixture(source), expected)
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_python_inputs
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test_python_inputs(self):
        code = self.reverse('a = int(input("n: "))\nb = float(input())\nc = input()\nprint(a, b, c)')
        self.assertIn('Definir a Como Entero', code)
        self.assertIn('Escribir Sin Saltar "n: "', code)
        self.assertEqual(run_fixture(self.forward(code), ['2','1.5','sí']), 'n: 2 1.5 sí\n')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_python_logicos
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        _, source, expected = case
        code = self.reverse(source)
        self.assertEqual(run_fixture(self.forward(code)), expected)
        self.assertEqual(run_fixture(source), expected)
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_python_matematicas
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        _, source, expected = case
        code = self.reverse(source)
        self.assertEqual(run_fixture(self.forward(code)), expected)
        self.assertEqual(run_fixture(source), expected)
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_python_print_separador
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        _, source, expected = case
        code = self.reverse(source)
        self.assertEqual(run_fixture(self.forward(code)), expected)
        self.assertEqual(run_fixture(source), expected)
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_python_subproceso
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        _, source, expected = case
        code = self.reverse(source)
        self.assertEqual(run_fixture(self.forward(code)), expected)
        self.assertEqual(run_fixture(source), expected)
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_python_while
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        _, source, expected = case
        code = self.reverse(source)
        self.assertEqual(run_fixture(self.forward(code)), expected)
        self.assertEqual(run_fixture(source), expected)
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_rechazo_pse_arreglo
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        result = translate(source, origin, 'Python' if origin == 'PSeInt' else 'PSeInt')
        self.assertFalse(result.ok, result.code)
        self.assertEqual(result.code, '')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_rechazo_pse_cadena
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        result = translate(source, origin, 'Python' if origin == 'PSeInt' else 'PSeInt')
        self.assertFalse(result.ok, result.code)
        self.assertEqual(result.code, '')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_rechazo_pse_cierre
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        result = translate(source, origin, 'Python' if origin == 'PSeInt' else 'PSeInt')
        self.assertFalse(result.ok, result.code)
        self.assertEqual(result.code, '')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_rechazo_pse_condicion_numerica
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        result = translate(source, origin, 'Python' if origin == 'PSeInt' else 'PSeInt')
        self.assertFalse(result.ok, result.code)
        self.assertEqual(result.code, '')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_rechazo_pse_contador_anidado
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        result = translate(source, origin, 'Python' if origin == 'PSeInt' else 'PSeInt')
        self.assertFalse(result.ok, result.code)
        self.assertEqual(result.code, '')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_rechazo_pse_contador_mutado
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        result = translate(source, origin, 'Python' if origin == 'PSeInt' else 'PSeInt')
        self.assertFalse(result.ok, result.code)
        self.assertEqual(result.code, '')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_rechazo_pse_doble_algoritmo
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        result = translate(source, origin, 'Python' if origin == 'PSeInt' else 'PSeInt')
        self.assertFalse(result.ok, result.code)
        self.assertEqual(result.code, '')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_rechazo_pse_expresion
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        result = translate(source, origin, 'Python' if origin == 'PSeInt' else 'PSeInt')
        self.assertFalse(result.ok, result.code)
        self.assertEqual(result.code, '')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_rechazo_pse_funcion_desconocida
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        result = translate(source, origin, 'Python' if origin == 'PSeInt' else 'PSeInt')
        self.assertFalse(result.ok, result.code)
        self.assertEqual(result.code, '')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_rechazo_pse_lectura_logica
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        result = translate(source, origin, 'Python' if origin == 'PSeInt' else 'PSeInt')
        self.assertFalse(result.ok, result.code)
        self.assertEqual(result.code, '')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_rechazo_pse_leer_contador
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        result = translate(source, origin, 'Python' if origin == 'PSeInt' else 'PSeInt')
        self.assertFalse(result.ok, result.code)
        self.assertEqual(result.code, '')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_rechazo_pse_limite_real
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        result = translate(source, origin, 'Python' if origin == 'PSeInt' else 'PSeInt')
        self.assertFalse(result.ok, result.code)
        self.assertEqual(result.code, '')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_rechazo_pse_paso_cero
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        result = translate(source, origin, 'Python' if origin == 'PSeInt' else 'PSeInt')
        self.assertFalse(result.ok, result.code)
        self.assertEqual(result.code, '')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_rechazo_pse_paso_variable
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        result = translate(source, origin, 'Python' if origin == 'PSeInt' else 'PSeInt')
        self.assertFalse(result.ok, result.code)
        self.assertEqual(result.code, '')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_rechazo_pse_retorno_no_definido
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        result = translate(source, origin, 'Python' if origin == 'PSeInt' else 'PSeInt')
        self.assertFalse(result.ok, result.code)
        self.assertEqual(result.code, '')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_rechazo_pse_segun
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        result = translate(source, origin, 'Python' if origin == 'PSeInt' else 'PSeInt')
        self.assertFalse(result.ok, result.code)
        self.assertEqual(result.code, '')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_rechazo_pse_sin_cierre
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        result = translate(source, origin, 'Python' if origin == 'PSeInt' else 'PSeInt')
        self.assertFalse(result.ok, result.code)
        self.assertEqual(result.code, '')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_rechazo_pse_sino
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        result = translate(source, origin, 'Python' if origin == 'PSeInt' else 'PSeInt')
        self.assertFalse(result.ok, result.code)
        self.assertEqual(result.code, '')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_rechazo_pse_sino_duplicado
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        result = translate(source, origin, 'Python' if origin == 'PSeInt' else 'PSeInt')
        self.assertFalse(result.ok, result.code)
        self.assertEqual(result.code, '')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_rechazo_pse_tipo_asignacion
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        result = translate(source, origin, 'Python' if origin == 'PSeInt' else 'PSeInt')
        self.assertFalse(result.ok, result.code)
        self.assertEqual(result.code, '')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_rechazo_pse_variable_sin_definir
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        result = translate(source, origin, 'Python' if origin == 'PSeInt' else 'PSeInt')
        self.assertFalse(result.ok, result.code)
        self.assertEqual(result.code, '')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_rechazo_py_and_valores
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        result = translate(source, origin, 'Python' if origin == 'PSeInt' else 'PSeInt')
        self.assertFalse(result.ok, result.code)
        self.assertEqual(result.code, '')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_rechazo_py_argumentos
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        result = translate(source, origin, 'Python' if origin == 'PSeInt' else 'PSeInt')
        self.assertFalse(result.ok, result.code)
        self.assertEqual(result.code, '')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_rechazo_py_break
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        result = translate(source, origin, 'Python' if origin == 'PSeInt' else 'PSeInt')
        self.assertFalse(result.ok, result.code)
        self.assertEqual(result.code, '')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_rechazo_py_cadena_escape
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        result = translate(source, origin, 'Python' if origin == 'PSeInt' else 'PSeInt')
        self.assertFalse(result.ok, result.code)
        self.assertEqual(result.code, '')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_rechazo_py_clase
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        result = translate(source, origin, 'Python' if origin == 'PSeInt' else 'PSeInt')
        self.assertFalse(result.ok, result.code)
        self.assertEqual(result.code, '')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_rechazo_py_colision
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        result = translate(source, origin, 'Python' if origin == 'PSeInt' else 'PSeInt')
        self.assertFalse(result.ok, result.code)
        self.assertEqual(result.code, '')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_rechazo_py_comparacion_encadenada
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        result = translate(source, origin, 'Python' if origin == 'PSeInt' else 'PSeInt')
        self.assertFalse(result.ok, result.code)
        self.assertEqual(result.code, '')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_rechazo_py_comprension
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        result = translate(source, origin, 'Python' if origin == 'PSeInt' else 'PSeInt')
        self.assertFalse(result.ok, result.code)
        self.assertEqual(result.code, '')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_rechazo_py_division_entera
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        result = translate(source, origin, 'Python' if origin == 'PSeInt' else 'PSeInt')
        self.assertFalse(result.ok, result.code)
        self.assertEqual(result.code, '')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_rechazo_py_import
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        result = translate(source, origin, 'Python' if origin == 'PSeInt' else 'PSeInt')
        self.assertFalse(result.ok, result.code)
        self.assertEqual(result.code, '')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_rechazo_py_infinito
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        result = translate(source, origin, 'Python' if origin == 'PSeInt' else 'PSeInt')
        self.assertFalse(result.ok, result.code)
        self.assertEqual(result.code, '')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_rechazo_py_input_anidado
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        result = translate(source, origin, 'Python' if origin == 'PSeInt' else 'PSeInt')
        self.assertFalse(result.ok, result.code)
        self.assertEqual(result.code, '')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_rechazo_py_lista
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        result = translate(source, origin, 'Python' if origin == 'PSeInt' else 'PSeInt')
        self.assertFalse(result.ok, result.code)
        self.assertEqual(result.code, '')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_rechazo_py_print_archivo
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        result = translate(source, origin, 'Python' if origin == 'PSeInt' else 'PSeInt')
        self.assertFalse(result.ok, result.code)
        self.assertEqual(result.code, '')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_rechazo_py_print_final
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        result = translate(source, origin, 'Python' if origin == 'PSeInt' else 'PSeInt')
        self.assertFalse(result.ok, result.code)
        self.assertEqual(result.code, '')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_rechazo_py_range_real
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        result = translate(source, origin, 'Python' if origin == 'PSeInt' else 'PSeInt')
        self.assertFalse(result.ok, result.code)
        self.assertEqual(result.code, '')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_rechazo_py_rangocero
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        result = translate(source, origin, 'Python' if origin == 'PSeInt' else 'PSeInt')
        self.assertFalse(result.ok, result.code)
        self.assertEqual(result.code, '')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_rechazo_py_return_temprano
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        result = translate(source, origin, 'Python' if origin == 'PSeInt' else 'PSeInt')
        self.assertFalse(result.ok, result.code)
        self.assertEqual(result.code, '')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_rechazo_py_sintaxis
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        result = translate(source, origin, 'Python' if origin == 'PSeInt' else 'PSeInt')
        self.assertFalse(result.ok, result.code)
        self.assertEqual(result.code, '')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_rechazo_py_string_aritmetica
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        result = translate(source, origin, 'Python' if origin == 'PSeInt' else 'PSeInt')
        self.assertFalse(result.ok, result.code)
        self.assertEqual(result.code, '')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_rechazo_py_tipos_cambiantes
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        result = translate(source, origin, 'Python' if origin == 'PSeInt' else 'PSeInt')
        self.assertFalse(result.ok, result.code)
        self.assertEqual(result.code, '')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_rechazo_py_truthiness
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        result = translate(source, origin, 'Python' if origin == 'PSeInt' else 'PSeInt')
        self.assertFalse(result.ok, result.code)
        self.assertEqual(result.code, '')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_rechazo_py_while_else
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test(self):
        result = translate(source, origin, 'Python' if origin == 'PSeInt' else 'PSeInt')
        self.assertFalse(result.ok, result.code)
        self.assertEqual(result.code, '')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_repeat_multiple
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test_repeat_multiple(self):
        code = self.forward(p('Definir n Como Entero\nRepetir\nn <- n + 1\nHasta Que n >= 3\nEscribir n'))
        self.assertEqual(run_fixture(code), '3\n')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_repeat_once
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test_repeat_once(self):
        code = self.forward(p('Definir n Como Entero\nn <- 0\nRepetir\nn <- n + 1\nHasta Que n = 1\nEscribir n'))
        self.assertEqual(run_fixture(code), '1\n')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_types_defaults
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test_types_defaults(self):
        code = self.forward(p('Definir n Como Entero\nDefinir r Como Real\nDefinir s Como Caracter\nDefinir b Como Logico\nEscribir n, r, s, b'))
        self.assertEqual(run_fixture(code), '00.0False\n')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_engine.EngineTests.test_utf8_files
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test_utf8_files(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'prueba.psc'
            save_code(path, 'Escribir "niño, canción"')
            self.assertEqual(load_code(path), 'Escribir "niño, canción"')
            path.write_bytes(b'\xef\xbb\xbfHola')
            self.assertEqual(load_code(path), 'Hola')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_gui.GuiTests.test_error_clears_old_output
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test_error_clears_old_output(self):
        self.app.source.set(PSE_EXAMPLE)
        self.app.do_translate()
        self.app.source.set('Algoritmo Incompleto')
        self.app.do_translate()
        self.assertEqual(self.app.output.get(), '')
        self.assertIn('Sintaxis', self.app.messages.get('1.0', 'end'))
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_gui.GuiTests.test_example_help_clear
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test_example_help_clear(self):
        self.app.example()
        self.assertEqual(self.app.source.get(), PSE_EXAMPLE)
        self.app.help()
        self.root.update()
        with patch('gui.messagebox.askyesno', return_value=True):
            self.app.clear()
        self.assertEqual(self.app.source.get(), '')
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_gui.GuiTests.test_load_save_copy
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test_load_save_copy(self):
        with tempfile.TemporaryDirectory() as directory:
            source, output = Path(directory)/'entrada.psc', Path(directory)/'salida.py'
            source.write_text(PSE_EXAMPLE, encoding='utf-8')
            with patch('gui.filedialog.askopenfilename', return_value=str(source)):
                self.app.load()
            self.app.do_translate()
            with patch('gui.filedialog.asksaveasfilename', return_value=str(output)) as dialog:
                self.app.save()
                self.assertTrue(dialog.call_args.kwargs['confirmoverwrite'])
            self.assertEqual(output.read_text(encoding='utf-8'), self.app.output.get())
            self.app.copy()
            self.assertEqual(self.root.clipboard_get(), self.app.output.get())
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_gui.GuiTests.test_read_write_errors
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test_read_write_errors(self):
        with patch('gui.filedialog.askopenfilename', return_value='missing.psc'):
            self.app.load()
        self.assertIn('Error al abrir', self.app.messages.get('1.0', 'end'))
        self.app.source.set(PSE_EXAMPLE)
        self.app.do_translate()
        with patch('gui.filedialog.asksaveasfilename', return_value='missing/folder/out.py'):
            self.app.save()
        self.assertIn('Error al guardar', self.app.messages.get('1.0', 'end'))
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

### tests.test_gui.GuiTests.test_window_and_translation_both_ways
Estado: APROBADO

Código de prueba (incluye entrada y aserciones esperadas):
```python
    def test_window_and_translation_both_ways(self):
        self.app.source.set(PSE_EXAMPLE)
        self.app.do_translate()
        self.assertIn('float(input())', self.app.output.get())
        self.app.origin.set('Python')
        self.app.change_direction(True)
        self.assertEqual(self.app.destination.get(), 'PSeInt')
        self.app.source.set(PY_EXAMPLE)
        self.app.do_translate()
        self.assertIn('Leer a', self.app.output.get())
```
Resultado obtenido: Todas las aserciones del caso se cumplieron.

## Evidencia de traducción por programa

### 01_hola_mundo (PSeInt)
Estado: APROBADO
Entrada:
```
Algoritmo Ejemplo
Escribir "Hola mundo"
FinAlgoritmo
```
Resultado esperado:
```
Hola mundo

```
Resultado obtenido:
```
Hola mundo

```
Código generado:
```
import math

print('Hola mundo', sep='', end='\n')
```

### 02_suma (PSeInt)
Estado: APROBADO
Entrada:
```
Algoritmo Ejemplo
Definir a, b Como Entero
Leer a, b
Escribir a + b
FinAlgoritmo
```
Resultado esperado:
```
11

```
Resultado obtenido:
```
11

```
Código generado:
```
import math

a = 0
b = 0
a = int(input())
b = int(input())
print(a + b, sep='', end='\n')
```

### 03_promedio (PSeInt)
Estado: APROBADO
Entrada:
```
Algoritmo Ejemplo
Definir a, b, c Como Real
Leer a, b, c
Escribir (a + b + c) / 3
FinAlgoritmo
```
Resultado esperado:
```
4.0

```
Resultado obtenido:
```
4.0

```
Código generado:
```
import math

a = 0.0
b = 0.0
c = 0.0
a = float(input())
b = float(input())
c = float(input())
print((a + b + c) / 3, sep='', end='\n')
```

### 04_par_impar (PSeInt)
Estado: APROBADO
Entrada:
```
Algoritmo Ejemplo
Definir n Como Entero
Leer n
Si n MOD 2 = 0 Entonces
Escribir "Par"
SiNo
Escribir "Impar"
FinSi
FinAlgoritmo
```
Resultado esperado:
```
Impar

```
Resultado obtenido:
```
Impar

```
Código generado:
```
import math

n = 0
n = int(input())
if n % 2 == 0:
    print('Par', sep='', end='\n')
else:
    print('Impar', sep='', end='\n')
```

### 05_mayor (PSeInt)
Estado: APROBADO
Entrada:
```
Algoritmo Ejemplo
Definir a, b Como Entero
Leer a, b
Si a > b Entonces
Escribir a
SiNo
Escribir b
FinSi
FinAlgoritmo
```
Resultado esperado:
```
9

```
Resultado obtenido:
```
9

```
Código generado:
```
import math

a = 0
b = 0
a = int(input())
b = int(input())
if a > b:
    print(a, sep='', end='\n')
else:
    print(b, sep='', end='\n')
```

### 06_alternativas (PSeInt)
Estado: APROBADO
Entrada:
```
Algoritmo Ejemplo
Definir n Como Entero
Leer n
Si n > 0 Entonces
Escribir "Positivo"
SiNo
Si n < 0 Entonces
Escribir "Negativo"
SiNo
Escribir "Cero"
FinSi
FinSi
FinAlgoritmo
```
Resultado esperado:
```
Cero

```
Resultado obtenido:
```
Cero

```
Código generado:
```
import math

n = 0
n = int(input())
if n > 0:
    print('Positivo', sep='', end='\n')
else:
    if n < 0:
        print('Negativo', sep='', end='\n')
    else:
        print('Cero', sep='', end='\n')
```

### 07_tabla (PSeInt)
Estado: APROBADO
Entrada:
```
Algoritmo Ejemplo
Definir i Como Entero
Para i <- 1 Hasta 3 Hacer
Escribir "5 x ", i, " = ", 5 * i
FinPara
FinAlgoritmo
```
Resultado esperado:
```
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15

```
Resultado obtenido:
```
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15

```
Código generado:
```
import math

i = 0
for i in range(1, (3) + 1, 1):
    print('5 x ', i, ' = ', 5 * i, sep='', end='\n')
```

### 08_suma_ciclo (PSeInt)
Estado: APROBADO
Entrada:
```
Algoritmo Ejemplo
Definir i, total Como Entero
total <- 0
Para i <- 1 Hasta 5 Hacer
total <- total + i
FinPara
Escribir total
FinAlgoritmo
```
Resultado esperado:
```
15

```
Resultado obtenido:
```
15

```
Código generado:
```
import math

i = 0
total = 0
total = 0
for i in range(1, (5) + 1, 1):
    total = total + i
print(total, sep='', end='\n')
```

### 09_factorial (PSeInt)
Estado: APROBADO
Entrada:
```
Algoritmo Ejemplo
Definir n, resultado Como Entero
n <- 5
resultado <- 1
Mientras n > 1 Hacer
resultado <- resultado * n
n <- n - 1
FinMientras
Escribir resultado
FinAlgoritmo
```
Resultado esperado:
```
120

```
Resultado obtenido:
```
120

```
Código generado:
```
import math

n = 0
resultado = 0
n = 5
resultado = 1
while n > 1:
    resultado = resultado * n
    n = n - 1
print(resultado, sep='', end='\n')
```

### 10_funcion (PSeInt)
Estado: APROBADO
Entrada:
```
Funcion r <- Doble(x)
Definir r Como Real
r <- x * 2
FinFuncion
Algoritmo Ejemplo
Escribir Doble(4)
FinAlgoritmo
```
Resultado esperado:
```
8

```
Resultado obtenido:
```
8

```
Código generado:
```
import math

def Doble(x):
    r = 0.0
    r = x * 2
    return r
print(Doble(4), sep='', end='\n')
```

### asignacion (Python)
Estado: APROBADO
Entrada:
```
x = 2
print(x + 3)
```
Resultado esperado:
```
5

```
Resultado obtenido:
```
5

```
Código generado:
```
Algoritmo ProgramaTraducido
    Definir x Como Entero
    x <- 2
    Escribir (x + 3)
FinAlgoritmo
```

### print_separador (Python)
Estado: APROBADO
Entrada:
```
print("a", "b", sep="-", end="")
```
Resultado esperado:
```
a-b
```
Resultado obtenido:
```
a-b
```
Código generado:
```
Algoritmo ProgramaTraducido
    Escribir Sin Saltar "a", "-", "b"
FinAlgoritmo
```

### elif (Python)
Estado: APROBADO
Entrada:
```
n = 0
if n > 0:
    print("positivo")
elif n < 0:
    print("negativo")
else:
    print("cero")
```
Resultado esperado:
```
cero

```
Resultado obtenido:
```
cero

```
Código generado:
```
Algoritmo ProgramaTraducido
    Definir n Como Entero
    n <- 0
    Si (n > 0) Entonces
        Escribir "positivo"
    SiNo
        Si (n < 0) Entonces
            Escribir "negativo"
        SiNo
            Escribir "cero"
        FinSi
    FinSi
FinAlgoritmo
```

### while (Python)
Estado: APROBADO
Entrada:
```
n = 3
while n > 0:
    print(n)
    n -= 1
```
Resultado esperado:
```
3
2
1

```
Resultado obtenido:
```
3
2
1

```
Código generado:
```
Algoritmo ProgramaTraducido
    Definir n Como Entero
    n <- 3
    Mientras (n > 0) Hacer
        Escribir n
        n <- (n - 1)
    FinMientras
FinAlgoritmo
```

### for_positivo (Python)
Estado: APROBADO
Entrada:
```
for i in range(1, 6, 2):
    print(i)
```
Resultado esperado:
```
1
3
5

```
Resultado obtenido:
```
1
3
5

```
Código generado:
```
Algoritmo ProgramaTraducido
    Definir i, ta_indice1, ta_limite1 Como Entero
    ta_indice1 <- 1
    ta_limite1 <- 6
    Mientras ta_indice1 < ta_limite1 Hacer
        i <- ta_indice1
        Escribir i
        ta_indice1 <- ta_indice1 + (2)
    FinMientras
FinAlgoritmo
```

### for_negativo (Python)
Estado: APROBADO
Entrada:
```
for i in range(5, 0, -2):
    print(i)
```
Resultado esperado:
```
5
3
1

```
Resultado obtenido:
```
5
3
1

```
Código generado:
```
Algoritmo ProgramaTraducido
    Definir i, ta_indice1, ta_limite1 Como Entero
    ta_indice1 <- 5
    ta_limite1 <- 0
    Mientras ta_indice1 > ta_limite1 Hacer
        i <- ta_indice1
        Escribir i
        ta_indice1 <- ta_indice1 + (-2)
    FinMientras
FinAlgoritmo
```

### for_vacio (Python)
Estado: APROBADO
Entrada:
```
i = 8
for i in range(3, 1):
    print(i)
print(i)
```
Resultado esperado:
```
8

```
Resultado obtenido:
```
8

```
Código generado:
```
Algoritmo ProgramaTraducido
    Definir i, ta_indice1, ta_limite1 Como Entero
    i <- 8
    ta_indice1 <- 3
    ta_limite1 <- 1
    Mientras ta_indice1 < ta_limite1 Hacer
        i <- ta_indice1
        Escribir i
        ta_indice1 <- ta_indice1 + (1)
    FinMientras
    Escribir i
FinAlgoritmo
```

### for_contador_mutable (Python)
Estado: APROBADO
Entrada:
```
for i in range(3):
    i = 99
print(i)
```
Resultado esperado:
```
99

```
Resultado obtenido:
```
99

```
Código generado:
```
Algoritmo ProgramaTraducido
    Definir i, ta_indice1, ta_limite1 Como Entero
    ta_indice1 <- 0
    ta_limite1 <- 3
    Mientras ta_indice1 < ta_limite1 Hacer
        i <- ta_indice1
        i <- 99
        ta_indice1 <- ta_indice1 + (1)
    FinMientras
    Escribir i
FinAlgoritmo
```

### for_limite_mutable (Python)
Estado: APROBADO
Entrada:
```
n = 3
for i in range(n):
    n = 1
    print(i)
```
Resultado esperado:
```
0
1
2

```
Resultado obtenido:
```
0
1
2

```
Código generado:
```
Algoritmo ProgramaTraducido
    Definir n, i, ta_indice1, ta_limite1 Como Entero
    n <- 3
    ta_indice1 <- 0
    ta_limite1 <- n
    Mientras ta_indice1 < ta_limite1 Hacer
        i <- ta_indice1
        n <- 1
        Escribir i
        ta_indice1 <- ta_indice1 + (1)
    FinMientras
FinAlgoritmo
```

### logicos (Python)
Estado: APROBADO
Entrada:
```
x = 2
if x > 0 and not (x == 3):
    print("bien")
```
Resultado esperado:
```
bien

```
Resultado obtenido:
```
bien

```
Código generado:
```
Algoritmo ProgramaTraducido
    Definir x Como Entero
    x <- 2
    Si ((x > 0) Y (NO (x = 3))) Entonces
        Escribir "bien"
    FinSi
FinAlgoritmo
```

### comentario (Python)
Estado: APROBADO
Entrada:
```
# mensaje
print("Y NO // SiNo") # conservar
```
Resultado esperado:
```
Y NO // SiNo

```
Resultado obtenido:
```
Y NO // SiNo

```
Código generado:
```
// Python línea 1: mensaje
// Python línea 2: conservar
Algoritmo ProgramaTraducido
    Escribir "Y NO // SiNo"
FinAlgoritmo
```

### funcion (Python)
Estado: APROBADO
Entrada:
```
def doble(x):
    r = x * 2
    return r
print(doble(4))
```
Resultado esperado:
```
8

```
Resultado obtenido:
```
8

```
Código generado:
```
SubProceso ta_resultado <- doble(x)
    Definir r, ta_resultado Como Real
    r <- (x * 2)
    ta_resultado <- r
FinSubProceso

Algoritmo ProgramaTraducido
    Escribir doble(4)
FinAlgoritmo
```

### subproceso (Python)
Estado: APROBADO
Entrada:
```
def saludar():
    print("Hola")
saludar()
```
Resultado esperado:
```
Hola

```
Resultado obtenido:
```
Hola

```
Código generado:
```
SubProceso saludar()
    Escribir "Hola"
FinSubProceso

Algoritmo ProgramaTraducido
    saludar()
FinAlgoritmo
```

### matematicas (Python)
Estado: APROBADO
Entrada:
```
import math
print(math.sqrt(9), abs(-2), math.trunc(2.8))
```
Resultado esperado:
```
3.0 2 2

```
Resultado obtenido:
```
3.0 2 2

```
Código generado:
```
Algoritmo ProgramaTraducido
    Escribir RC(9), " ", abs((-2)), " ", TRUNC(2.8)
FinAlgoritmo
```

### anidados (Python)
Estado: APROBADO
Entrada:
```
for i in range(2):
    for j in range(2):
        if i == j:
            print(i, j)
```
Resultado esperado:
```
0 0
1 1

```
Resultado obtenido:
```
0 0
1 1

```
Código generado:
```
Algoritmo ProgramaTraducido
    Definir i, ta_indice1, ta_limite1, j, ta_indice2, ta_limite2 Como Entero
    ta_indice1 <- 0
    ta_limite1 <- 2
    Mientras ta_indice1 < ta_limite1 Hacer
        i <- ta_indice1
        ta_indice2 <- 0
        ta_limite2 <- 2
        Mientras ta_indice2 < ta_limite2 Hacer
            j <- ta_indice2
            Si (i = j) Entonces
                Escribir i, " ", j
            FinSi
            ta_indice2 <- ta_indice2 + (1)
        FinMientras
        ta_indice1 <- ta_indice1 + (1)
    FinMientras
FinAlgoritmo
```

### rechazo_PSeInt_tipo_asignacion (PSeInt)
Estado: APROBADO
Entrada:
```
Algoritmo Ejemplo
Definir n Como Entero
n <- "texto"
FinAlgoritmo
```
Resultado esperado:
```
Diagnóstico y código de salida vacío
```
Resultado obtenido:
```
No compatible, línea 3: Asignación incompatible: n es Entero, la expresión es Cadena.
```
Código generado:
```

```

### rechazo_PSeInt_limite_real (PSeInt)
Estado: APROBADO
Entrada:
```
Algoritmo Ejemplo
Definir i Como Entero
Para i <- 1 Hasta 2.5 Hacer
FinPara
FinAlgoritmo
```
Resultado esperado:
```
Diagnóstico y código de salida vacío
```
Resultado obtenido:
```
No compatible, línea 3: Los límites de Para deben ser enteros.
```
Código generado:
```

```

### rechazo_PSeInt_condicion_numerica (PSeInt)
Estado: APROBADO
Entrada:
```
Algoritmo Ejemplo
Si 1 Entonces
FinSi
FinAlgoritmo
```
Resultado esperado:
```
Diagnóstico y código de salida vacío
```
Resultado obtenido:
```
No compatible, línea 2: La condición debe ser lógica; use una comparación explícita.
```
Código generado:
```

```

### rechazo_PSeInt_leer_contador (PSeInt)
Estado: APROBADO
Entrada:
```
Algoritmo Ejemplo
Definir i Como Entero
Para i <- 1 Hasta 3 Hacer
Leer i
FinPara
FinAlgoritmo
```
Resultado esperado:
```
Diagnóstico y código de salida vacío
```
Resultado obtenido:
```
No compatible, línea 4: Leer no puede modificar un contador de Para activo.
```
Código generado:
```

```

### rechazo_PSeInt_contador_anidado (PSeInt)
Estado: APROBADO
Entrada:
```
Algoritmo Ejemplo
Definir i Como Entero
Para i <- 1 Hasta 3 Hacer
Para i <- 1 Hasta 2 Hacer
FinPara
FinPara
FinAlgoritmo
```
Resultado esperado:
```
Diagnóstico y código de salida vacío
```
Resultado obtenido:
```
No compatible, línea 4: Use contadores diferentes para ciclos Para anidados.
```
Código generado:
```

```

### rechazo_PSeInt_cierre (PSeInt)
Estado: APROBADO
Entrada:
```
Algoritmo A
Si Verdadero Entonces
FinAlgoritmo
```
Resultado esperado:
```
Diagnóstico y código de salida vacío
```
Resultado obtenido:
```
Sintaxis, línea 3: Cierre o alternativa sin el bloque de apertura correspondiente.
```
Código generado:
```

```

### rechazo_PSeInt_sin_cierre (PSeInt)
Estado: APROBADO
Entrada:
```
Algoritmo A
Escribir 1
```
Resultado esperado:
```
Diagnóstico y código de salida vacío
```
Resultado obtenido:
```
Sintaxis, línea 2: Falta cerrar el bloque algoritmo iniciado en la línea 1.
```
Código generado:
```

```

### rechazo_PSeInt_sino (PSeInt)
Estado: APROBADO
Entrada:
```
Algoritmo Ejemplo
SiNo
FinAlgoritmo
```
Resultado esperado:
```
Diagnóstico y código de salida vacío
```
Resultado obtenido:
```
Sintaxis, línea 2: Cierre o alternativa sin el bloque de apertura correspondiente.
```
Código generado:
```

```

### rechazo_PSeInt_sino_duplicado (PSeInt)
Estado: APROBADO
Entrada:
```
Algoritmo Ejemplo
Si Verdadero Entonces
SiNo
SiNo
FinSi
FinAlgoritmo
```
Resultado esperado:
```
Diagnóstico y código de salida vacío
```
Resultado obtenido:
```
Sintaxis, línea 4: SiNo duplicado o con texto adicional.
```
Código generado:
```

```

### rechazo_PSeInt_paso_cero (PSeInt)
Estado: APROBADO
Entrada:
```
Algoritmo Ejemplo
Definir i Como Entero
Para i <- 1 Hasta 3 Con Paso 0 Hacer
FinPara
FinAlgoritmo
```
Resultado esperado:
```
Diagnóstico y código de salida vacío
```
Resultado obtenido:
```
Sintaxis, línea 3: El paso no puede ser cero.
```
Código generado:
```

```

### rechazo_PSeInt_paso_variable (PSeInt)
Estado: APROBADO
Entrada:
```
Algoritmo Ejemplo
Definir i, n Como Entero
Para i <- 1 Hasta 3 Con Paso n Hacer
FinPara
FinAlgoritmo
```
Resultado esperado:
```
Diagnóstico y código de salida vacío
```
Resultado obtenido:
```
No compatible, línea 3: El paso debe ser un entero literal distinto de cero.
```
Código generado:
```

```

### rechazo_PSeInt_variable_sin_definir (PSeInt)
Estado: APROBADO
Entrada:
```
Algoritmo Ejemplo
x <- 1
FinAlgoritmo
```
Resultado esperado:
```
Diagnóstico y código de salida vacío
```
Resultado obtenido:
```
Sintaxis, línea 2: Variable 'x' sin Definir.
```
Código generado:
```

```

### rechazo_PSeInt_expresion (PSeInt)
Estado: APROBADO
Entrada:
```
Algoritmo Ejemplo
Escribir (1 +
FinAlgoritmo
```
Resultado esperado:
```
Diagnóstico y código de salida vacío
```
Resultado obtenido:
```
Sintaxis, línea 2: Paréntesis o lista de expresiones incompleta.
```
Código generado:
```

```

### rechazo_PSeInt_cadena (PSeInt)
Estado: APROBADO
Entrada:
```
Algoritmo Ejemplo
Escribir "hola
FinAlgoritmo
```
Resultado esperado:
```
Diagnóstico y código de salida vacío
```
Resultado obtenido:
```
Sintaxis, línea 2: Símbolo o cadena no admitida cerca de '"hola'.
```
Código generado:
```

```

### rechazo_PSeInt_arreglo (PSeInt)
Estado: APROBADO
Entrada:
```
Algoritmo Ejemplo
Dimension a[3]
FinAlgoritmo
```
Resultado esperado:
```
Diagnóstico y código de salida vacío
```
Resultado obtenido:
```
Sintaxis, línea 2: Símbolo o cadena no admitida cerca de '[3]'.
```
Código generado:
```

```

### rechazo_PSeInt_segun (PSeInt)
Estado: APROBADO
Entrada:
```
Algoritmo Ejemplo
Segun n Hacer
FinAlgoritmo
```
Resultado esperado:
```
Diagnóstico y código de salida vacío
```
Resultado obtenido:
```
No compatible, línea 2: Instrucción 'Segun' no reconocida.
```
Código generado:
```

```

### rechazo_PSeInt_lectura_logica (PSeInt)
Estado: APROBADO
Entrada:
```
Algoritmo Ejemplo
Definir b Como Logico
Leer b
FinAlgoritmo
```
Resultado esperado:
```
Diagnóstico y código de salida vacío
```
Resultado obtenido:
```
No compatible, línea 3: Leer necesita un tipo declarado Entero, Real o Cadena; no admite Logico.
```
Código generado:
```

```

### rechazo_PSeInt_funcion_desconocida (PSeInt)
Estado: APROBADO
Entrada:
```
Algoritmo Ejemplo
Escribir sistema(1)
FinAlgoritmo
```
Resultado esperado:
```
Diagnóstico y código de salida vacío
```
Resultado obtenido:
```
No compatible, línea 2: Función desconocida o cantidad incorrecta de argumentos: sistema.
```
Código generado:
```

```

### rechazo_PSeInt_retorno_no_definido (PSeInt)
Estado: APROBADO
Entrada:
```
Funcion r <- doble(x)
FinFuncion
Algoritmo Ejemplo
Escribir 1
FinAlgoritmo
```
Resultado esperado:
```
Diagnóstico y código de salida vacío
```
Resultado obtenido:
```
Sintaxis, línea 2: Variable 'r' sin Definir.
```
Código generado:
```

```

### rechazo_PSeInt_doble_algoritmo (PSeInt)
Estado: APROBADO
Entrada:
```
Algoritmo Ejemplo
Escribir 1
FinAlgoritmo
Algoritmo Ejemplo
Escribir 2
FinAlgoritmo
```
Resultado esperado:
```
Diagnóstico y código de salida vacío
```
Resultado obtenido:
```
Sintaxis, línea 4: Se permite un único algoritmo principal con nombre.
```
Código generado:
```

```

### rechazo_PSeInt_contador_mutado (PSeInt)
Estado: APROBADO
Entrada:
```
Algoritmo Ejemplo
Definir i Como Entero
Para i <- 1 Hasta 3 Hacer
i <- 1
FinPara
FinAlgoritmo
```
Resultado esperado:
```
Diagnóstico y código de salida vacío
```
Resultado obtenido:
```
No compatible, línea 4: No modifique un contador de Para dentro del ciclo.
```
Código generado:
```

```

### rechazo_Python_infinito (Python)
Estado: APROBADO
Entrada:
```
x = 1e999
```
Resultado esperado:
```
Diagnóstico y código de salida vacío
```
Resultado obtenido:
```
No compatible, línea 1: Use constantes numéricas finitas.
```
Código generado:
```

```

### rechazo_Python_sintaxis (Python)
Estado: APROBADO
Entrada:
```
if True
 print(1)
```
Resultado esperado:
```
Diagnóstico y código de salida vacío
```
Resultado obtenido:
```
Sintaxis, línea 1: expected ':'
```
Código generado:
```

```

### rechazo_Python_lista (Python)
Estado: APROBADO
Entrada:
```
x = [1, 2]
```
Resultado esperado:
```
Diagnóstico y código de salida vacío
```
Resultado obtenido:
```
No compatible, línea 1: Expresión List fuera del subconjunto.
```
Código generado:
```

```

### rechazo_Python_clase (Python)
Estado: APROBADO
Entrada:
```
class A:
    pass
```
Resultado esperado:
```
Diagnóstico y código de salida vacío
```
Resultado obtenido:
```
No compatible, línea 1: Instrucción Python ClassDef no implementada.
```
Código generado:
```

```

### rechazo_Python_import (Python)
Estado: APROBADO
Entrada:
```
import os
```
Resultado esperado:
```
Diagnóstico y código de salida vacío
```
Resultado obtenido:
```
No compatible, línea 1: Instrucción Python Import no implementada.
```
Código generado:
```

```

### rechazo_Python_comprension (Python)
Estado: APROBADO
Entrada:
```
x = [i for i in range(2)]
```
Resultado esperado:
```
Diagnóstico y código de salida vacío
```
Resultado obtenido:
```
No compatible, línea 1: Expresión ListComp fuera del subconjunto.
```
Código generado:
```

```

### rechazo_Python_division_entera (Python)
Estado: APROBADO
Entrada:
```
x = 5 // 2
```
Resultado esperado:
```
Diagnóstico y código de salida vacío
```
Resultado obtenido:
```
No compatible, línea 1: Expresión BinOp fuera del subconjunto.
```
Código generado:
```

```

### rechazo_Python_break (Python)
Estado: APROBADO
Entrada:
```
while True:
    break
```
Resultado esperado:
```
Diagnóstico y código de salida vacío
```
Resultado obtenido:
```
No compatible, línea 2: Instrucción Python Break no implementada.
```
Código generado:
```

```

### rechazo_Python_while_else (Python)
Estado: APROBADO
Entrada:
```
while False:
    pass
else:
    pass
```
Resultado esperado:
```
Diagnóstico y código de salida vacío
```
Resultado obtenido:
```
No compatible, línea 1: while ... else no está implementado.
```
Código generado:
```

```

### rechazo_Python_return_temprano (Python)
Estado: APROBADO
Entrada:
```
def f(x):
    if x > 0:
        return x
    return 0
```
Resultado esperado:
```
Diagnóstico y código de salida vacío
```
Resultado obtenido:
```
No compatible, línea 1: Use un único return con valor al final de la función.
```
Código generado:
```

```

### rechazo_Python_argumentos (Python)
Estado: APROBADO
Entrada:
```
def f(x=1):
    return x
```
Resultado esperado:
```
Diagnóstico y código de salida vacío
```
Resultado obtenido:
```
No compatible, línea 1: Funciones sin decoradores, anotaciones ni parámetros especiales.
```
Código generado:
```

```

### rechazo_Python_print_archivo (Python)
Estado: APROBADO
Entrada:
```
print(1, file=f)
```
Resultado esperado:
```
Diagnóstico y código de salida vacío
```
Resultado obtenido:
```
No compatible, línea 1: print solo admite sep y end literales.
```
Código generado:
```

```

### rechazo_Python_print_final (Python)
Estado: APROBADO
Entrada:
```
print(1, end="!")
```
Resultado esperado:
```
Diagnóstico y código de salida vacío
```
Resultado obtenido:
```
No compatible, línea 1: print admite end='' o end='\n'.
```
Código generado:
```

```

### rechazo_Python_input_anidado (Python)
Estado: APROBADO
Entrada:
```
print(input())
```
Resultado esperado:
```
Diagnóstico y código de salida vacío
```
Resultado obtenido:
```
No compatible, línea 1: Función desconocida o cantidad incorrecta de argumentos: input.
```
Código generado:
```

```

### rechazo_Python_and_valores (Python)
Estado: APROBADO
Entrada:
```
x = 1 and 2
```
Resultado esperado:
```
Diagnóstico y código de salida vacío
```
Resultado obtenido:
```
No compatible, línea 1: and/or requieren valores lógicos, no selección de operandos.
```
Código generado:
```

```

### rechazo_Python_truthiness (Python)
Estado: APROBADO
Entrada:
```
if 1:
    print(1)
```
Resultado esperado:
```
Diagnóstico y código de salida vacío
```
Resultado obtenido:
```
No compatible, línea 1: La condición debe ser lógica: use, por ejemplo, n <> 0 / n != 0.
```
Código generado:
```

```

### rechazo_Python_tipos_cambiantes (Python)
Estado: APROBADO
Entrada:
```
x = 1
x = "a"
```
Resultado esperado:
```
Diagnóstico y código de salida vacío
```
Resultado obtenido:
```
No compatible, línea 2: La variable x cambia de tipo (Entero a Cadena); use otra variable.
```
Código generado:
```

```

### rechazo_Python_colision (Python)
Estado: APROBADO
Entrada:
```
abc = 1
ABC = 2
```
Resultado esperado:
```
Diagnóstico y código de salida vacío
```
Resultado obtenido:
```
No compatible, línea 2: Colisión de nombres: PSeInt no distingue mayúsculas.
```
Código generado:
```

```

### rechazo_Python_rangocero (Python)
Estado: APROBADO
Entrada:
```
for i in range(1, 3, 0):
    print(i)
```
Resultado esperado:
```
Diagnóstico y código de salida vacío
```
Resultado obtenido:
```
No compatible, línea 1: Paso de range: entero literal no nulo.
```
Código generado:
```

```

### rechazo_Python_range_real (Python)
Estado: APROBADO
Entrada:
```
for i in range(1.0):
    print(i)
```
Resultado esperado:
```
Diagnóstico y código de salida vacío
```
Resultado obtenido:
```
No compatible, línea 1: Los límites de range deben ser enteros.
```
Código generado:
```

```

### rechazo_Python_cadena_escape (Python)
Estado: APROBADO
Entrada:
```
print("a\nb")
```
Resultado esperado:
```
Diagnóstico y código de salida vacío
```
Resultado obtenido:
```
No compatible, línea 1: Cadenas con comillas dobles, escapes o saltos de línea.
```
Código generado:
```

```

### rechazo_Python_comparacion_encadenada (Python)
Estado: APROBADO
Entrada:
```
x = 1 < 2 < 3
```
Resultado esperado:
```
Diagnóstico y código de salida vacío
```
Resultado obtenido:
```
No compatible, línea 1: Separe las comparaciones encadenadas usando Y/and.
```
Código generado:
```

```

### rechazo_Python_string_aritmetica (Python)
Estado: APROBADO
Entrada:
```
x = "a" * 3
```
Resultado esperado:
```
Diagnóstico y código de salida vacío
```
Resultado obtenido:
```
No compatible, línea 1: Operaciones aritméticas solo sobre números; no se traduce concatenación ni repetición de cadenas.
```
Código generado:
```

```
