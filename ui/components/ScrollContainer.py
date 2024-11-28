import tkinter as tk
from tkinter import ttk


class ScrollableFrame(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # 创建 Canvas 作为容器
        self.canvas = tk.Canvas(self, highlightthickness=0, bd=0)

        # 创建垂直滚动条
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)

        # 将滚动条与 Canvas 绑定
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # 创建 Frame 放置在 Canvas 中，支持 pack 布局
        self.scrollable_frame = ttk.Frame(self.canvas)

        # 在 Canvas 中创建窗口（只创建一次）
        self.window_item = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # 更新 scrollregion 以适应子元素大小
        self.scrollable_frame.bind("<Configure>", self._update_scroll_region)
        self.bind("<Configure>", self._update_frame_width)  # 调整 frame 宽度

        # 调用一次来初始化
        self._update_scroll_region()

        # 布局 Canvas 和滚动条
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # 允许 ScrollableFrame 自动扩展
        self.pack(fill="both", expand=True)

        # 绑定鼠标滚轮事件
        self.canvas.bind_all("<MouseWheel>", self._on_mouse_wheel)

        self.after(250, self._update_scroll_region)
        self.after(250, self._update_frame_width)

    def _update_scroll_region(self, event=None):
        """
        当 Frame 大小改变时，更新 Canvas 的 scrollregion。
        使 Canvas 能够滚动超出可视区域的部分。
        """
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _update_frame_width(self, event=None):
        """
        当窗口大小调整时，更新 scrollable_frame 的宽度，使其与 Canvas 宽度匹配。
        """
        canvas_width = self.canvas.winfo_width()
        # 更新已有窗口项的宽度，而不是重新创建
        self.canvas.itemconfig(self.window_item, width=canvas_width)

    def _on_mouse_wheel(self, event):
        """鼠标滚轮滚动事件处理"""
        # Windows 和 MacOS 不同方向处理
        if event.delta:
            self.canvas.yview_scroll(-1 * (event.delta // 120), "units")

    def get_frame(self):
        """返回 Frame 用于放置内容"""
        return self.scrollable_frame