from pathlib import Path
from split_files import file_name_to_dict, convert_dicts_to_csv
from parser import parse


def list_files(location="./Photos/"):
    return list(file.name for file in Path(location).rglob("*.jpg"))


def sort_file_names_to_dict(files: list):
    rows = []
    for file in files:
        rows.append(file_name_to_dict(file))
    return rows


def write_dict_to_csv(dict_list, file_name):
    convert_dicts_to_csv(dict_list=dict_list, file_name=file_name)


if __name__ == "__main__":

    args = parse()
    files = list_files(location=args.directory)
    dict_list = sort_file_names_to_dict(files)
    write_dict_to_csv(dict_list, args.output_file)

    print(
        f"""
    Found {len(dict_list)} files within '{args.directory}' to parse.
    Ouput file written to '{args.output_file}'.
    """
    )
