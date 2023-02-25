FIELDS = (
    'Name',
    'Publisher',
    'Volume',
    'Number',
    'Month/season',
    'Year',
    'Series',
)

def file_name_to_dict(file):
    renamed_file = str(file).split('.jpg')[0]
    splitted_file = renamed_file.split('_')
    assert len(splitted_file) >= 1
    assert len(splitted_file) <= len(FIELDS)
    output = {}
    for idx, field in enumerate(FIELDS):
        try:
            output[field] = splitted_file[idx].strip()
        except IndexError:
            output[field] = ''
    return output
