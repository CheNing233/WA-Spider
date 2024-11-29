import os

from src.models.db import DB
from src.models.tusi_art import TusiArt, TusiArtModelDetail
from src.utils.helper import format_dict_as_string, get_root_dir


class TusiArtFetcher:
    def __init__(self, raw_url: str):
        self.raw_url = raw_url
        self.db = DB(os.path.join(get_root_dir(), 'data', 'database.db'))
        self.db.create_model_detail_table()
        self.model_id = None
        self.model_detail: TusiArtModelDetail | None = None

    def __del__(self):
        self.db.close_connection()

    def fetch_model_detail(self) -> str:
        prefix = "https://www.tusiart.com/models/"
        if self.raw_url.startswith(prefix):
            self.model_id = self.raw_url[len(prefix):]
        else:
            return '无法解析model_id'

        self.model_detail = TusiArtModelDetail(
            TusiArt.get_model_detail(self.model_id)['data']
        )

        return format_dict_as_string(self.model_detail.build_simplified_detail())

    def save_model_detail(self) -> str:
        if self.model_detail is None:
            return 'model_detail 为空'

        self.model_detail.save_2_file()
        self.db.insert_model_detail(self.model_detail.build_standard_detail())

        return f"已保存{self.model_detail.get_name()}"

    def save_model_covers(self) -> str:
        if self.model_detail is None:
            return 'model_detail 为空'

        covers = self.model_detail.get_related_covers()

        for cover in covers:
            TusiArt.get_cover_image(
                cover['url'],
                os.path.join(self.model_detail.get_project_dir(), 'cover')
            )
