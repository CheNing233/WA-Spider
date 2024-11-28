from tkinter import ttk
from tkinter import Tk


class TusiArtComponent:
    def __init__(self, root):
        self.root = root

        # 创建标题标签并使用 pack 布局
        self.title_label = ttk.Label(self.root, text="TusiArt模型信息抓取", font=("Arial", 14, "bold"))
        self.title_label.pack(fill="x", padx=5, pady=10)  # 水平方向填充，带外边距

        # 创建输入框容器 Frame
        self.input_frame = ttk.Frame(self.root)
        self.input_frame.pack(fill="x", padx=5, pady=5)

        # 在输入框容器中放置 Label 和 Entry
        self.entry_label = ttk.Label(self.input_frame, text="输入吐司模型页链接：")
        self.entry_label.pack(side="left", padx=5)  # 左对齐

        self.entry_input = ttk.Entry(self.input_frame)
        self.entry_input.pack(side="left", fill="x", expand=True, padx=5)  # 水平方向扩展，左对齐

        # 创建按钮容器 Frame
        self.button_frame = ttk.Frame(self.root)
        self.button_frame.pack(fill="x", padx=5, pady=5)

        # 在按钮容器中放置提交按钮
        self.submit_button = ttk.Button(self.button_frame, text="提交", command=self.on_submit)
        self.submit_button.pack(side="left", padx=5)  # 按钮放在左侧，带一点内边距

    def on_submit(self):
        input_text = self.entry_input.get()
        print(f"输入框中的内容：{input_text}")
