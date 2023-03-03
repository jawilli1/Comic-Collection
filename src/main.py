from pathlib import Path
from split_files import file_name_to_dict, convert_dicts_to_csv


def list_files(location="./Photos/"):
    return list(Path(location).rglob("*.jpg"))


def sort_file_names_to_dict(files: list):
    rows = []
    for file in files:
        rows.append(file_name_to_dict(file))
    return rows


def write_dict_to_csv(dict_list, file_name):
    convert_dicts_to_csv(dict_list=dict_list, file_name=file_name)


if __name__ == "__main__":
    files = list_files()
    dict_list = sort_file_names_to_dict(files)
    write_dict_to_csv(dict_list, 'file_names.csv')
    print(len(dict_list))
