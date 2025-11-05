import tkinter as tk
from tkinter import ttk
from shared_lib.gui.int_entry import IntEntry


class WidgetImageSet(tk.Frame):
    """A frame allowing to insert width and height of modified images and set their extension"""
    def __init__(self, master, **kwargs):
        super().__init__(master,
                         bd=2,
                         relief="solid",
                         **kwargs)

        # Labels
        self.label_w = ttk.Label(self, text="Width")
        self.label_h = ttk.Label(self, text="Height")
        self.label_format = ttk.Label(self, text="File format")

        # Integer Entry widgets
        self.entry_w = IntEntry(self, width=5)
        self.entry_h = IntEntry(self, width=5)

        # Combobox
        self.combo = ttk.Combobox(self, values=["jpg", "png", "tiff"], width=6)
        self.combo.current(0)

        # Layout using grid
        self.columnconfigure(1, weight=1)  # make combo stretch if needed

        self.label_w.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_w.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.label_h.grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.entry_h.grid(row=0, column=3, padx=5, pady=5, sticky="w")
        self.label_format.grid(row=0, column=4, padx=5, pady=5, sticky="w")
        self.combo.grid(row=0, column=5, padx=5, pady=5, sticky="w")

    def get_size(self):
        """Return a tuple (int1, int2, combo_value)."""
        return self.entry_w.get_int(), self.entry_h.get_int()

    def set_values(self, val1, val2, combo_value=None):
        """Set widget values."""
        self.entry_w.set_int(val1)
        self.entry_h.set_int(val2)
        if combo_value is not None:
            self.combo.set(combo_value)
