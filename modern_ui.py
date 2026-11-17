"""Capa visual. Reutiliza los controladores originales sin cambiar el motor."""
import tkinter as tk
from tkinter import ttk
from pathlib import Path

TEMPLATES = {
    "Hola mundo": 'Algoritmo Saludo\n    Escribir "Hola, mundo"\nFinAlgoritmo\n',
    "Si / Entonces": 'Algoritmo Condicional\n    Definir edad Como Entero\n    edad <- 18\n    Si edad >= 18 Entonces\n        Escribir "Mayor de edad"\n    SiNo\n        Escribir "Menor de edad"\n    FinSi\nFinAlgoritmo\n',
    "Mientras": 'Algoritmo Contador\n    Definir i Como Entero\n    i <- 1\n    Mientras i <= 5 Hacer\n        Escribir i\n        i <- i + 1\n    FinMientras\nFinAlgoritmo\n',
    "Para": 'Algoritmo Recorrido\n    Definir i Como Entero\n    Para i <- 1 Hasta 5 Hacer\n        Escribir i\n    FinPara\nFinAlgoritmo\n',
}
SNIPPETS = {
    "Escribir": 'Escribir "Hola"',
    "Leer": 'Leer dato',
    "Si": 'Si condicion Entonces\n    Escribir "Se cumple"\nFinSi',
    "Mientras": 'Mientras condicion Hacer\n    // Actualizar la condicion\nFinMientras',
    "Para": 'Para i <- 1 Hasta 5 Hacer\n    Escribir i\nFinPara',
}
DARK = dict(bg="#111318", panel="#181b22", editor="#14171d", fg="#e6e9ef",
            muted="#9ba5b6", border="#303644", accent="#8b7cf8", select="#39315d",
            good="#73d6ac", warning="#f2c779", error="#ff929c")
LIGHT = dict(bg="#f3f4f8", panel="#ffffff", editor="#ffffff", fg="#202430",
             muted="#626c7f", border="#dce0e8", accent="#6550ce", select="#e6e0ff",
             good="#16704d", warning="#865900", error="#b5263b")


