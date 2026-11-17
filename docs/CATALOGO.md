# Catálogo de compatibilidad

Los fragmentos omiten el envoltorio y las declaraciones cuando no son el objeto del ejemplo. Compatible siempre se refiere al perfil académico de la guía.

## 1. Variables y asignaciones

| Instrucción de origen | Equivalencia destino | Estado | Restricciones | Entrada | Salida esperada |
|---|---|---|---|---|---|
| Definir / asignación Python | Inicialización / Definir y <- | Compatible con restricciones | Entero, Real, Cadena, Caracter y Logico. Python conserva un tipo por variable. PSeInt exige declarar antes de usar. | Definir n Como Entero<br>n <- 2 | n = 0<br>n = 2 |
| Algoritmo / Proceso | Cuerpo del módulo Python | Compatible | Un principal; funciones antes del principal. Una instrucción por línea; punto y coma final opcional. | Algoritmo Demo<br>Escribir 1<br>FinAlgoritmo | import math<br>print(1, sep="", end="\n") |
| Asignación aumentada Python | Asignación explícita | Compatible con restricciones | Variable escalar ya inicializada; operaciones numéricas admitidas. | n += 1 | n <- (n + 1) |

## 2. Operadores

| Instrucción de origen | Equivalencia destino | Estado | Restricciones | Entrada | Salida esperada |
|---|---|---|---|---|---|
| + - * / MOD ^ | + - * / % ** | Compatible con restricciones | Valores reales finitos. MOD: usar enteros no negativos. Evitar división por cero y potencias complejas. | Escribir 2 ^ 3, 7 MOD 2 | print(2 ** 3, 7 % 2, sep="", end="\n") |
| Y, O, NO; comparaciones | and, or, not; == != < <= > >= | Compatible con restricciones | Operandos lógicos explícitos. Sin comparaciones encadenadas ni efectos secundarios en condiciones. | Si n > 0 Y NO (n = 3) Entonces | if n > 0 and not n == 3: |
| Python //, cadenas + o * | Sin equivalencia implementada | No compatible | Se rechaza división entera, concatenación y repetición de cadenas. | x = 5 // 2 | Diagnóstico, sin código |

## 3. Entrada y salida

| Instrucción de origen | Equivalencia destino | Estado | Restricciones | Entrada | Salida esperada |
|---|---|---|---|---|---|
| Leer | input con conversión | Compatible con restricciones | Entero -> int; Real -> float; Cadena/Caracter -> str. Leer Logico y parámetros sin tipo: rechazados. | Definir n Como Entero<br>Leer n | n = 0<br>n = int(input()) |
| input / int(input) / float(input) | Mensaje opcional y Leer | Compatible con restricciones | Solo asignación directa; mensaje literal; un valor por lectura. | n = int(input("Edad: ")) | Definir n Como Entero<br>Escribir Sin Saltar "Edad: "<br>Leer n |
| Escribir / print | print / Escribir | Compatible con restricciones | PSeInt concatena argumentos; Python inserta espacios por defecto. sep literal; end vacío o salto. Revisar formato real y lógico. | print("a", "b", sep="-") | Escribir "a", "-", "b" |

## 4. Condicionales

| Instrucción de origen | Equivalencia destino | Estado | Restricciones | Entrada | Salida esperada |
|---|---|---|---|---|---|
| Si / SiNo / FinSi | if / else | Compatible | Anidamiento con cierres correspondientes; bloques vacíos usan pass. | Si n > 0 Entonces<br>Escribir n<br>FinSi | if n > 0:<br>    print(n, sep="", end="\n") |
| Python elif | Si anidado en SiNo | Compatible | Se cierra cada Si anidado. Condiciones de tipo lógico. | if n > 0:<br>    print(1)<br>elif n < 0:<br>    print(-1) | Si (n > 0) Entonces<br>    Escribir 1<br>SiNo<br>    Si (n < 0) Entonces<br>        Escribir (-1)<br>    FinSi<br>FinSi |

## 5. Ciclos

