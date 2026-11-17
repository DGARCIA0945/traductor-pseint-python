# Verificación del ejecutable de Windows

Fecha: 27 de octubre de 2026 (America/Bogota).

## Resultado real

- Compilación con PyInstaller 6.16.0: completada, formato `--onefile --windowed`, arquitectura Windows x64.
- Entorno de compilación y prueba: Windows 11, versión 10.0.26200, Python 3.12.14.
- Ejecutable probado: `dist/TraductorAcademico.exe`.
- Prueba del ejecutable final: proceso independiente iniciado sin `PYTHONPATH`, `PYTHONHOME`, `TCL_LIBRARY` ni `TK_LIBRARY` del entorno de desarrollo.
- Código de salida: **0**.
- Creación de ventana Tk: aprobada.
- Traducción PSeInt a Python desde los controles de la GUI: aprobada.
- Traducción Python a PSeInt desde los controles de la GUI: aprobada.
- Detección de la guía incluida en el paquete: aprobada.
- Detección de ejecución empaquetada: aprobada.

Los cinco resultados booleanos se conservan en `prueba_exe.json`. El hash SHA-256 se publica en `SHA256SUMS.txt` en la raíz del proyecto. El ejecutable incorpora Python y Tcl/Tk; no llama a una instalación externa de Python.

## Incidencia encontrada y corregida

El primer empaquetado no pudo inicializar Tcl/Tk en este entorno restringido. Se diagnosticó con una compilación temporal con consola. La versión final configura el directorio de recursos y las variables Tcl/Tk **antes de importar Tkinter**, y usa rutas relativas al directorio de extracción de PyInstaller. La prueba del ejecutable final se realizó después de esta corrección. La aplicación abre los diálogos de archivos en Documentos o en la última carpeta elegida, no en el directorio temporal del paquete.

## Alcance y pendientes de validación externa

La prueba crea una ventana oculta e interactúa con widgets reales. Las 93 pruebas del proyecto verifican adicionalmente el motor, lectura/escritura UTF-8, portapapeles, ayuda, errores y cambios de dirección. Los diálogos se simulan en las pruebas automatizadas. No fue posible capturar una imagen de escritorio desde el entorno; no se adjunta una captura ficticia de la interfaz.

No se probó en Windows 10 ni en una máquina limpia sin Python. La arquitectura del paquete es autónoma, pero la prueba local no certifica todos los equipos ni políticas de antivirus. No se dispuso del intérprete oficial PSeInt: los ejemplos de salida se compararon con referencias y mediante los motores propios, no con ese intérprete. El archivo no está firmado digitalmente.

No se necesitan conexiones de red, servicios ni servidores durante la ejecución. La descarga de PyInstaller y sus dependencias se realizó únicamente durante el desarrollo. El análisis de los módulos de la aplicación no contiene clientes de red.

## Repetir la prueba

Desde la carpeta del proyecto:

```bat
dist\TraductorAcademico.exe --self-test prueba_exe.json
```

Espere a que termine el proceso y revise el JSON. Para reconstruir, siga README.md y ejecute build.bat. Las versiones de las herramientas utilizadas están fijadas en requirements-build.txt. La guía de empaquetado se basa en la documentación oficial: https://pyinstaller.org/en/v6.16.0/usage.html
