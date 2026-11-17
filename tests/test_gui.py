"""Integración real con Tk; diálogos de archivos simulados para no bloquear pruebas."""
import tempfile
import tkinter as tk
import unittest
from pathlib import Path
from unittest.mock import patch
from gui import Application, PSE_EXAMPLE, PY_EXAMPLE


class GuiTests(unittest.TestCase):
    def setUp(self):
        try:
            self.root = tk.Tk()
        except tk.TclError as exc:
            self.skipTest("Tk no disponible: " + str(exc))
        self.root.withdraw()
        self.app = Application(self.root)
        self.root.update()

    def tearDown(self):
        if hasattr(self, 'root'):
            self.root.destroy()

    def test_window_and_translation_both_ways(self):
        self.app.source.set(PSE_EXAMPLE)
        self.app.do_translate()
        self.assertIn('float(input())', self.app.output.get())
        self.app.origin.set('Python')
        self.app.change_direction(True)
        self.assertEqual(self.app.destination.get(), 'PSeInt')
        self.app.source.set(PY_EXAMPLE)
        self.app.do_translate()
        self.assertIn('Leer a', self.app.output.get())

    def test_load_save_copy(self):
        with tempfile.TemporaryDirectory() as directory:
            source, output = Path(directory)/'entrada.psc', Path(directory)/'salida.py'
            source.write_text(PSE_EXAMPLE, encoding='utf-8')
            with patch('gui.filedialog.askopenfilename', return_value=str(source)):
                self.app.load()
            self.app.do_translate()
            with patch('gui.filedialog.asksaveasfilename', return_value=str(output)) as dialog:
                self.app.save()
                self.assertTrue(dialog.call_args.kwargs['confirmoverwrite'])
            self.assertEqual(output.read_text(encoding='utf-8'), self.app.output.get())
            self.app.copy()
            self.assertEqual(self.root.clipboard_get(), self.app.output.get())

    def test_error_clears_old_output(self):
        self.app.source.set(PSE_EXAMPLE)
        self.app.do_translate()
        self.app.source.set('Algoritmo Incompleto')
        self.app.do_translate()
        self.assertEqual(self.app.output.get(), '')
        self.assertIn('Sintaxis', self.app.messages.get('1.0', 'end'))

    def test_example_help_clear(self):
        self.app.example()
        self.assertEqual(self.app.source.get(), PSE_EXAMPLE)
        self.app.help()
        self.root.update()
        with patch('gui.messagebox.askyesno', return_value=True):
            self.app.clear()
        self.assertEqual(self.app.source.get(), '')

    def test_read_write_errors(self):
        with patch('gui.filedialog.askopenfilename', return_value='missing.psc'):
            self.app.load()
        self.assertIn('Error al abrir', self.app.messages.get('1.0', 'end'))
        self.app.source.set(PSE_EXAMPLE)
        self.app.do_translate()
        with patch('gui.filedialog.asksaveasfilename', return_value='missing/folder/out.py'):
            self.app.save()
        self.assertIn('Error al guardar', self.app.messages.get('1.0', 'end'))
