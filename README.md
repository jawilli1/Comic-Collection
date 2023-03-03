# Comic-Collection


```
usage: Wilson's comic collection [-h] [--directory DIRECTORY] --output-file OUTPUT_FILE

Loops through a directory of files extracting necessary metadata from file names into a csv
to be used for cataloging Jeff's catalog collection. If you are trying to use this for
something other than make spreadsheets for Jeff's comic collection - may god have mercy on
your soul.

optional arguments:
  -h, --help            show this help message and exit
  --directory DIRECTORY, -d DIRECTORY
                        Relative path to start parsing files
  --output-file OUTPUT_FILE, -out OUTPUT_FILE
                        Name of file for output
```

### How to run
```bash
$ ./run.py --directory name/of/dir --output-file my_output_file.csv
```
