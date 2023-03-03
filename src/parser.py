import argparse


def parse():
    args = argparse.ArgumentParser(
        prog="Wilson's comic collection",
        description="""
            Loops through a directory of files extracting necessary 
            metadata from file names into a csv to be used for 
            cataloging Jeff's catalog collection. If you are trying to 
            use this for something other than make spreadsheets for 
            Jeff's comic collection - may god have mercy on your soul.
            """,
        add_help=True,
    )

    args.add_argument(
        "--directory",
        "-d",
        type=str,
        default="./Photos/",
        help="Relative path to start parsing files",
    )
    args.add_argument(
        "--output-file", "-out", type=str, required=True, help="Name of file for output"
    )

    return args.parse_args()
