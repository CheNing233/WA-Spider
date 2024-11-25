# share.py
import requests
from requests import Request, Session


class WaSpiderShare:
    """
    共享类
    """

    def __init__(self):
        self._wa_spider_ui_root = None
        self._wa_spider_ui = None
        self._wa_requests_session = None

    @property
    def wa_spider_ui_root(self):
        return self._wa_spider_ui_root

    @wa_spider_ui_root.setter
    def wa_spider_ui_root(self, root):
        self._wa_spider_ui_root = root

    @property
    def wa_spider_ui(self):
        return self._wa_spider_ui

    @wa_spider_ui.setter
    def wa_spider_ui(self, app_ui):
        self._wa_spider_ui = app_ui

    @property
    def wa_requests_session(self) -> requests.Session:
        if not self._wa_requests_session:
            self._wa_requests_session = Session()
        return self._wa_requests_session

    @wa_requests_session.setter
    def wa_requests_session(self, session):
        self._wa_requests_session = session


# 共享实例
wa_spider_share = WaSpiderShare()
