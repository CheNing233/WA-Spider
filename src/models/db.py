import sqlite3

from src.utils.helper import format_dict_value_as_string


class DB:
    def __init__(self, db_file_path: str = '../data/database.db'):
        self.connection = sqlite3.connect(db_file_path)
        self.cursor = self.connection.cursor()
        self.create_model_detail_table()

    def create_model_detail_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS model_detail (
                id INTEGER PRIMARY KEY NOT NULL UNIQUE,
                name TEXT,
                description TEXT,
                type TEXT,
                base_model TEXT,
                trigger_words TEXT,
                update_time TEXT,
                author_name TEXT,
                file_list TEXT,
                related_covers TEXT
            )
        ''')
        self.connection.commit()

    def insert_model_detail(self, data):
        data_stringify = format_dict_value_as_string(data)

        try:
            self.cursor.execute('''
                INSERT INTO model_detail (id, name, description, type, base_model, trigger_words, update_time, author_name, file_list, related_covers)
                VALUES (:id, :name, :description, :type, :base_model, :trigger_words, :update_time, :author_name, :file_list, :related_covers)
            ''', data_stringify)
            self.connection.commit()
            print("Data inserted successfully.")
        except sqlite3.IntegrityError as e:
            print("Error:", e)

    def close_connection(self):
        self.connection.close()
