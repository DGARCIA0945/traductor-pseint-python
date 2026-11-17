"""Interfaz local Tkinter/ttk. Nunca ejecuta el código introducido."""
import sys
from pathlib import Path
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from translator import translate
from file_io import load_code, save_code

PSE_EXAMPLE = '''Algoritmo Suma
    Definir a, b Como Real
    Escribir "Primer número:"
    Leer a
    Escribir "Segundo número:"
    Leer b
    Escribir "Suma: ", a + b
FinAlgoritmo
'''
PY_EXAMPLE = '''# Suma de dos números
a = float(input("Primer número: "))
b = float(input("Segundo número: "))
print("Suma:", a + b)
'''


class CodeEditor(ttk.Frame):
    def __init__(self, parent, background, readonly=False):
        super().__init__(parent)
        self.readonly = readonly
        self.numbers = tk.Canvas(self, width=46, bg="#edf1f7", highlightthickness=0)
        self.text = tk.Text(self, wrap="none", undo=True, font=("Consolas", 11), bg=background,
                            fg="#172b4d", insertbackground="#165dbe", relief="flat", padx=10, pady=10)
        self.vertical = ttk.Scrollbar(self, orient="vertical", command=self.scroll)
        horizontal = ttk.Scrollbar(self, orient="horizontal", command=self.text.xview)
        self.text.configure(yscrollcommand=self.on_scroll, xscrollcommand=horizontal.set)
        self.numbers.grid(row=0, column=0, sticky="ns")
        self.text.grid(row=0, column=1, sticky="nsew")
        self.vertical.grid(row=0, column=2, sticky="ns")
        horizontal.grid(row=1, column=1, sticky="ew")
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        for event in ("<KeyRelease>", "<Configure>", "<<Modified>>"):
            self.text.bind(event, lambda e: self.after_idle(self.redraw), add=True)
        self.text.bind("<Tab>", self.tab)
        if readonly:
            self.text.configure(state="disabled")

    def tab(self, event):
        if not self.readonly:
            self.text.insert("insert", "    ")
        return "break"

    def scroll(self, *args):
        self.text.yview(*args)
        self.redraw()

    def on_scroll(self, *args):
        self.vertical.set(*args)
        self.redraw()

    def redraw(self):
        self.numbers.delete("all")
        index = self.text.index("@0,0")
        while True:
            info = self.text.dlineinfo(index)
            if info is None:
                break
            self.numbers.create_text(38, info[1], anchor="ne", text=index.split('.')[0], fill="#63748a", font=("Consolas", 10))
            index = self.text.index(index + "+1line")

    def get(self):
        return self.text.get("1.0", "end-1c")

    def set(self, value):
        self.text.configure(state="normal")
        self.text.delete("1.0", "end")
        self.text.insert("1.0", value)
        self.text.edit_modified(False)
        if self.readonly:
            self.text.configure(state="disabled")
        self.redraw()


