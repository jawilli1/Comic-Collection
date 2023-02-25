FIELDS = (
    'Name',
    'Publisher',
    'Volume',
    'Number',
    'Month/season',
    'Year',
    'Series',
)

def assert_file_name_list(file_name_list):
    file_name_list_length = len(file_name_list)
    field_length = len(FIELDS)
    assert file_name_list_length >= 1, "File must have a name"
    assert file_name_list_length <= field_length, f"File can only have {field_length} has {file_name_list_length}"

def file_name_to_dict(file):
    renamed_file = str(file).split('.jpg')[0]
    splitted_file = renamed_file.split('_')
    assert_file_name_list(splitted_file)
    output = {}
    for idx, field in enumerate(FIELDS):
        try:
            output[field] = splitted_file[idx].strip()
        except IndexError:
            output[field] = ''
    return output
