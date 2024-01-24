import os
import re

# Define a regular expression pattern to match fields in filenames
pattern = r'([^_^]+)'


# Function to extract fields from a filename and return them as a
# comma-separated string
def extract_fields(filename):
    # Remove the ".jpg" extension before extracting fields
    filename = filename.rstrip('.jpg')
    fields = re.findall(pattern, filename)
    return ','.join(fields)


# Function to traverse a directory and process each file
def traverse_directory(directory):
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.jpg'):
                fields = extract_fields(filename)
                print(fields)


# Specify the directory you want to traverse
directory_to_traverse = "Photos"


if __name__ == "__main__":
    traverse_directory(directory_to_traverse)
