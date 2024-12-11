#!/usr/bin/python3
'''
This module check the files params in the sys
Argv[1] is a file input
Argv[2] is a file output
'''
import sys
import os


if __name__ == "__main__":

    if len(sys.argv) != 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(input_file):
        sys.stderr.write(f"Missing {input_file}\n")
        sys.exit(1)
    sys.exit(0)
