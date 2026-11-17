# Interfaz moderna — 17 de noviembre de 2026

Abra dist/TraductorAcademicoModerno.exe. Para ejecutar el código fuente con Python y Tkinter: python main.py, o Abrir_traductor.bat.

Esta entrega rediseña la aplicación existente de escritorio Tkinter. No utiliza HTML, React ni un servidor web.

La entrada sigue siendo source.get(); origin y destination conservan sus nombres. El controlador original do_translate() llama a translator.translate(), escribe result.code en output y muestra result.error o result.warnings en messages. modern_ui.py construye los widgets y añade controles visuales mediante una subclase. gui.py conserva su código original y agrega únicamente la conexión a esa subclase al final. main.py y los módulos del motor no se modificaron.

Las plantillas compatibles cargan PSeInt y llaman al controlador original. La edición manual se traduce al pulsar Traducir o Ctrl+Enter. Los botones de comandos insertan texto en el cursor; las variables de las estructuras deben declararse y completarse. Arreglos y Según permanecen deshabilitados porque el motor no los admite. La traducción inversa Python a PSeInt continúa disponible.

El divisor se arrastra para ajustar los editores. El selector cambia el tema claro/oscuro. Copiar muestra temporalmente «¡Copiado!». Descargar reutiliza el guardado original, con extensión correspondiente al destino. La guía visual es plegable. Los mensajes originales se conservan, incluidas las advertencias semánticas: el estado de una traducción aceptada indica «Sincronizado · revisar advertencias».

Validación: 93 pruebas originales y 5 pruebas nuevas de interfaz. El registro de esta versión está en docs/pruebas_interfaz_moderna.log. Los resultados históricos de otros documentos corresponden a entregas anteriores. El diseño fue revisado visualmente en ambos temas. No se amplió la compatibilidad del lenguaje ni se corrigieron limitaciones semánticas anteriores.

Para compilar: instale requirements-build.txt y ejecute build.bat. Ese comando conserva su nombre de salida histórico TraductorAcademico.exe; contiene la nueva interfaz cuando se compila desde estas fuentes.
