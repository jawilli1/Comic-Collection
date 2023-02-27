import os

def parse_input():
    file_dir = str(input("Provide directory to loop through (relative to here): "))
    number_file = str(input("Provide number list file: "))
    with open(number_file, 'r') as f:
        numbers = f.readlines()
    return file_dir, numbers

def rename_file_numbers(directory, number_list):
    files = os.listdir(directory)

    assert len(files) == len(number_list), f"""
    JEFF ERROR: Found {len(files)} files and {len(number_list)} list. FAILURE!
    """

    for i, file in enumerate(files):
        old_file_path = os.path.join(directory, file)
        new_file = file[:-8] + str(number_list[i]) + '.jpg'
        new_file_path = os.path.join(directory, new_file)
        os.rename(old_file_path, new_file_path)
        print(f"Renamed\t{old_file_path} to \n\t\t{new_file_path}")

if __name__=='__main__':
    my_directory, x = parse_input()
    rename_file_numbers(my_directory, x)