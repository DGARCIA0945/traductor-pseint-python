import tkinter as tk
import unittest
from unittest.mock import patch
from gui import Application
from modern_ui import TEMPLATES

class ModernUiTests(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.app = Application(self.root)
        self.root.update()
    def tearDown(self):
        if self.app.copy_timer:
            self.app.after_cancel(self.app.copy_timer)
        self.root.destroy()
    def test_templates_and_status_after_events(self):
        with patch("gui.messagebox.askyesno", return_value=True):
            for name in TEMPLATES:
                self.app.load_template(name)
                self.root.update()
                self.assertTrue(self.app.output.get(), name)
                self.assertIn("Sincronizado", self.app.status_text)
    def test_snippet_cursor_undo(self):
        self.app.source.set("Algoritmo Prueba\n    \nFinAlgoritmo")
        self.app.source.text.mark_set("insert", "2.4")
        self.app.insert_snippet("Escribir")
        self.assertIn('    Escribir "Hola"\nFinAlgoritmo', self.app.source.get())
        self.app.source.text.edit_undo()
        self.assertNotIn('Escribir', self.app.source.get())
    def test_theme_guide_and_direction(self):
        self.app.toggle_theme()
        self.assertEqual(self.app.source.text.cget("background"), "#ffffff")
        self.app.toggle_guide()
        self.assertEqual(self.app.guide.winfo_manager(), "grid")
        self.app.toggle_guide()
        self.assertFalse(self.app.guide.winfo_manager())
        self.app.origin.set("Python")
        self.app.change_direction(True)
        self.assertEqual(str(self.app.snippet_buttons[0].cget("state")), "disabled")
        self.assertEqual(self.app.save_button.cget("text"), "Descargar .psc")
    def test_errors_and_copy_feedback(self):
        self.app.load_template("Hola mundo")
        self.app.copy()
        self.assertEqual(self.app.copy_button.cget("text"), "¡Copiado!")
        self.assertEqual(self.root.clipboard_get(), self.app.output.get())
        self.app.source.set("Algoritmo Incompleto")
        self.app.do_translate()
        self.root.update()
        self.assertEqual(self.app.status_kind, "error")
        self.assertFalse(self.app.output.get())
    def test_repeated_edits_mark_pending(self):
        self.app.load_template("Hola mundo")
        self.root.update()
        self.app.source.text.insert("end", " ")
        self.app.on_edit()
        self.assertEqual(self.app.status_text, "Cambios pendientes")
        self.app.do_translate()
        self.app.source.text.insert("end", " ")
        self.app.on_edit()
        self.assertEqual(self.app.status_text, "Cambios pendientes")
