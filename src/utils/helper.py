import os


def format_dict_as_string(input_dict):
    formatted_string = "\n".join([f"{key}: {value}" for key, value in input_dict.items()])
    return formatted_string


def format_dict_value_as_string(input_dict):
    return {key: str(value) for key, value in input_dict.items()}


def get_root_dir():
    return os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
