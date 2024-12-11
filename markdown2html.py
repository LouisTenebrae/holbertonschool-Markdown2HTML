#!/usr/bin/python3
"""
Markdown to HTML converter
"""

import os  # For file and path-related operations
import sys  # For interacting with the command-line arguments and system


def main():
    """
    Main function to validate input arguments and file existence.
    """

    # Ensure at least 3 arguments are provided: script name, input file,
    # and output file
    if len(sys.argv) < 3:
        # Print usage error message to stderr
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html")
        # Exit with an error code 1
        sys.exit(1)

    # Extract the input file name from command-line arguments
    input_file = sys.argv[1]
    # Check if the specified input file exists
    if not os.path.isfile(input_file):
        # Print a missing file error message to stderr
        sys.stderr.write(f"Missing {input_file}\n")
        # Exit with an error code 1
        sys.exit(1)

    # If all checks pass, the script exits successfully
    sys.exit(0)


if __name__ == "__main__":
    # Execute the main function when the script is run directly
    main()