class Application(ttk.Frame):
    def __init__(self, root):
        super().__init__(root, padding=18)
        self.root = root
        self.last_directory = str(Path.home() / 'Documents')
        root.title("Traductor Académico PSeInt-Python")
        root.geometry("1180x760")
        root.minsize(850, 580)
        style = ttk.Style(root)
        style.theme_use("clam")
        style.configure("TFrame", background="#eef3f9")
        style.configure("TLabel", background="#eef3f9", foreground="#172b4d", font=("Segoe UI", 10))
        style.configure("Title.TLabel", font=("Segoe UI", 20, "bold"))
        style.configure("TButton", font=("Segoe UI", 10), padding=(11, 8))
        style.configure("Accent.TButton", background="#185abc", foreground="white")
        self.pack(fill="both", expand=True)
        ttk.Label(self, text="P ⇄ Py   Traductor Académico", style="Title.TLabel").pack(anchor="w")
        ttk.Label(self, text="PSeInt y Python · Traducción local · Aprende comparando ambos lenguajes").pack(anchor="w", pady=(3, 17))
        selectors = ttk.Frame(self)
        selectors.pack(fill="x", pady=(0, 12))
        self.origin, self.destination = tk.StringVar(value="PSeInt"), tk.StringVar(value="Python")
        ttk.Label(selectors, text="Origen").pack(side="left")
        source_box = ttk.Combobox(selectors, textvariable=self.origin, values=("PSeInt", "Python"), state="readonly", width=13)
        source_box.pack(side="left", padx=(8, 22))
        ttk.Label(selectors, text="Destino").pack(side="left")
        target_box = ttk.Combobox(selectors, textvariable=self.destination, values=("Python", "PSeInt"), state="readonly", width=13)
        target_box.pack(side="left", padx=8)
        source_box.bind("<<ComboboxSelected>>", lambda e: self.change_direction(True))
        target_box.bind("<<ComboboxSelected>>", lambda e: self.change_direction(False))
        ttk.Button(selectors, text="Ayuda y compatibilidad", command=self.help).pack(side="right")
        panes = ttk.Panedwindow(self, orient="horizontal")
        panes.pack(fill="both", expand=True)
        left, right = ttk.Frame(panes), ttk.Frame(panes)
        panes.add(left, weight=1)
        panes.add(right, weight=1)
        ttk.Label(left, text="CÓDIGO DE ENTRADA", font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=(0, 7))
        ttk.Label(right, text="RESULTADO · SOLO LECTURA", font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=(0, 7))
        self.source = CodeEditor(left, "#ffffff")
        self.output = CodeEditor(right, "#f0f8ff", readonly=True)
        self.source.pack(fill="both", expand=True, padx=(0, 7))
        self.output.pack(fill="both", expand=True, padx=(7, 0))
        actions = ttk.Frame(self)
        actions.pack(fill="x", pady=14)
        for label, command, accent in [("Traducir", self.do_translate, True), ("Cargar archivo", self.load, False), ("Guardar resultado", self.save, False), ("Copiar resultado", self.copy, False), ("Limpiar", self.clear, False), ("Ejemplo", self.example, False)]:
            ttk.Button(actions, text=label, command=command, style="Accent.TButton" if accent else "TButton").pack(side="left", padx=(0, 7))
        self.messages = tk.Text(self, height=5, wrap="word", bg="#e2eaf5", fg="#172b4d", relief="flat", font=("Segoe UI", 10), padx=10, pady=8, state="disabled")
        self.messages.pack(fill="x")
        self.message("Listo. Introduzca código o pulse Ejemplo. Ctrl+Enter: traducir. La aplicación no ejecuta programas.")
        root.bind("<Control-Return>", lambda e: self.do_translate())
        root.protocol("WM_DELETE_WINDOW", self.close)

    def message(self, value):
        self.messages.configure(state="normal")
        self.messages.delete("1.0", "end")
        self.messages.insert("1.0", value)
        self.messages.configure(state="disabled")

    def change_direction(self, from_source):
        other = {"Python": "PSeInt", "PSeInt": "Python"}
        if from_source:
            self.destination.set(other[self.origin.get()])
        else:
            self.origin.set(other[self.destination.get()])
        self.output.set("")
        self.message("Dirección actualizada. El código de entrada se conserva; compruebe que corresponde al lenguaje seleccionado.")

    def do_translate(self):
        result = translate(self.source.get(), self.origin.get(), self.destination.get())
        self.output.set(result.code)
        if not result.ok:
            self.message(result.error)
        elif result.warnings:
            self.message("Traducción con advertencias:\n" + "\n".join("• " + w for w in result.warnings))
        else:
            self.message("Traducción exitosa.")

    def can_replace(self):
        return not self.source.get().strip() or messagebox.askyesno("Reemplazar entrada", "¿Desea reemplazar el código de entrada actual?", parent=self.root)

    def example(self):
        if self.can_replace():
            self.source.set(PSE_EXAMPLE if self.origin.get() == "PSeInt" else PY_EXAMPLE)
            self.output.set("")
            self.message("Ejemplo cargado. Pulse Traducir.")

    def load(self):
        path = filedialog.askopenfilename(parent=self.root, initialdir=self.last_directory, filetypes=[("Código", "*.psc *.py *.txt"), ("Todos", "*.*")])
        if not path:
            return
        try:
            code = load_code(path)
            if not self.can_replace():
                return
            self.source.set(code)
            self.last_directory = str(Path(path).parent)
            if Path(path).suffix.lower() in (".psc", ".py"):
                self.origin.set("Python" if Path(path).suffix.lower() == ".py" else "PSeInt")
                self.change_direction(True)
            self.output.set("")
            self.message("Archivo cargado en UTF-8: " + path)
        except (OSError, UnicodeError) as exc:
            self.message("Error al abrir archivo: " + str(exc))

    def save(self):
        if not self.output.get():
            self.message("No hay resultado para guardar.")
            return
        extension = ".py" if self.destination.get() == "Python" else ".psc"
        path = filedialog.asksaveasfilename(parent=self.root, initialdir=self.last_directory, defaultextension=extension, confirmoverwrite=True, filetypes=[("Código traducido", "*" + extension), ("Texto", "*.txt")])
        if path:
            try:
                save_code(path, self.output.get())
                self.last_directory = str(Path(path).parent)
                self.message("Resultado guardado en UTF-8: " + path)
            except (OSError, UnicodeError) as exc:
                self.message("Error al guardar archivo: " + str(exc))

    def copy(self):
        if not self.output.get():
            self.message("No hay resultado para copiar.")
            return
        self.root.clipboard_clear()
        self.root.clipboard_append(self.output.get())
        self.message("Resultado copiado al portapapeles.")

    def clear(self):
        if self.can_replace():
            self.source.set("")
            self.output.set("")
            self.message("Editores vacíos.")

    def close(self):
        if not self.source.text.edit_modified() or messagebox.askyesno("Salir", "Hay cambios en la entrada. ¿Desea cerrar la aplicación?", parent=self.root):
            self.root.destroy()

    def help(self):
        window = tk.Toplevel(self.root)
        window.title("Ayuda y compatibilidad")
        window.geometry("820x620")
        frame = CodeEditor(window, "white", readonly=True)
        frame.pack(fill="both", expand=True, padx=15, pady=15)
        base = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parent))
        try:
            frame.set(load_code(base / "docs" / "GUIA.md"))
        except OSError:
            frame.set("Consulte docs/GUIA.md y docs/Guia_de_usuario.pdf en la carpeta del proyecto.")

# Adaptador visual: los controladores originales permanecen intactos.
from modern_ui import create_application_class
Application = create_application_class(Application, CodeEditor)
