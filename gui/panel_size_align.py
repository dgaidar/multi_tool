'''
Convert pdf file to images (one per page)
'''
import tkinter as tk
from shared_lib.img_process import resize_and_crop
from shared_lib.history import History
from shared_lib.gui.widget_select_file import WidgetSelectFile
from gui.widget_run import WidgetRun
import os
from gui.widget_image_set import WidgetImageSet
from shared_lib.gui.widget_preview_folder import WidgetPreviewFolder

class PanelSizeAlign(tk.Frame):
    def __init__(self, parent, name=None, **kwargs):
        super().__init__(parent, **kwargs)
        self.name = name

        self.pack(fill=tk.BOTH, expand=True)
        self.rowconfigure(1, weight=1)

        # Source folder panel
        self.panel_src_folder = WidgetSelectFile(self, True,
                                                 History("history/size_align_src.json", 20),
                                                 init_from_history=False)
        self.panel_src_folder.grid(row=0, column=0, padx=5, pady=5, sticky="new")

        # File preview scrollable panel
        self.panel_preview = WidgetPreviewFolder(self)
        self.panel_src_folder.var_path.trace_add("write", self.load_folder)  # fires on .set() or user change
        self.panel_preview.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

        # Destination directory panel (stick to the bottom)
        self.panel_dst_folder = WidgetSelectFile(self,
                                              True,
                                              History("history/size_align_dst.json", 20))
        #self.panel_dst_folder.pack(anchor=tk.S, pady=5, padx=5, fill=tk.X)
        self.panel_dst_folder.grid(row=2, column=0, padx=5, pady=5, sticky="swe")

        self.settings = WidgetImageSet(self)
        self.settings.grid(row=3, column=0, padx=5, pady=5, sticky="sew")

        self.panel_run = WidgetRun(self, text=__doc__, command=self.run)
        self.panel_run.grid(row=4, column=0, padx=5, pady=5, sticky="sew")

    def load_folder(self, *args):
        path = self.panel_src_folder.var_path.get()
        self.panel_preview.load_folder(path)

    @staticmethod
    def check_folder(path):
        if not path:
            raise RuntimeError("Path not provided")
        if not os.path.exists(path):
            raise RuntimeError(F"Path '{path}' doesn't exist")
        if not os.path.isdir(path):
            raise RuntimeError(F"Path '{path}' not a folder")

    def run(self):
        new_size = self.settings.get_size()
        src = self.panel_src_folder.var_path.get()
        dst = self.panel_dst_folder.var_path.get()
        self.check_folder(src)
        self.check_folder(dst)
        for fname in os.listdir(src):
            fpath = os.path.join(src, fname)
            if fpath in self.panel_preview.path2image:
                img = self.panel_preview.path2image[fpath]
                resized = resize_and_crop(img, new_size)
                resized.save(os.path.join(dst, fname))



# Main Application
if __name__ == "__main__":
    root = tk.Tk()
    root.title("File Control Example")
    root.geometry("600x500")

    control = PanelSizeAlign(root)

    root.mainloop()
