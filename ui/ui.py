from ui.pages import TusiArtComponent

class WaSpiderUI:
    _instance = None  # 单例实例

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(WaSpiderUI, cls).__new__(cls)
        return cls._instance

    def __init__(self, root):
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

        self.tusi_art_component = TusiArtComponent(self.root)
