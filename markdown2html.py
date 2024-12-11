#!/usr/bin/python3
"""
Markdown to HTML converter.
This script validates input arguments for converting a Markdown file
to an HTML file. It processes:
- Markdown headings (#, ##, etc.) to HTML heading tags (<h1>, <h2>, etc.).
- Unordered (-) and ordered (*) lists to <ul> and <ol> tags.
- Bold (**text**) to <b> and emphasis (__text__) to <em>.
Usage: ./markdown2html.py README.md README.html
"""

import os
import sys
import re


def convert_inline_styles(line):
    """
    Converts bold and emphasized Markdown syntax to HTML.
    """
    # Convert bold (**) to <b>
    line = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', line)
    # Convert emphasized (__) to <em>
    line = re.sub(r'__(.+?)__', r'<em>\1</em>', line)
    return line


def process_markdown(input_file, output_file):
    """
    Reads a Markdown file, processes its content, and writes the HTML output.
    """
    try:
        unordered_start = False
        ordered_start = False
        paragraph_lines = []

        with open(input_file, 'r') as read, open(output_file, 'w') as html:
            for line in read:
                stripped_line = line.strip()
                stripped_unordered = line.lstrip('-')
                stripped_ordered = line.lstrip('*')
                stripped_heading = line.lstrip('#')
                heading_level = len(line) - len(stripped_heading)
                unordered_num = len(line) - len(stripped_unordered)
                ordered_num = len(line) - len(stripped_ordered)

                # Handle headings
                if 1 <= heading_level <= 6:
                    if unordered_start:
                        html.write('</ul>\n')
                        unordered_start = False
                    if ordered_start:
                        html.write('</ol>\n')
                        ordered_start = False
                    if paragraph_lines:
                        html.write('<p>{}</p>\n'
                                   .format('<br/>'.join(paragraph_lines)))
                        paragraph_lines = []
                    html.write('<h{}>{}</h{}>\n'.format(
                        heading_level,
                        convert_inline_styles(stripped_heading.strip()),
                        heading_level
                    ))
                # Handle unordered lists
                elif unordered_num:
                    if not unordered_start:
                        html.write('<ul>\n')
                        unordered_start = True
                    if paragraph_lines:
                        html.write('<p>{}</p>\n'
                                   .format('<br/>'.join(paragraph_lines)))
                        paragraph_lines = []
                    html.write('<li>{}</li>\n'.format(
                        convert_inline_styles(stripped_unordered.strip())
                    ))
                # Handle ordered lists
                elif ordered_num:
                    if not ordered_start:
                        html.write('<ol>\n')
                        ordered_start = True
                    if paragraph_lines:
                        html.write('<p>{}</p>\n'
                                   .format('<br/>'.join(paragraph_lines)))
                        paragraph_lines = []
                    html.write('<li>{}</li>\n'.format(
                        convert_inline_styles(stripped_ordered.strip())
                    ))
                # Handle paragraph lines
                elif stripped_line:
                    if unordered_start:
                        html.write('</ul>\n')
                        unordered_start = False
                    if ordered_start:
                        html.write('</ol>\n')
                        ordered_start = False
                    paragraph_lines.append(
                        convert_inline_styles(stripped_line))
                # Handle empty lines (end of a paragraph)
                else:
                    if paragraph_lines:
                        html.write('<p>{}</p>\n'
                                   .format('<br/>'.join(paragraph_lines)))
                        paragraph_lines = []

            # Close any remaining open tags
            if unordered_start:
                html.write('</ul>\n')
            if ordered_start:
                html.write('</ol>\n')
            if paragraph_lines:
                html.write('<p>{}</p>\n'.format('<br/>'.join(paragraph_lines)))

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


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
    output_file = sys.argv[2]

    # Validate the existence of the input file
    if not os.path.isfile(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    # Processes the markdown
    process_markdown(input_file, output_file)
    # Success case exits with status 0
    sys.exit(0)


if __name__ == "__main__":
    main()