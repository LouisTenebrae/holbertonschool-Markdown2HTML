#!/usr/bin/python3
"""script that tanked an argument 2 strings"""


from sys import argv, exit, stderr
import os


def main():
    """tanked an argument 2 strings"""
    if len(argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=stderr)
        exit(1)
        
    markdown_file = argv[1]
    output_file_name = argv[2]

    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=stderr)
        exit(1)

    exit(0)

if __name__ == "__main__":
    main()