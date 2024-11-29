from tkinter import ttk
from tkinter import Tk

from src.controllers.tusi_art_fetcher import TusiArtFetcher
from ui.components.logger import LoggerContainer


class TusiArtComponent:
    def __init__(self, root):
        self.fetcher: TusiArtFetcher | None = None
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

        # fetch_detail_btn
        self.fetch_detail_btn = ttk.Button(
            self.button_frame, text="抓取模型详情", command=self.on_fetch_detail
        )
        self.fetch_detail_btn.pack(side="left", padx=5)  # 按钮放在左侧，带一点内边距

        self.save_detail_btn = ttk.Button(
            self.button_frame, text="保存模型详情（保存到sqlite数据库）",
            command=self.on_save_detail)
        self.save_detail_btn.pack(side="left", padx=5)

        # fetch_covers_btn
        self.fetch_covers_btn = ttk.Button(
            self.button_frame, text="抓取模型相关图片", command=self.on_fetch_covers
        )
        self.fetch_covers_btn.pack(side="left", padx=5)  # 按钮放在左侧，带一点内边距

        # all_fetch_and_save_btn
        self.all_fetch_and_save_btn = ttk.Button(
            self.button_frame, text="一键抓取并入库",
            command=self.on_fetch_and_save)
        self.all_fetch_and_save_btn.pack(side="left", padx=5)

        self.info_frame = ttk.Frame(self.root)
        self.info_frame.pack(fill="x", padx=5, pady=5)

        self.info_label = ttk.Label(self.info_frame, text="准备完毕", wraplength=200)
        self.info_label.pack(side="left", fill="x", expand=True, padx=5)

        self.logger_frame = ttk.Frame(self.root)
        self.logger_frame.pack(fill="both", padx=5, pady=5)

        self.logger = LoggerContainer(self.logger_frame)
        self.logger.pack(fill="both", expand=True, padx=5)

    def on_fetch_detail(self):
        self.fetcher = None

        url = self.entry_input.get()
        print(f"开始抓取模型详情：{url}")
        self.fetcher = TusiArtFetcher(url)

        self.info_label.config(
            text=self.fetcher.fetch_model_detail()
        )

        print('抓取完成')

    def on_save_detail(self):
        if self.fetcher is None:
            self.info_label.config(text="请先抓取详情")
            return

        self.info_label.config(
            text=self.fetcher.save_model_detail()
        )

        print('模型详情已入库')

    def on_fetch_covers(self):
        if self.fetcher is None:
            self.info_label.config(text="请先抓取详情")
            return

        self.info_label.config(
            text=self.fetcher.save_model_covers()
        )

        print('模型封面图片抓取完成')

    def on_fetch_and_save(self):
        self.on_fetch_detail()
        self.on_save_detail()
        self.on_fetch_covers()