def create_application_class(Base, Editor):
    class ModernEditor(Editor):
        def redraw(self):
            self.numbers.delete("all")
            index = self.text.index("@0,0")
            while True:
                info = self.text.dlineinfo(index)
                if info is None:
                    break
                self.numbers.create_text(42, info[1], anchor="ne",
                    text=index.split(".")[0], fill=getattr(self, "gutter_color", "#9ba5b6"),
                    font=("Consolas", 10))
                index = self.text.index(index + "+1line")

        def set(self, value):
            super().set(value)
            self.text.event_generate("<<ContentChanged>>")

    class Application(Base):
        def __init__(self, root):
            # Mismos nombres de widgets y variables que consumen los controladores.
            ttk.Frame.__init__(self, root, padding=20)
            self.root = root
            self.last_directory = str(Path.home() / "Documents")
            self.origin = tk.StringVar(value="PSeInt")
            self.destination = tk.StringVar(value="Python")
            self.dark = True
            self.status_kind = "muted"
            self.status_text = "Listo"
            self.copy_timer = None
            self.translated_input = None
            self.guide_visible = False
            self.style = ttk.Style(root)
            self.style.theme_use("clam")
            root.title("Traductor Académico | PSeInt + Python")
            root.geometry("1280x820")
            root.minsize(980, 680)
            self.pack(fill="both", expand=True)
            self.columnconfigure(0, weight=1)
            self.rowconfigure(3, weight=1)

            header = ttk.Frame(self)
            header.grid(row=0, column=0, sticky="ew", pady=(0, 18))
            ttk.Label(header, text="P / Py", style="Brand.TLabel").pack(side="left", padx=(0, 18))
            title = ttk.Frame(header)
            title.pack(side="left")
            ttk.Label(title, text="Traductor académico", style="Title.TLabel").pack(anchor="w")
            ttk.Label(title, text="Tu lógica, en otro lenguaje.", style="Muted.TLabel").pack(anchor="w")
            self.theme_button = ttk.Button(header, text="Modo claro", command=self.toggle_theme)
            self.theme_button.pack(side="right")
            ttk.Button(header, text="Guía visual", command=self.toggle_guide).pack(side="right", padx=8)
            ttk.Button(header, text="Compatibilidad", command=self.help).pack(side="right")

            templates = ttk.Frame(self)
            templates.grid(row=1, column=0, sticky="ew", pady=(0, 12))
            ttk.Label(templates, text="EXPLORAR", style="Muted.TLabel").pack(side="left", padx=(0, 16))
            for label in TEMPLATES:
                ttk.Button(templates, text=label, style="Pill.TButton",
                    command=lambda name=label: self.load_template(name)).pack(side="left", padx=(0, 6))
            ttk.Button(templates, text="Arreglos · no admitido", state="disabled",
                       style="Pill.TButton").pack(side="left")

            selectors = ttk.Frame(self)
            selectors.grid(row=2, column=0, sticky="ew", pady=(0, 12))
            ttk.Label(selectors, text="Origen").pack(side="left", padx=(0, 8))
            source_box = ttk.Combobox(selectors, textvariable=self.origin,
                values=("PSeInt", "Python"), state="readonly", width=10)
            source_box.pack(side="left")
            ttk.Label(selectors, text="  →  Destino  ").pack(side="left")
            target_box = ttk.Combobox(selectors, textvariable=self.destination,
                values=("Python", "PSeInt"), state="readonly", width=10)
            target_box.pack(side="left")
            source_box.bind("<<ComboboxSelected>>", lambda e: self.change_direction(True))
            target_box.bind("<<ComboboxSelected>>", lambda e: self.change_direction(False))
            ttk.Button(selectors, text="Traducir  ·  Ctrl+Enter", style="Accent.TButton",
                       command=self.do_translate).pack(side="right")

            self.panes = ttk.Panedwindow(self, orient="horizontal")
            self.panes.grid(row=3, column=0, sticky="nsew")
            left, right = ttk.Frame(self.panes), ttk.Frame(self.panes)
            self.panes.add(left, weight=1)
            self.panes.add(right, weight=1)
            left_header, right_header = ttk.Frame(left), ttk.Frame(right)
            left_header.pack(fill="x", pady=(4, 10))
            right_header.pack(fill="x", pady=(4, 10))
            self.source_title = ttk.Label(left_header, text="PSeInt  /  entrada.psc", style="Section.TLabel")
            self.source_title.pack(side="left")
            self.output_title = ttk.Label(right_header, text="Python  /  salida.py", style="Section.TLabel")
            self.output_title.pack(side="left")
            ttk.Label(right_header, text="SOLO LECTURA", style="Muted.TLabel").pack(side="right")
            snippets = ttk.Frame(left)
            snippets.pack(fill="x", pady=(0, 8))
            self.snippet_buttons = []
            for name in SNIPPETS:
                button = ttk.Button(snippets, text=name, style="Snippet.TButton",
                                    command=lambda key=name: self.insert_snippet(key))
                button.pack(side="left", padx=(0, 3))
                self.snippet_buttons.append(button)
            ttk.Button(snippets, text="Según ×", style="Snippet.TButton", state="disabled").pack(side="left")
            tools = ttk.Frame(right)
            tools.pack(fill="x", pady=(0, 8))
            self.copy_button = ttk.Button(tools, text="Copiar Python", command=self.copy)
            self.copy_button.pack(side="left")
            self.save_button = ttk.Button(tools, text="Descargar .py", command=self.save)
            self.save_button.pack(side="left", padx=6)
            self.source = ModernEditor(left, DARK["editor"])
            self.output = ModernEditor(right, DARK["editor"], readonly=True)
            self.source.pack(fill="both", expand=True, padx=(0, 6))
            self.output.pack(fill="both", expand=True, padx=(6, 0))

            bottom = ttk.Frame(self)
            bottom.grid(row=4, column=0, sticky="ew", pady=(12, 10))
            self.badge = ttk.Label(bottom, text="● Listo", style="Status.TLabel")
            self.badge.pack(side="left")
            self.position = ttk.Label(bottom, text="Lín 1, Col 1", style="Muted.TLabel")
            self.position.pack(side="left", padx=20)
            ttk.Button(bottom, text="Limpiar paneles", command=self.clear).pack(side="right")
            ttk.Button(bottom, text="Cargar archivo", command=self.load).pack(side="right", padx=8)
            ttk.Button(bottom, text="Ejemplo de suma", command=self.example).pack(side="right")

            self.guide = ttk.Frame(self, padding=12, style="Card.TFrame")
            ttk.Label(self.guide, text="GUÍA VISUAL · selecciona una estructura para insertarla",
                      style="Card.TLabel").pack(anchor="w", pady=(0, 8))
            cards = ttk.Frame(self.guide, style="Card.TFrame")
            cards.pack(fill="x")
            for key, text in (("Escribir", "Escribir → print()"), ("Leer", "Leer → input()"),
                              ("Si", "Si → if / else"), ("Mientras", "Mientras → while"),
                              ("Para", "Para → for / range")):
                ttk.Button(cards, text=text, command=lambda k=key: self.insert_snippet(k)).pack(side="left", padx=(0, 6))
            ttk.Label(self.guide, text="Declara las variables antes de usarlas. Para incluye el límite final; range lo excluye.",
                      style="Card.TLabel").pack(anchor="w", pady=(8, 0))

            self.messages = tk.Text(self, height=3, wrap="word", relief="flat",
                font=("Segoe UI", 10), padx=12, pady=10, state="disabled")
            self.messages.grid(row=6, column=0, sticky="ew")
            self.message("Listo. Elige una plantilla o escribe tu código y pulsa Traducir. Arreglos y Según no están admitidos.")
            ttk.Label(self, text="LOCAL · SIN EJECUCIÓN DE CÓDIGO                  Arrastra el divisor para ajustar los paneles.",
                      style="Muted.TLabel").grid(row=7, column=0, sticky="w", pady=(9, 0))
            self.source.text.bind("<<Modified>>", self.on_edit, add=True)
            self.source.text.bind("<<ContentChanged>>", self.on_edit, add=True)
            self.source.text.bind("<KeyRelease>", self.on_edit, add=True)
            for event in ("<<Paste>>", "<<Cut>>", "<<Undo>>", "<<Redo>>"):
                self.source.text.bind(event, lambda e: self.after_idle(self.on_edit), add=True)
            self.source.text.bind("<ButtonRelease-1>", self.update_position, add=True)
            root.bind("<Control-Return>", lambda e: self.do_translate())
            root.protocol("WM_DELETE_WINDOW", self.close)
            self.apply_theme()
            self.after_idle(lambda: self.panes.sashpos(0, self.panes.winfo_width() // 2))

        def status(self, text, kind="muted"):
            self.status_text, self.status_kind = text, kind
            self.badge.configure(text="● " + text)
            self.style.configure("Status.TLabel", foreground=self.palette[kind])

        def on_edit(self, event=None):
            if (self.source.get(), self.origin.get(), self.destination.get()) != self.translated_input:
                self.status("Cambios pendientes" if self.source.get().strip() else "Listo")
            self.update_position()

        def update_position(self, event=None):
            line, col = self.source.text.index("insert").split(".")
            self.position.configure(text=f"Lín {line}, Col {int(col) + 1}")

        def do_translate(self):
            # El controlador original conserva llamada, errores y advertencias.
            super().do_translate()
            self.translated_input = (self.source.get(), self.origin.get(), self.destination.get())
            self.status("Sincronizado · revisar advertencias" if self.output.get() else "Error de traducción",
                        "warning" if self.output.get() else "error")

        def change_direction(self, from_source):
            super().change_direction(from_source)
            self.refresh_direction()
            self.status("Dirección actualizada")

        def refresh_direction(self):
            source, target = self.origin.get(), self.destination.get()
            self.source_title.configure(text=source + "  /  entrada" + (".psc" if source == "PSeInt" else ".py"))
            self.output_title.configure(text=target + "  /  salida" + (".py" if target == "Python" else ".psc"))
            if self.copy_timer:
                self.after_cancel(self.copy_timer)
                self.copy_timer = None
            self.copy_button.configure(text="Copiar " + target)
            self.save_button.configure(text="Descargar " + (".py" if target == "Python" else ".psc"))
            for button in self.snippet_buttons:
                button.configure(state="normal" if source == "PSeInt" else "disabled")

        def load_template(self, name):
            if not self.can_replace():
                return
            self.origin.set("PSeInt")
            self.change_direction(True)
            self.source.set(TEMPLATES[name])
            # Procesar los eventos de edición antes de fijar el estado final.
            self.source.text.edit_modified(True)
            self.root.update_idletasks()
            self.do_translate()

        def insert_snippet(self, name):
            if self.origin.get() != "PSeInt":
                self.message("Los comandos de esta guía se insertan con PSeInt como origen.")
                return
            text = self.source.text
            # Insertar una estructura en su propia línea, respetando la sangría.
            index = text.index("insert")
            before = text.get(index + " linestart", index)
            indent = before[:len(before) - len(before.lstrip())]
            prefix = "\n" + indent if before.strip() else ""
            suffix = "\n" + indent if text.get(index, index + " lineend").strip() else ""
            snippet = prefix + SNIPPETS[name].replace("\n", "\n" + indent) + suffix
            text.edit_separator()
            text.insert("insert", snippet)
            text.edit_separator()
            text.see("insert")
            text.focus_set()
            self.on_edit()

        def copy(self):
            super().copy()
            if self.output.get():
                self.copy_button.configure(text="¡Copiado!")
                if self.copy_timer:
                    self.after_cancel(self.copy_timer)
                self.copy_timer = self.after(1600, self.restore_copy)

        def restore_copy(self):
            self.copy_timer = None
            self.copy_button.configure(text="Copiar " + self.destination.get())

        def clear(self):
            super().clear()
            if not self.source.get():
                self.status("Listo")
                self.refresh_direction()

        def toggle_guide(self):
            self.guide_visible = not self.guide_visible
            if self.guide_visible:
                self.guide.grid(row=5, column=0, sticky="ew", pady=(0, 10))
            else:
                self.guide.grid_remove()

        def toggle_theme(self):
            self.dark = not self.dark
            self.apply_theme()

        def apply_theme(self):
            p = self.palette = DARK if self.dark else LIGHT
            s = self.style
            self.root.configure(background=p["bg"])
            s.configure(".", font=("Segoe UI", 10), background=p["bg"], foreground=p["fg"])
            s.configure("TFrame", background=p["bg"])
            s.configure("TLabel", background=p["bg"], foreground=p["fg"])
            s.configure("Title.TLabel", font=("Segoe UI", 20, "bold"))
            s.configure("Brand.TLabel", foreground=p["accent"], font=("Consolas", 24, "bold"))
            s.configure("Muted.TLabel", foreground=p["muted"], font=("Segoe UI", 9))
            s.configure("Section.TLabel", font=("Segoe UI", 11, "bold"))
            s.configure("Card.TFrame", background=p["panel"])
            s.configure("Card.TLabel", background=p["panel"], foreground=p["muted"])
            s.configure("TButton", background=p["panel"], foreground=p["fg"],
                        bordercolor=p["border"], padding=(10, 7), relief="flat")
            s.map("TButton", background=[("active", p["select"])],
                  foreground=[("disabled", p["muted"])])
            s.configure("Pill.TButton", padding=(11, 6))
            s.configure("Snippet.TButton", padding=(7, 7), width=0, font=("Segoe UI", 9))
            s.configure("Accent.TButton", background=p["accent"], foreground="#ffffff")
            s.map("Accent.TButton", background=[("active", "#7664de")])
            s.configure("TCombobox", fieldbackground=p["panel"], background=p["panel"],
                        foreground=p["fg"], arrowcolor=p["muted"], padding=5)
            s.map("TCombobox", fieldbackground=[("readonly", p["panel"])],
                  foreground=[("readonly", p["fg"])], selectbackground=[("readonly", p["panel"])],
                  selectforeground=[("readonly", p["fg"])])
            self.root.option_add("*TCombobox*Listbox.background", p["panel"])
            self.root.option_add("*TCombobox*Listbox.foreground", p["fg"])
            s.configure("TPanedwindow", background=p["border"])
            s.configure("Sash", sashthickness=6)
            s.configure("TScrollbar", background=p["border"], troughcolor=p["editor"],
                        arrowcolor=p["muted"], bordercolor=p["editor"])
            for editor in (self.source, self.output):
                editor.text.configure(height=1, width=1, bg=p["editor"], fg=p["fg"], insertbackground=p["accent"],
                    selectbackground=p["select"], selectforeground=p["fg"], spacing1=3, spacing3=3)
                editor.numbers.configure(bg=p["editor"], width=52)
                editor.gutter_color = p["muted"]
                editor.redraw()
            self.messages.configure(bg=p["panel"], fg=p["muted"])
            self.theme_button.configure(text="Modo claro" if self.dark else "Modo oscuro")
            self.status(self.status_text, self.status_kind)

    return Application