| Instrucción de origen | Equivalencia destino | Estado | Restricciones | Entrada | Salida esperada |
|---|---|---|---|---|---|
| Mientras / while | while / Mientras | Compatible con restricciones | Sin else, break ni continue en Python. No se comprueba terminación. | Mientras n > 0 Hacer<br>n <- n - 1<br>FinMientras | while n > 0:<br>    n = n - 1 |
| Para inclusivo | range con límite ajustado | Compatible con restricciones | Contador y límites enteros; paso literal no nulo. No modificar contador ni depender de su valor final. Límites se evalúan una vez. | Para i <- 5 Hasta 1 Con Paso -2 Hacer | for i in range(5, (1) - 1, -2): |
| Python for range | Mientras y auxiliares | Compatible con restricciones | Uno a tres argumentos; paso literal no nulo. Conserva evaluación única de límites y control independiente del contador visible. | for i in range(3):<br>    print(i) | ta_indice1 <- 0<br>ta_limite1 <- 3<br>Mientras ta_indice1 < ta_limite1 Hacer<br>    i <- ta_indice1<br>    Escribir i<br>    ta_indice1 <- ta_indice1 + (1)<br>FinMientras |
| Repetir / Hasta Que | while True y break condicional | Compatible con restricciones | Solo PSeInt -> Python. Ejecuta al menos una vez. El Python generado con break no pertenece al subconjunto inverso. | Repetir<br>n <- n + 1<br>Hasta Que n >= 3 | while True:<br>    n = n + 1<br>    if n >= 3:<br>        break |

## 6. Funciones

| Instrucción de origen | Equivalencia destino | Estado | Restricciones | Entrada | Salida esperada |
|---|---|---|---|---|---|
| Funcion / SubProceso | def y return final | Compatible con restricciones | Parámetros numéricos por valor; retorno declarado; sin ámbitos globales ni referencias. Funciones antes del principal. | Funcion r <- Doble(x)<br>Definir r Como Real<br>r <- x * 2<br>FinFuncion | def Doble(x):<br>    r = 0.0<br>    r = x * 2<br>    return r |
| Python def / return | SubProceso y variable de retorno | Compatible con restricciones | Un único return con valor al final, o subproceso sin return. Sin defaults, decoradores, anotaciones ni parámetros especiales. | def doble(x):<br>    return x * 2 | SubProceso ta_resultado <- doble(x)<br>    Definir ta_resultado Como Real<br>    ta_resultado <- (x * 2)<br>FinSubProceso |

## 7. Comentarios

| Instrucción de origen | Equivalencia destino | Estado | Restricciones | Entrada | Salida esperada |
|---|---|---|---|---|---|
| // comentario | # comentario | Compatible con restricciones | Se conserva el texto; comentario en línea pasa antes de la instrucción. Las cadenas no se modifican. | Escribir "Y NO //" // nota | # nota<br>print("Y NO //", sep="", end="\n") |
| # comentario Python | // comentario | Compatible con restricciones | Se agrupan en el prólogo con su línea original; no se conserva su posición exacta. | # nota<br>print(1) | // Python línea 1: nota<br>Algoritmo ProgramaTraducido<br>    Escribir 1<br>FinAlgoritmo |

## 8. Funciones matemáticas

| Instrucción de origen | Equivalencia destino | Estado | Restricciones | Entrada | Salida esperada |
|---|---|---|---|---|---|
| ABS RC SEN COS TAN LN EXP TRUNC | abs y módulo math | Compatible con restricciones | Un argumento numérico. Radianes, logaritmo natural y truncamiento hacia cero. Revise dominio y precisión; no se admite REDON. | Escribir RC(9), TRUNC(2.8) | print(math.sqrt(9), math.trunc(2.8), sep="", end="\n") |
| Listas, arreglos, clases, archivos, librerías arbitrarias | Sin implementación | No compatible | También se rechazan Segun, Dimension, try, with, yield, async y comprensiones. | x = [1, 2] | Diagnóstico, sin código |

