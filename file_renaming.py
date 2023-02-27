import os

def parse_number_file(number_file):
    with open(number_file, 'r') as f:
        numbers = [line.rstrip() for line in f.readlines()]
    return numbers

def rename_file_numbers(directory, number_list):
    files = os.listdir(directory)
    files.sort()

    assert len(files) == len(number_list), f"""
    JEFF ERROR: Found {len(files)} files and {len(number_list)} list. FAILURE!
    """

    for i, file in enumerate(files):
        old_file_path = os.path.join(directory, file)
        new_file = f'{file[:-8]}{number_list[i]}.jpg'
        new_file_path = os.path.join(directory, new_file)
        os.rename(old_file_path, new_file_path)
        print(f"Renamed\t{old_file_path} to \n\t\t{new_file_path}")

if __name__=='__main__':
    my_directory = 'Photos/2022-07/Not Cataloged/Simpsons Comics Presents Bart Simpson'
    file_number_list = parse_number_file('Photos/2022-07/Not Cataloged/Simpsons Comics Presents Bart Simpson.txt')
    rename_file_numbers(my_directory, file_number_list)