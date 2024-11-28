from src.models.tusi_art import TusiArt, TusiArtModelDetail
from src.utils.helper import format_dict_as_string


class TusiArtFetcher:
    def __init__(self, raw_url: str):
        self.raw_url = raw_url
        self.model_id = None
        self.model_detail = None

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
