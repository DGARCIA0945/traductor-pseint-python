# Registro de pendientes

Estado de esta entrega: prototipo funcional con interfaz renovada, pruebas y ejemplos reproducibles. Los siguientes puntos se registran como trabajo pendiente, no como prestaciones disponibles. Las prioridades indican orden técnico sugerido; no se atribuyen responsables ni fechas comprometidas.

| ID | Prioridad | Pendiente y fundamento | Criterio de aceptación | Estado |
| --- | --- | --- | --- | --- |
| P01 | Alta | Analizar asignación definida por flujo. Una variable asignada solo dentro de una rama puede quedar sin valor en Python, mientras la traducción PSeInt la inicializa. | Rechazar o advertir el caso documentado y probar ramas y bucles sin ejecución. | Pendiente |
| P02 | Alta | Validar parámetros duplicados y restricciones contextuales de funciones. ast.parse no equivale a todas las comprobaciones del compilador. | Rechazar def f(x, x) antes de generar salida; añadir regresión. | Pendiente |
| P03 | Alta | Validar con el intérprete oficial de PSeInt y fijar el perfil utilizado. | Ejecutar casos aceptados en el perfil elegido y guardar versión, entradas y resultados. | Pendiente |
| P04 | Media | Definir y comprobar la política para llamadas recursivas. La aceptación actual no garantiza terminación. | Documentar la política y añadir casos de llamadas directas e indirectas; no prometer decidir la terminación general. | Pendiente |
| P05 | Media | Probar distribución en equipos limpios Windows 10/11 sin Python. | Registrar arquitectura, versión, arranque, traducción y guardado en cada equipo comprobado. | Pendiente |
| P06 | Media | Separar la inferencia compartida del acoplamiento entre motores. | Extraer un módulo común conservando las pruebas; realizarlo en una tarea posterior autorizada. | Pendiente |
| P07 | Baja | Evaluar arreglos/listas y Según dentro de una ampliación formal del lenguaje. | Especificación, reglas, diagnósticos y pruebas antes de habilitar sus controles. | Fuera del alcance actual |
| P08 | Baja | Mejorar accesibilidad y adaptación a diferentes escalas y tamaños de pantalla. | Verificar navegación completa por teclado, foco, contraste y ausencia de controles ocultos en la matriz acordada. | Pendiente |

## Casos que fundamentan los pendientes semánticos

Para P01, el programa Python siguiente tiene una lectura de una variable no definida en la ruta ejecutada:

~~~python
if False:
    n = 1
print(n)
~~~

El motor acepta el caso en la auditoría previa, mientras que la inicialización introducida en PSeInt altera su comportamiento. La interfaz no resuelve esta diferencia; debe conservarse como limitación del motor.

Para P02, la auditoría previa registró la aceptación de parámetros duplicados en def f(x, x): return x. Para P04 se comprobó aceptación de recursión, sin ejecutar recursión indefinida. Estos antecedentes no deben describirse como errores corregidos.

## Trabajo completado y evidencia

La capa visual conserva el motor original, incorpora controles modernos y mantiene la traducción inversa. El registro de 98 pruebas aprobadas está en docs/pruebas_interfaz_moderna.log. La autoprueba empaquetada está en docs/prueba_exe_moderno.json. Los tres casos de esta entrega se encuentran en evidencias/ y pueden regenerarse con el script incluido.
