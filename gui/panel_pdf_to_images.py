import tkinter as tk
from shared_lib.history import History
from shared_lib.gui.widget_select_file import WidgetSelectFile
from shared_lib.gui.widget_preview_file import WidgetPreview
from gui.widget_run import WidgetRun
from shared_lib.img_process import pdf_to_png


class PanelPdfToImages(tk.Frame):
    """Convert pdf file to images (one per page)"""
    def __init__(self, parent, name=None, **kwargs):
        """Initialize"""
        super().__init__(parent, **kwargs)
        self.name = name

        self.pack(fill=tk.BOTH, expand=True)
        self.rowconfigure(1, weight=1)

        # Source file panel
        self.panel_src_file = WidgetSelectFile(self, False,
                                               History("history/history_pdftoimg_src.json", 20),
                                               init_from_history=False)
        self.panel_src_file.grid(row=0, column=0, padx=5, pady=5, sticky="new")
        self.panel_src_file.var_path.trace_add("write", self.on_select_source)  # fires on .set() or user change

        # File preview panel
        self.panel_preview = WidgetPreview(self,
                                           bd=2,  # border width
                                           relief="solid"  # style: "flat", "raised", "sunken", "groove", "ridge", "solid"
                                           )
        self.panel_preview.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

        # Destination directory panel (stick to the bottom)
        self.panel_dst_dir = WidgetSelectFile(self, True, History("history/history_pdftoimg_dst.json", 20))
        self.panel_dst_dir.grid(row=2, column=0, padx=5, pady=5, sticky="swe")

        self.panel_run = WidgetRun(self, text=__doc__, command=self.run)
        self.panel_run.grid(row=3, column=0, padx=5, pady=5, sticky="sew")

    def run(self):
        """Convert pdf pages to png images"""
        pdf_to_png(self.panel_src_file.get_path(), self.panel_dst_dir.get_path())

    def on_select_source(self, *argv):
        """Source file is selected - update preview"""
        path = self.panel_src_file.var_path.get()
        self.panel_preview.load(path)
