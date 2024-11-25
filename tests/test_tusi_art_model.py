from unittest import TestCase

from src.tusi_art_model import TusiArtModel


class TestTusiArtModel(TestCase):
    def test_get_model_detail(self):
        response_json = TusiArtModel.get_model_detail(
            '716869009959579815'
        )

        print(response_json)
