from unittest import TestCase

from src.models.tusi_art import TusiArtModel


class TestTusiArtModel(TestCase):
    def test_get_model_detail(self):
        response_json = TusiArtModel.get_model_detail(
            '716869009959579815'
        )

        print(response_json)
