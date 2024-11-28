import json
from unittest import TestCase

from src.models.tusi_art import TusiArt

from src.models.tusi_art import TusiArtModelDetail


class TestTusiArtModelDetail(TestCase):
    def test_build_simplified_detail(self):
        with open('../docs/tusi_model_detail.json', 'r', encoding='utf-8') as f:
            detail_data = json.load(f)['data']

            test_detail = TusiArtModelDetail(detail_data)

            print(test_detail.build_simplified_detail())


class TestTusiArt(TestCase):
    def test_get_model_detail(self):
        response_json = TusiArt.get_model_detail(
            '716869009959579815'
        )

        print(response_json)

    def test_get_cover_image(self):
        TusiArt.get_cover_image(
            'https://images.tusiassets.com/model_showcase/0/8607847e-a5ca-e286-d414-2e72d410446e.png'
        )
