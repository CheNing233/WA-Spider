from tkinter import ttk
from ui.components import Col


class TusiArtComponent:
    def __init__(self, root):
        self.root = root

        # 标题
        self.col1 = Col(root, 0, 0, [
            {'column': 0, 'weight': 1}
        ]).get_frame()

        self.title_label = ttk.Label(self.col1, text="TusiArt模型信息抓取", font=("Arial", 14, "bold"))
        self.title_label.grid(row=0, column=0, sticky="w", padx=5, pady=0)

        # 输入框
        self.col2 = Col(root, 1, 0, [
            {'column': 0, 'weight': 0},
            {'column': 1, 'weight': 1}
        ]).get_frame()

        self.entry_label = ttk.Label(self.col2, text="输入吐司模型页链接：")
        self.entry_label.grid(row=1, column=0, padx=5, pady=0)

        self.entry_input = ttk.Entry(self.col2)
        self.entry_input.grid(row=1, column=1, sticky="ew", padx=5, pady=0)  # 输入框宽度随窗口变化

        # 创建按钮
        self.col3 = Col(root, 2, 0, [
            {'column': 0, 'weight': 0}
        ]).get_frame()

        self.submit_button = ttk.Button(self.col3, text="提交", command=self.on_submit)
        self.submit_button.grid(row=2, column=0, sticky="w", padx=5, pady=0)  # 按钮宽度随窗口变化

    def on_submit(self):
        input_text = self.entry_input.get()
        print(f"输入框中的内容：{input_text}")
