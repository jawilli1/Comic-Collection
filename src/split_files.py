import csv

FIELDS = (
    "Name",
    "Number",
    "Month",
    "Year",
    "Volume",
    "Publisher",
    "Series",
)


def assert_file_name_list(file_name_list):
    file_name_list_length = len(file_name_list)
    field_length = len(FIELDS)
    assert file_name_list_length >= 1, "File must have a name"
    assert (
        file_name_list_length <= field_length
    ), f"File can only have {field_length} has {file_name_list_length}"


def remove_placeholders_map(item):
    if str(item).startswith("%"):
        return ""
    return item


def file_name_to_dict(file):
    renamed_file = str(file).split(".jpg")[0]
    splitted_file = renamed_file.split("_")
    splitted_file = list(map(remove_placeholders_map, splitted_file))
    assert_file_name_list(splitted_file)
    file_name_dict = {}
    for idx, field in enumerate(FIELDS):
        try:
            file_name_dict[field] = splitted_file[idx].strip()
        except IndexError:
            file_name_dict[field] = ""
    return file_name_dict


def convert_dicts_to_csv(dict_list, file_name):

    with open(file_name, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELDS)
        writer.writeheader()
        for row in dict_list:
            writer.writerow(row)
