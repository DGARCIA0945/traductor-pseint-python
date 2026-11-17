@echo off
setlocal
cd /d "%~dp0"
python -m unittest discover -s tests -v
if errorlevel 1 exit /b 1
python -m PyInstaller --noconfirm --clean --onefile --windowed --name TraductorAcademico --add-data "docs;docs" main.py
if errorlevel 1 exit /b 1
echo Ejecutable disponible en dist\TraductorAcademico.exe
endlocal
