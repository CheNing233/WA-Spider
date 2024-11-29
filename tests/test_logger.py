from unittest import TestCase
import tkinter as tk

from ui.components.logger import LoggerContainer


class TestScrollableText(TestCase):
    def test_logger(self):
        # 创建 tkinter 窗口
        root = tk.Tk()
        root.title("Print to Tkinter Scrollable Text")

        # 创建 ScrollableText 实例并传入父容器
        scrollable_text = LoggerContainer(root)

        # 进行测试输出
        print("This is a test message.")
        print("This is another message.")
        # 添加更多 print 语句来测试滚动

        root.mainloop()
