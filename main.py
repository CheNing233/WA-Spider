# main.py

from tkinter import Tk

import requests

from ui.ui import WaSpiderUI
from share import wa_spider_share


def main():
    # 初始化 tkinter 主窗口
    root = Tk()
    wa_spider_share.wa_spider_ui_root = root

    # 初始化requests.Session
    wa_spider_share.wa_requests_session = requests.Session()

    # 创建 GUI 实例
    app = WaSpiderUI(root)
    wa_spider_share.wa_spider_ui = app

    # 启动主循环
    root.mainloop()


if __name__ == "__main__":
    main()
