#!/usr/bin/python3
"""
Markdown to HTML converter.
This script validates input arguments for converting a Markdown file
to an HTML file. It ensures:
1. Correct usage with two arguments: input Markdown file and output HTML file.
2. The input file exists before proceeding.
Usage: ./markdown2html.py README.md README.html
"""

import os  # For file and path-related operations
import sys  # For interacting with the command-line arguments and system


def main():
    """
    Main function to validate input arguments and file existence.
    """
    # Validate the number of arguments
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)

    # Extract input and output file names
    input_file = sys.argv[1]
    # output_file = sys.argv[2]
    # Currently unused but reserved for further steps
    # Validate the existence of the input file
    if not os.path.isfile(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    # Placeholder for further logic
    # Success case exits with status 0
    sys.exit(0)


if __name__ == "__main__":
    main()