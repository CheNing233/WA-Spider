import requests
from requests import Session

from config import GlobalConfig
from share import wa_spider_share


class TusiArtModel:

    @staticmethod
    def get_model_detail(model_id: str):
        url = GlobalConfig.tusi_art_get_model_detail_url()
        params = {'modelId': model_id}
        s: Session = wa_spider_share.wa_requests_session

        try:
            # 发起 GET 请求
            response = s.get(url, params=params)

            # 如果请求成功，返回响应内容
            if response.status_code == 200:
                return response.json()  # 返回 JSON 格式的数据
            else:
                print(f"请求失败，状态码: {response.status_code}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"请求发生错误: {e}")
            return None
