"""Casos de referencia: entradas y salidas esperadas independientes del motor."""
def p(body):
    return "Algoritmo Ejemplo\n" + body + "\nFinAlgoritmo\n"


ACADEMIC = [
    ("01_hola_mundo", p('Escribir "Hola mundo"'), [], "Hola mundo\n"),
    ("02_suma", p('Definir a, b Como Entero\nLeer a, b\nEscribir a + b'), ["4", "7"], "11\n"),
    ("03_promedio", p('Definir a, b, c Como Real\nLeer a, b, c\nEscribir (a + b + c) / 3'), ["3", "4", "5"], "4.0\n"),
    ("04_par_impar", p('Definir n Como Entero\nLeer n\nSi n MOD 2 = 0 Entonces\nEscribir "Par"\nSiNo\nEscribir "Impar"\nFinSi'), ["7"], "Impar\n"),
    ("05_mayor", p('Definir a, b Como Entero\nLeer a, b\nSi a > b Entonces\nEscribir a\nSiNo\nEscribir b\nFinSi'), ["9", "2"], "9\n"),
    ("06_alternativas", p('Definir n Como Entero\nLeer n\nSi n > 0 Entonces\nEscribir "Positivo"\nSiNo\nSi n < 0 Entonces\nEscribir "Negativo"\nSiNo\nEscribir "Cero"\nFinSi\nFinSi'), ["0"], "Cero\n"),
    ("07_tabla", p('Definir i Como Entero\nPara i <- 1 Hasta 3 Hacer\nEscribir "5 x ", i, " = ", 5 * i\nFinPara'), [], "5 x 1 = 5\n5 x 2 = 10\n5 x 3 = 15\n"),
    ("08_suma_ciclo", p('Definir i, total Como Entero\ntotal <- 0\nPara i <- 1 Hasta 5 Hacer\ntotal <- total + i\nFinPara\nEscribir total'), [], "15\n"),
    ("09_factorial", p('Definir n, resultado Como Entero\nn <- 5\nresultado <- 1\nMientras n > 1 Hacer\nresultado <- resultado * n\nn <- n - 1\nFinMientras\nEscribir resultado'), [], "120\n"),
    ("10_funcion", 'Funcion r <- Doble(x)\nDefinir r Como Real\nr <- x * 2\nFinFuncion\n' + p('Escribir Doble(4)'), [], "8\n"),
]

PYTHON_CASES = [
    ("asignacion", "x = 2\nprint(x + 3)", "5\n"),
    ("print_separador", 'print("a", "b", sep="-", end="")', "a-b"),
    ("elif", 'n = 0\nif n > 0:\n    print("positivo")\nelif n < 0:\n    print("negativo")\nelse:\n    print("cero")', "cero\n"),
    ("while", 'n = 3\nwhile n > 0:\n    print(n)\n    n -= 1', "3\n2\n1\n"),
    ("for_positivo", 'for i in range(1, 6, 2):\n    print(i)', "1\n3\n5\n"),
    ("for_negativo", 'for i in range(5, 0, -2):\n    print(i)', "5\n3\n1\n"),
    ("for_vacio", 'i = 8\nfor i in range(3, 1):\n    print(i)\nprint(i)', "8\n"),
    ("for_contador_mutable", 'for i in range(3):\n    i = 99\nprint(i)', "99\n"),
    ("for_limite_mutable", 'n = 3\nfor i in range(n):\n    n = 1\n    print(i)', "0\n1\n2\n"),
    ("logicos", 'x = 2\nif x > 0 and not (x == 3):\n    print("bien")', "bien\n"),
    ("comentario", '# mensaje\nprint("Y NO // SiNo") # conservar', "Y NO // SiNo\n"),
    ("funcion", 'def doble(x):\n    r = x * 2\n    return r\nprint(doble(4))', "8\n"),
    ("subproceso", 'def saludar():\n    print("Hola")\nsaludar()', "Hola\n"),
    ("matematicas", 'import math\nprint(math.sqrt(9), abs(-2), math.trunc(2.8))', "3.0 2 2\n"),
    ("anidados", 'for i in range(2):\n    for j in range(2):\n        if i == j:\n            print(i, j)', "0 0\n1 1\n"),
]
