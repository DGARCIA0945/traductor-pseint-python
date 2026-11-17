# Guía de usuario · Traductor Académico PSeInt-Python

## 1. Objetivo y alcance
Herramienta local para estudiantes que aprenden variables, expresiones, entrada/salida, decisiones, ciclos y funciones. Traduce un subconjunto académico explícito. Traducir significa producir otro texto de código; ejecutar significa correr ese programa. Esta aplicación solo traduce: no evalúa código pegado en el editor ni muestra su resultado de ejecución.

La validación detecta sintaxis, bloques incompletos, nombres no admitidos y varias incompatibilidades de tipos. No demuestra la corrección total del algoritmo. Una traducción aceptada siempre incluye una advertencia de revisión semántica. No equivale a certificación del intérprete PSeInt.

## 2. Instalación y primer uso
El ejecutable está orientado a Windows 10/11 de 64 bits. Abra dist/TraductorAcademico.exe desde la carpeta extraída del ZIP. No necesita Python, servidor, base de datos ni Internet para usarlo. Para desarrollo, use Python 3.10 o posterior con Tcl/Tk. Ejecute python main.py desde la carpeta del proyecto.

Seleccione el lenguaje de origen; el destino cambia automáticamente. Escriba o pegue código en el panel izquierdo, o pulse Ejemplo. Pulse Traducir o Ctrl+Enter. El resultado aparece a la derecha, en un panel de solo lectura. Lea el área inferior: errores de sintaxis y de instrucciones no compatibles impiden generar código; las advertencias requieren revisar el resultado. Los números de línea y las barras de desplazamiento facilitan navegar.

Cargar archivo admite .psc, .py y .txt en UTF-8; las extensiones .psc y .py seleccionan el origen. Guardar resultado propone la extensión de destino y confirma la sobrescritura. Copiar resultado usa el portapapeles. Limpiar y Ejemplo piden confirmación si reemplazan una entrada no vacía. Cambiar la dirección conserva la entrada y borra el resultado anterior. La salida se borra también ante un error de traducción.

## 3. Perfil PSeInt y reglas
Un Algoritmo/FinAlgoritmo o Proceso/FinProceso por archivo, con funciones antes del principal. Palabras clave sin distinción de mayúsculas; identificadores ASCII que empiecen por letra. Se rechazan nombres reservados o que interfieran con funciones incorporadas. Una instrucción por línea, punto y coma final opcional, comentarios //, asignación <-, declaraciones Definir al nivel principal del algoritmo o función. Las cadenas admiten comillas simples o dobles sin escapes; para máxima compatibilidad con PSeInt use comillas dobles. La salida PSeInt usa comillas dobles.

Configure PSeInt con sintaxis flexible que permita funciones/subprocesos, Escribir Sin Saltar e instrucciones sin punto y coma. No se garantiza compatibilidad con todos sus perfiles estrictos. Entero, Real, Cadena, Caracter y Logico son los tipos admitidos; Caracter se trata como cadena y no limita la longitud. Las declaraciones se inicializan a 0, 0.0, cadena vacía o Falso. Declare e inicialice antes de usar en los ejemplos portables.

Los rangos PSeInt son inclusivos; el límite Python se ajusta según el signo del paso. Los range de Python usan auxiliares y Mientras para conservar su límite exclusivo, evaluar sus argumentos una vez y permitir asignaciones al contador visible sin alterar el recorrido. Los nombres auxiliares se eligen para evitar colisiones. Repetir se convierte en while True con condición de salida al final. elif se representa mediante Si anidados.

## 4. Límites y revisión manual
Solo escalares, números reales finitos y funciones sencillas. No se admiten arreglos/listas, índices, diccionarios, clases, excepciones, archivos, importaciones arbitrarias, referencias, funciones anidadas, closures, retornos anticipados, defaults, decoradores, anotaciones, break/continue de entrada Python, for/while con else, división entera ni concatenación/repetición de cadenas. Solo import math sin alias. Las condiciones deben ser lógicas, sin truthiness ni comparaciones encadenadas. input solo se admite en asignación directa, con conversión int/float/str opcional y mensaje literal.

Revise estas diferencias: formato de reales y booleanos al imprimir; precisión y tamaño de números; dominio de raíces, logaritmos y potencias; división por cero; entrada numérica inválida; tratamiento de espacios en Leer; MOD con operandos negativos; evaluación de expresiones lógicas con efectos secundarios. Use MOD solo con enteros no negativos y condiciones sin efectos secundarios. No se validan todos los errores de ejecución.

En PSeInt, no modifique contadores Para ni dependa de su valor después del ciclo; los límites se evalúan una sola vez. Python debe inicializar variables antes de todos los caminos que las usan: no hay análisis completo de asignación por rama y las declaraciones PSeInt tienen valores por defecto. Las funciones reciben escalares numéricos por valor; los parámetros se analizan como Real. Use funciones en orden de dependencia, sin recursión ni llamadas con efectos secundarios en expresiones. La inferencia de tipos es conservadora; Python no puede cambiar el tipo de una variable. PSeInt permite asignar Entero a Real, pero se rechaza Real a Entero.

No se garantiza una conversión de ida y vuelta de todo el código generado: por ejemplo, Repetir produce break y la dirección inversa rechaza break. Los comentarios Python se trasladan al inicio con su número de línea original. Límites de entrada: 150 000 caracteres y 3000 líneas. Revise manualmente antes de entregar o ejecutar el código en su entorno académico.

