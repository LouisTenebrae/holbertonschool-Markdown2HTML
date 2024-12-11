#!/usr/bin/python3
"""
Markdown to HTML converter.
This script validates input arguments for converting a Markdown file
to an HTML file. It processes Markdown syntax including headings, lists,
bold (**text**), and emphasis (__text__) to generate valid HTML.
Usage: ./markdown2html.py README.md README.html
"""

import os
import sys
import re


def apply_text_formatting(text):
    """
    Apply bold (**text**) and emphasis (__text__) formatting to text.
    Args:
        text (str): Input text with Markdown formatting.
    Returns:
        str: Text with HTML formatting applied.
    """
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'__(.*?)__', r'<em>\1</em>', text)
    return text


def process_markdown(input_file, output_file):
    """
    Reads a Markdown file, processes its content, and writes the HTML output.
    Args:
        input_file (str): Path to the input Markdown file.
        output_file (str): Path to the output HTML file.
    """
    try:
        unordered_start = False  # Tracks if a <ul> is open
        ordered_start = False  # Tracks if a <ol> is open
        paragraph_open = False  # Tracks if a <p> is open

        with open(input_file, 'r') as read, open(output_file, 'w') as html:
            for line in read:
                line = line.rstrip()

                # Handle headings
                if line.startswith('#'):
                    if unordered_start:
                        html.write('</ul>\n')
                        unordered_start = False
                    if ordered_start:
                        html.write('</ol>\n')
                        ordered_start = False
                    if paragraph_open:
                        html.write('</p>\n')
                        paragraph_open = False

                    heading_level = len(line) - len(line.lstrip('#'))
                    content = line.lstrip('#').strip()
                    html.write(
                        f'<h{heading_level}>'
                        f'{apply_text_formatting(content)}'
                        f'</h{heading_level}>\n'
                    )

                # Handle unordered lists (-)
                elif line.startswith('- '):
                    if ordered_start:
                        html.write('</ol>\n')
                        ordered_start = False
                    if not unordered_start:
                        html.write('<ul>\n')
                        unordered_start = True
                    content = line.lstrip('-').strip()
                    html.write(f'<li>{apply_text_formatting(content)}</li>\n')

                # Handle ordered lists (*)
                elif line.startswith('* '):
                    if unordered_start:
                        html.write('</ul>\n')
                        unordered_start = False
                    if not ordered_start:
                        html.write('<ol>\n')
                        ordered_start = True
                    content = line.lstrip('*').strip()
                    html.write(f'<li>{apply_text_formatting(content)}</li>\n')

                # Handle paragraphs
                elif line.strip():
                    if unordered_start:
                        html.write('</ul>\n')
                        unordered_start = False
                    if ordered_start:
                        html.write('</ol>\n')
                        ordered_start = False
                    if not paragraph_open:
                        html.write('<p>\n')
                        paragraph_open = True
                    else:
                        html.write('<br/>\n')
                    html.write(apply_text_formatting(line) + '\n')

                # Handle blank lines
                else:
                    if paragraph_open:
                        html.write('</p>\n')
                        paragraph_open = False

            # Close any remaining open tags
            if unordered_start:
                html.write('</ul>\n')
            if ordered_start:
                html.write('</ol>\n')
            if paragraph_open:
                html.write('</p>\n')

    except Exception as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)


def main():
    """
    Main function to validate input arguments and file existence.
    """
    if len(sys.argv) < 3:
        print(
            "Usage: ./markdown2html.py README.md README.html",
            file=sys.stderr
        )
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    process_markdown(input_file, output_file)
    sys.exit(0)


if __name__ == "__main__":
    main()