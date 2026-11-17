"""Punto de entrada para Python y PyInstaller."""
import sys
import json
import os
from pathlib import Path


def main():
    self_test_path = Path(sys.argv[2]).resolve() if len(sys.argv) == 3 and sys.argv[1] == '--self-test' else None
    # Recursos del bundle: rutas relativas también funcionan en escritorios
    # restringidos donde Tcl no puede resolver ciertas rutas absolutas.
    if getattr(sys, 'frozen', False):
        base = Path(sys._MEIPASS)
        os.chdir(base)
        os.environ['TCL_LIBRARY'] = '_tcl_data'
        os.environ['TK_LIBRARY'] = '_tk_data'
    import tkinter as tk
    from gui import Application
    root = tk.Tk()
    app = Application(root)
    if self_test_path is not None:
        # Prueba reproducible del ejecutable: no interpreta argumentos como código.
        from gui import PSE_EXAMPLE, PY_EXAMPLE
        root.withdraw()
        root.update()
        app.source.set(PSE_EXAMPLE)
        app.do_translate()
        forward = 'float(input())' in app.output.get()
        app.origin.set('Python')
        app.change_direction(True)
        app.source.set(PY_EXAMPLE)
        app.do_translate()
        reverse = 'Leer a' in app.output.get()
        base = Path(getattr(sys, '_MEIPASS', Path(__file__).resolve().parent))
        checks = dict(ventana=True, pseint_a_python=forward, python_a_pseint=reverse,
                      ayuda=(base/'docs'/'GUIA.md').is_file(), empaquetado=bool(getattr(sys, 'frozen', False)))
        self_test_path.write_text(json.dumps(checks, ensure_ascii=False, indent=2), encoding='utf-8')
        root.destroy()
        raise SystemExit(0 if all(checks.values()) else 1)
    root.mainloop()


if __name__ == "__main__":
    main()
