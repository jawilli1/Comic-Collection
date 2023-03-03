from pathlib import Path
from split_files import file_name_to_dict, convert_dicts_to_csv


def list_files(location="./Photos/2022-01"):
    return list(Path(location).rglob("*.jpg"))


def test_list_files():
    return [
        "Mad^EC^1^%35^July^1958.jpg",
        "Detective Comics^DC^1^1^Sep^1940.jpg",
        "Mad^^^110^Sep^1966.jpg",
        "Mad^ ^ ^110^Sep^1966.jpg",
        "Mad^     ^     ^110^Sep^1966.jpg",
        "Detective Comics^^^4^^1953.jpg",
        "Mad^^^250.jpg",
        "Simpsons Shenanigans^Bongo.jpg",
    ]


def sort_file_names_to_dict(files: list):
    rows = []
    for file in files:
        rows.append(file_name_to_dict(file))
    return rows


def write_dict_to_csv(dict_list, file_name):
    convert_dicts_to_csv(dict_list=dict_list, file_name=file_name)


if __name__ == "__main__":
    files = test_list_files()
    dict_list = sort_file_names_to_dict(files)
    # write_dict_to_csv(dict_list, 'file_names.csv')
    print(len(dict_list))
