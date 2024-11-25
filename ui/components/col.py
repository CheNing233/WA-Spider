from tkinter import Tk, ttk


class Col:
    def __init__(self, parent, p_row, p_col, col_configs):
        """
        初始化 Col 类，创建一个 Frame 并根据传入的 col_configs 配置各个列。

        :param parent: 父级容器（通常是 Tk 或其他 Frame）
        :param p_row: 父级row
        :param p_col: 父级col
        :param col_configs: 列配置的列表，每个配置为一个字典，包含 column, weight, minsize 等设置
        """
        self.parent = parent
        self.col_configs = col_configs

        # 创建一个 Frame
        self.frame = ttk.Frame(self.parent, padding="10")
        self.frame.grid(row=p_row, column=p_col, sticky="ew", padx=8, pady=0)

        # 配置列
        for config in self.col_configs:
            self.frame.grid_columnconfigure(
                config['column'],
                weight=config.get('weight', 1),
                minsize=config.get('minsize', 0)
            )

    def get_frame(self):
        """返回创建的 frame"""
        return self.frame
