from unittest import TestCase

from src.models.db import DB


class TestDB(TestCase):

    def test_insert_model_detail(self):
        db = DB()

        db.create_model_detail_table()
        db.insert_model_detail({
            'id': 1,
            'name': 'Model Name',
            'description': 'Model Description',
            'type': 'Model Type',
            'base_model': 'Base Model',
            'trigger_words': 'Trigger Words',
            'update_time': 'Update Time',
            'author_name': 'Author Name',
            'file_list': 'File List',
            'related_covers': 'Related Covers'
        })
        db.close_connection()
