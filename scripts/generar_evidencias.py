"""Genera evidencias de tres fixtures propios; nunca ejecuta entrada del usuario."""
import ast
import contextlib
import ctypes
import hashlib
import io
import json
import platform
import sys
from pathlib import Path
from datetime import datetime, timezone

BASE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE))
from translator import translate
from modern_ui import TEMPLATES

CASES = [
    ("01_saludo", "Hola mundo", "Hola, mundo\n"),
    ("02_condicional", "Si / Entonces", "Mayor de edad\n"),
    ("03_ciclo_mientras", "Mientras", "1\n2\n3\n4\n5\n"),
]

def main():
    screenshot = "--capturas" in sys.argv
    root = app = None
    if screenshot:
        if sys.platform == "win32":
            ctypes.windll.user32.SetProcessDPIAware()
        import tkinter as tk
        from gui import Application
        from PIL import ImageGrab
        root = tk.Tk()
        app = Application(root)
        root.geometry("1280x820+20+20")
        root.attributes("-topmost", True)
    records = []
    try:
        for case_id, name, expected in CASES:
            folder = BASE / "evidencias" / case_id
            folder.mkdir(parents=True, exist_ok=True)
            source = TEMPLATES[name]
            result = translate(source)
            assert result.ok, result.error
            ast.parse(result.code)
            output = io.StringIO()
            # Solo se ejecutan los fixtures constantes de CASES.
            with contextlib.redirect_stdout(output):
                exec(compile(result.code, case_id, "exec"), {})
            actual = output.getvalue()
            assert actual == expected, (case_id, actual, expected)
            (folder/"entrada.psc").write_text(source, encoding="utf-8")
            (folder/"traducido.py").write_text(result.code, encoding="utf-8")
            (folder/"salida_observada.txt").write_text(actual, encoding="utf-8")
            record = dict(caso=case_id, plantilla=name, origen="PSeInt", destino="Python",
                          salida_esperada=expected, salida_observada=actual,
                          coincide=True, advertencias=result.warnings,
                          sha256_entrada=hashlib.sha256(source.encode()).hexdigest(),
                          sha256_traducido=hashlib.sha256(result.code.encode()).hexdigest())
            if screenshot:
                app.source.set(source)
                app.do_translate()
                assert app.output.get() == result.code
                root.update()
                root.after(250, root.quit)
                root.mainloop()
                x,y = root.winfo_rootx(),root.winfo_rooty()
                ImageGrab.grab(bbox=(x,y,x+root.winfo_width(),y+root.winfo_height())).save(folder/"interfaz.png")
                record["captura"] = "interfaz.png"
            (folder/"resultado.json").write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding="utf-8")
            records.append(record)
    finally:
        if root:
            root.destroy()
    report = dict(fecha_utc=datetime.now(timezone.utc).isoformat(),python=sys.version,
                  plataforma=platform.platform(),casos=records,
                  alcance="Ejecución de Python generado para tres fixtures propios; no certifica el intérprete oficial de PSeInt.")
    (BASE/"evidencias"/"resumen.json").write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
    print("3 casos verificados; entradas, traducciones, salidas y registros guardados.")

if __name__ == "__main__":
    main()
