import tkinter as tk


class WidgetRun(tk.Frame):
    """Contains just RUN button and explanation what this RUN does"""
    def __init__(self, parent, text, command, **kwargs):
        """Initialize"""
        super().__init__(parent,
                         bd=2,  # border width
                         relief="solid",  # style: "flat", "raised", "sunken", "groove", "ridge", "solid"
                         **kwargs)
        self.parent = parent

        # Source File Selection
        self.explanation = tk.Label(self, text=text)
        self.explanation.grid(row=0, column=0, sticky="w", pady=(10, 0), padx=10)

        self.run_button = tk.Button(self, text="Run", command=command)
        self.run_button.grid(row=0, column=2, sticky="e", padx=(10, 5))

        self.grid_columnconfigure(1, weight=1)
