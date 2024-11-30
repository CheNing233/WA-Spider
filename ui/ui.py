# ui.py
from ui.components.ScrollContainer import ScrollableFrame
from ui.pages import TusiArtComponent
from tkinter import ttk


class WaSpiderUI:
    _instance = None  # 单例实例

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(WaSpiderUI, cls).__new__(cls)
        return cls._instance

    def __init__(self, root):
        self.civitai_frame = None
        self.civitai_scroll = None
        self.tusi_art_frame = None
        self.tusi_art_scroll = None
        self.tusi_art_component = None

        # 确保 __init__ 只在实例化时执行一次
        if not hasattr(self, 'initialized'):
            self.root = root
            self.root.title("WA-Spider")
            self.root.geometry("800x600")
            self.create_widgets()
            self.initialized = True  # 标记已经初始化

    def create_widgets(self):
        self.root.grid_columnconfigure(0, weight=1)

        # 创建 Notebook（选项卡控件）
        notebook = ttk.Notebook(self.root)

        # 创建 TusiArt 页面
        # 创建 TusiArt 页面容器
        self.tusi_art_frame = ttk.Frame(notebook)
        # 添加 TusiArt 页面容器到 tab
        notebook.add(self.tusi_art_frame, text="TusiArt")
        # 创建滚动容器
        self.tusi_art_scroll = ScrollableFrame(self.tusi_art_frame)
        # 将组件挂载到滚动容器
        self.tusi_art_component \
            = TusiArtComponent(self.tusi_art_scroll.get_frame())

        # 创建 Civitai 页面
        # self.civitai_frame = ttk.Frame(notebook)
        # notebook.add(self.civitai_frame, text="Civitai")
        # self.civitai_scroll = ScrollableFrame(self.civitai_frame)

        # 将 Notebook 放置在窗口中
        notebook.pack(expand=True, fill="both")
