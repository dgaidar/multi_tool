import tkinter as tk
from tkinter import ttk
from shared_lib.settings import Settings
from gui.panel_pdf_to_images import PanelPdfToImages
from gui.panel_size_align import PanelSizeAlign
from gui.panel_crop import PanelCrop


class MultiTool:
    """Archives a set of usefull tools in the single place"""
    def __init__(self):
        """Initialize"""
        self.root = tk.Tk()
        self.root.title("MultiTool")
        # Restore window size
        sizes = Settings().get(field="MainWindow_Size", default_val="600x600")
        self.root.geometry(sizes)
        # Get events
        self.root.bind("<Configure>", self.save_cur_size)
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        # Create Tabs
        tab_control = ttk.Notebook(self.root)
        tab_control.pack(expand=1, fill="both")

        tab1 = PanelSizeAlign(tab_control)
        tab_control.add(tab1, text=tab1.name)

        tab2 = PanelPdfToImages(tab_control)
        tab_control.add(tab2, text=tab2.name)

        tab3 = PanelCrop(tab_control)
        tab_control.add(tab3, text=tab3.name)

        # Restore tab selection
        tab_index = Settings().get("Tab_SelectedIndex", default_val=0)
        tab_control.select(tab_index)
        tab_control.bind("<<NotebookTabChanged>>", self.save_tag_selected)

    def on_close(self, *args):
        """Avoid size saving during destroy on exit"""
        self.root.unbind("<Configure>")
        self.root.destroy()

    def save_cur_size(self, event):
        size_str = f"{event.width}x{event.height}"
        Settings().set("MainWindow_Size", size_str)

    def save_tag_selected(self, event):
        notebook = event.widget  # the Notebook widget
        tab_id = notebook.select()  # ID of the selected tab
        tab_index = notebook.index(tab_id)
        Settings().set("Tab_SelectedIndex", tab_index)

if __name__ == "__main__":
    control = MultiTool()
    control.root.mainloop()