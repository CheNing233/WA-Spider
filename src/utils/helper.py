def format_dict_as_string(input_dict):
    formatted_string = "\n".join([f"{key}: {value}" for key, value in input_dict.items()])
    return formatted_string
