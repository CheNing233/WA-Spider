from unittest import TestCase

import tkinter as tk
from tkinter import ttk

from ui.components.ScrollContainer import ScrollableFrame


class TestScrollableFrame(TestCase):
    def test_get_frame(self):
        root = tk.Tk()
        root.geometry("400x300")

        # 创建 ScrollableFrame 实例
        scrollable_frame = ScrollableFrame(root)
        scrollable_frame.pack(fill="both", expand=True)

        # 向 scrollable_frame 的 Frame 中添加内容
        content_frame = scrollable_frame.get_frame()
        for i in range(50):
            ttk.Label(content_frame, text=f"Label {i + 1}").pack(padx=10, pady=5)

        root.mainloop()
