import json
import os

import requests
from requests import Session

from config import GlobalConfig
from share import wa_spider_share
from src.utils.helper import get_root_dir


class TusiArtModelDetail:
    def __init__(self, detail_data: dict):
        self.project_dir = None
        self.raw_data = detail_data

    def get_id(self):
        return self.raw_data['model']['id']

    def get_name(self):
        return self.raw_data['model']['name']

    def get_description(self):
        return self.raw_data['model']['description']

    def get_type(self):
        return self.raw_data['model']['type']

    def get_base_model(self):
        return self.raw_data['model']['baseModel']

    def get_trigger_words(self):
        return self.raw_data['model']['triggerWords']

    def get_update_time(self):
        return self.raw_data['model']['createdAt']

    def get_author_name(self):
        return self.raw_data['model']['owner']['nickname']

    def get_file_list(self):
        return self.raw_data['model']['files']

    def get_related_covers(self):
        return self.raw_data['model']['cover']

    def build_simplified_detail(self):
        return {
            'id': self.get_id(),
            'name': self.get_name(),
            'type': self.get_type(),
            'base_model': self.get_base_model(),
            'trigger_words': self.get_trigger_words(),
            'update_time': self.get_update_time(),
            'author_name': self.get_author_name(),
        }

    def build_standard_detail(self):
        return {
            'id': self.get_id(),
            'name': self.get_name(),
            'description': self.get_description(),
            'type': self.get_type(),
            'base_model': self.get_base_model(),
            'trigger_words': self.get_trigger_words(),
            'update_time': self.get_update_time(),
            'author_name': self.get_author_name(),
            'file_list': self.get_file_list(),
            'related_covers': self.get_related_covers()
        }

    def save_2_file(self):
        self.project_dir = str(os.path.join(get_root_dir(), "data", self.get_id()))
        cover_dir = os.path.join(self.project_dir, "cover")
        detail_json_dir = os.path.join(self.project_dir, f'{self.raw_data["model"]["files"][0]["name"]}.json')

        if not os.path.exists(self.project_dir):
            os.makedirs(self.project_dir)
        if not os.path.exists(cover_dir):
            os.makedirs(cover_dir)

        with open(detail_json_dir, "w", encoding="utf-8") as file:
            json.dump(self.raw_data, file, ensure_ascii=False, indent=4)

    def get_project_dir(self) -> str:
        if self.project_dir is None:
            return str(os.path.join(get_root_dir(), "data", self.get_id()))
        return self.project_dir


class TusiArt:
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

    @staticmethod
    def get_cover_image(cover_url: str, save_path: str):
        filename = cover_url.split("/")[-1]  # 从 URL 中获取文件名
        full_save_path = os.path.join(save_path, filename)
        s: Session = wa_spider_share.wa_requests_session

        response = s.get(cover_url)
        if response.status_code == 200:
            with open(full_save_path, 'wb') as f:
                f.write(response.content)
            print(f"图片已成功下载到指定路径，文件名为: {filename}\n")
        else:
            print("下载失败，HTTP状态码: ", response.status_code)
