# Traductor académico PSeInt ↔ Python

Aplicación de escritorio para traducir un subconjunto documentado de PSeInt y Python. Incluye editores paralelos, numeración de líneas, divisor ajustable, plantillas, inserción de comandos, temas claro/oscuro y una guía plegable. La interfaz no ejecuta el programa del usuario.

## Ejecutar desde el repositorio

Entorno comprobado: Windows 11, Python 3.13.2 y Tcl/Tk. La aplicación utiliza la biblioteca estándar; no requiere instalar paquetes de ejecución con pip. Instala Python con Tcl/Tk y abre una terminal en la carpeta que contiene main.py:

~~~bat
python main.py
~~~

También puedes abrir Abrir_traductor.bat. Si aparece un error de Tkinter, comprueba la instalación con python -m tkinter. La distribución ejecutable se entrega por separado; la carpeta dist no forma parte del repositorio.

## Demostración de un flujo operativo

Abre la aplicación, deja PSeInt como origen y Python como destino, y pulsa la plantilla «Si / Entonces». La plantilla carga el código y ejecuta la función de traducción original. Comprueba la condición edad >= 18 y su correspondencia if/else. El resultado es de solo lectura. Revisa las advertencias, pulsa «Copiar Python» y comprueba el mensaje «¡Copiado!». Pulsa «Descargar .py» y guarda el archivo.

Cambia edad <- 18 por edad <- 15 en el editor izquierdo: el estado indica cambios pendientes. Pulsa Traducir o Ctrl+Enter para actualizar la salida. La edición manual conserva el disparador original; no se traduce automáticamente por cada tecla.

El guion completo, incluidos los resultados esperados y cómo mostrar el manejo de errores, está en [DEMOSTRACION.md](DEMOSTRACION.md).

## Evidencias de tres casos

Las capturas corresponden a la aplicación real. Las salidas se obtuvieron ejecutando exclusivamente tres ejemplos controlados desde un script de verificación, fuera de la interfaz.

| Caso | Comportamiento comprobado | Resultado |
| --- | --- | --- |
| [Saludo](evidencias/01_saludo/) | Escribir se traduce a print | Hola, mundo |
| [Condicional](evidencias/02_condicional/) | Selección de rama para edad = 18 | Mayor de edad |
| [Ciclo Mientras](evidencias/03_ciclo_mientras/) | Condición, incremento y terminación | 1, 2, 3, 4, 5, en líneas separadas |

Cada carpeta incluye entrada.psc, traducido.py, salida_observada.txt, resultado.json e interfaz.png. [El resumen](evidencias/resumen.json) registra fecha UTC, entorno, advertencias y hashes. [El informe](EVIDENCIAS.md) explica la validación.

Para repetir la comprobación de los tres casos sin capturas:

~~~bat
python scripts/generar_evidencias.py
~~~

Para regenerar también las capturas, instala Pillow y ejecuta en una sesión de escritorio visible:

~~~bat
python -m pip install Pillow
python scripts/generar_evidencias.py --capturas
~~~

Pillow solo se necesita para capturas, no para usar el traductor. El script reemplaza las evidencias generadas; nunca debe adaptarse para ejecutar entrada no confiable.

## Pruebas

~~~bat
python -m unittest discover -s tests -v
~~~

La versión entregada cuenta con 98 pruebas aprobadas: 93 originales y 5 de los nuevos controles. El registro es [docs/pruebas_interfaz_moderna.log](docs/pruebas_interfaz_moderna.log). La [autoprueba del ejecutable](docs/prueba_exe_moderno.json) comprobó arranque, traducción en ambos sentidos, ayuda y empaquetado. Estos resultados corresponden al equipo de desarrollo; no certifican todos los sistemas Windows.

## Arquitectura y conservación del motor

main.py inicia la aplicación. gui.py mantiene los controladores originales y conecta la capa visual de modern_ui.py. El editor de entrada se consulta con source.get(); origin y destination determinan la dirección. do_translate() llama a translate(), muestra result.code en output y presenta result.error o result.warnings en messages.

translator.py coordina validación y motores. lexer.py procesa elementos léxicos; expressions.py restringe expresiones; pseint_to_python.py verifica bloques y genera Python; python_to_pseint.py recorre el AST de Python. file_io.py conserva la lectura y escritura UTF-8. El rediseño no modificó estos módulos ni main.py; conservó íntegramente los controladores anteriores.

## Alcance y pendientes

Se admiten variables escalares, asignaciones, entrada/salida, condicionales, Mientras/while, Para/range restringidos y funciones sencillas. [CATALOGO.md](docs/CATALOGO.md) detalla el subconjunto. Arreglos y Según permanecen deshabilitados; no deben presentarse como funcionalidades completadas.

El proyecto tiene limitaciones semánticas conocidas, registradas con prioridad y criterio de aceptación en [PENDIENTES.md](PENDIENTES.md). No se ha certificado la salida con el intérprete oficial de PSeInt. La advertencia del motor debe revisarse incluso cuando la traducción sea aceptada.

## Construir un ejecutable

~~~bat
python -m pip install -r requirements-build.txt
build.bat
~~~

El script ejecuta las pruebas y produce dist/TraductorAcademico.exe con la interfaz actual. El binario de la entrega anterior se llama TraductorAcademicoModerno.exe. Ambos nombres dependen del comando de empaquetado, no de motores diferentes.

## Correspondencia con la entrega

| Requisito | Ubicación |
| --- | --- |
| Repositorio y código completo | Raíz, tests/, examples/, docs/ |
| Demostración de flujo operativo | DEMOSTRACION.md |
| README de ejecución | Este archivo |
| Evidencias de tres casos | EVIDENCIAS.md y evidencias/ |
| Registro de pendientes | PENDIENTES.md |

Los informes antiguos conservados en docs/ son antecedentes; sus fechas y cantidades de pruebas no sustituyen el registro de esta entrega.
