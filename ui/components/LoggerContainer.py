import io
import tkinter as tk
import sys


class PrintLogger(io.StringIO):
    def __init__(self, text_widget):
        super().__init__()
        self.text_widget = text_widget

    def write(self, message):
        self.text_widget.configure(state=tk.NORMAL)
        self.text_widget.insert("end", message)
        self.text_widget.see("end")
        self.text_widget.configure(state=tk.DISABLED)

    def flush(self):
        pass

    def getvalue(self):
        return self.getvalue()


class LoggerContainer(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.text = tk.Text(self, wrap="word")
        self.scrollbar = tk.Scrollbar(self, command=self.text.yview)

        self.text.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.text.config(yscrollcommand=self.scrollbar.set)

        self.pack(fill="both", expand=True)

        self.print_logger = PrintLogger(self.text)
        sys.stdout = self.print_logger
