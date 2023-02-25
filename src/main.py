from pathlib import Path
from split_files import file_name_to_dict

def list_files(location='./Photos/2022-01'):
    return list(Path(location).rglob("*.jpg"))

def test_list_files():
    return [
        'Mad_EC_1_35_July_1958.jpg',
        'Detective Comics_DC_1_1_Sep_1940.jpg',
        'Mad___110_Sep_1966.jpg',
        'Mad_ _ _110_Sep_1966.jpg',
        'Mad_     _     _110_Sep_1966.jpg',
        'Detective Comics___4__1953.jpg',
        'Mad___250.jpg',
        'Simpsons Shenanigans_Bongo.jpg'
    ]

def sort_file_names(files: list):
    for file in files:
        print(file_name_to_dict(file))

if __name__=='__main__':
    files = test_list_files()
    sort_file_names(files)