## 5. Pruebas y mantenimiento
Ejecute python -m unittest discover -s tests -v. Ejecute python run_tests.py para regenerar el informe, el log y los datos JSON. Las pruebas ejecutan únicamente fixtures propios: comparan salidas esperadas, rechazos, cierres, tipos, límites de ciclos y GUI. ast.parse comprueba sintaxis Python sin ejecutar; no demuestra equivalencia semántica. Las pruebas de ida y vuelta usan ambos motores propios, por lo que no sustituyen la validación en PSeInt. No se dispuso del intérprete oficial PSeInt para esta entrega.

Consulte INFORME_PRUEBAS.md y resultados_pruebas.json para los resultados reales, con entrada, salida esperada, obtenida y estado. Consulte VERIFICACION_EMPAQUETADO.md para el alcance de la prueba del ejecutable. Antes de distribución institucional, pruebe en Windows 10 y 11 sin Python instalado y con la configuración PSeInt de la institución.

## 6. Empaquetado reproducible
En Windows, cree y active un entorno virtual: python -m venv .venv, después .venv\Scripts\activate. Instale python -m pip install -r requirements-build.txt y ejecute build.bat. El script ejecuta unittest antes de compilar. PyInstaller se usa solo para empaquetar.

Comando exacto: python -m PyInstaller --noconfirm --clean --onefile --windowed --name TraductorAcademico --add-data "docs;docs" main.py

El archivo se genera en dist/TraductorAcademico.exe. Las guías viajan en docs. No hay iconos externos; el logotipo es textual. Para añadir un .ico propio use --icon ruta\icono.ico. Si faltan Tcl/Tk, repare la instalación de Python. Si faltan recursos, revise --add-data y el directorio de compilación. Para investigar fallos de arranque, compile sin --windowed; para problemas de extracción temporal pruebe --onedir. No se certifica funcionamiento universal y el binario no está firmado.

Referencia oficial: https://pyinstaller.org/en/v6.16.0/usage.html

## 7. Catálogo de instrucciones

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


## 8. Diez ejemplos académicos completos

### 01 hola mundo

Origen PSeInt:
```
Algoritmo Ejemplo
Escribir "Hola mundo"
FinAlgoritmo
```

Destino Python:
```python
import math

print('Hola mundo', sep='', end='\n')
```

Datos de entrada: []. Salida observable esperada:
```
Hola mundo
```

### 02 suma

Origen PSeInt:
```
Algoritmo Ejemplo
Definir a, b Como Entero
Leer a, b
Escribir a + b
FinAlgoritmo
```

Destino Python:
```python
import math

a = 0
b = 0
a = int(input())
b = int(input())
print(a + b, sep='', end='\n')
```

Datos de entrada: ['4', '7']. Salida observable esperada:
```
11
```

### 03 promedio

Origen PSeInt:
```
Algoritmo Ejemplo
Definir a, b, c Como Real
Leer a, b, c
Escribir (a + b + c) / 3
FinAlgoritmo
```

Destino Python:
```python
import math

a = 0.0
b = 0.0
c = 0.0
a = float(input())
b = float(input())
c = float(input())
print((a + b + c) / 3, sep='', end='\n')
```

Datos de entrada: ['3', '4', '5']. Salida observable esperada:
```
4.0
```

### 04 par impar

Origen PSeInt:
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

Destino Python:
```python
import math

n = 0
n = int(input())
if n % 2 == 0:
    print('Par', sep='', end='\n')
else:
    print('Impar', sep='', end='\n')
```

Datos de entrada: ['7']. Salida observable esperada:
```
Impar
```

### 05 mayor

Origen PSeInt:
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

Destino Python:
```python
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

Datos de entrada: ['9', '2']. Salida observable esperada:
```
9
```

### 06 alternativas

Origen PSeInt:
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

Destino Python:
```python
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

Datos de entrada: ['0']. Salida observable esperada:
```
Cero
```

### 07 tabla

Origen PSeInt:
```
Algoritmo Ejemplo
Definir i Como Entero
Para i <- 1 Hasta 3 Hacer
Escribir "5 x ", i, " = ", 5 * i
FinPara
FinAlgoritmo
```

Destino Python:
```python
import math

i = 0
for i in range(1, (3) + 1, 1):
    print('5 x ', i, ' = ', 5 * i, sep='', end='\n')
```

Datos de entrada: []. Salida observable esperada:
```
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
```

### 08 suma ciclo

Origen PSeInt:
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

Destino Python:
```python
import math

i = 0
total = 0
total = 0
for i in range(1, (5) + 1, 1):
    total = total + i
print(total, sep='', end='\n')
```

Datos de entrada: []. Salida observable esperada:
```
15
```

### 09 factorial

Origen PSeInt:
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

Destino Python:
```python
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

Datos de entrada: []. Salida observable esperada:
```
120
```

### 10 funcion

Origen PSeInt:
```
Funcion r <- Doble(x)
Definir r Como Real
r <- x * 2
FinFuncion
Algoritmo Ejemplo
Escribir Doble(4)
FinAlgoritmo
```

Destino Python:
```python
import math

def Doble(x):
    r = 0.0
    r = x * 2
    return r
print(Doble(4), sep='', end='\n')
```

Datos de entrada: []. Salida observable esperada:
```
8
```

### Python a PSeInt: elif

```python
n = 0
if n > 0:
    print("positivo")
elif n < 0:
    print("negativo")
else:
    print("cero")
```

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

### Python a PSeInt: for_negativo

```python
for i in range(5, 0, -2):
    print(i)
```

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

### Python a PSeInt: funcion

```python
def doble(x):
    r = x * 2
    return r
print(doble(4))
```

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
