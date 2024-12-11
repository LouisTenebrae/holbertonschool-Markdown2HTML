#!/usr/bin/env python3

import sys
import os

def convert_markdown_to_html(markdown_content):
    """Convert simple Markdown to HTML."""
    html_content = []

    for line in markdown_content.splitlines():
        line = line.strip()

        # Convert headers (# to <h1>, ## to <h2>, etc.)
        if line.startswith("#"):
            header_level = len(line.split(' ')[0])  # Count leading '#' characters
            header_content = line[header_level:].strip()
            html_content.append(f"<h{header_level}>{header_content}</h{header_level}>")
        
        # Convert bold (**text** or __text__)
        elif "**" in line or "__" in line:
            line = line.replace("**", "<b>").replace("__", "<b>", 1)
            line = line.replace("**", "</b>").replace("__", "</b>", 1)
            html_content.append(f"<p>{line}</p>")
        
        # Convert italic (*text* or _text_)
        elif "*" in line or "_" in line:
            line = line.replace("*", "<i>").replace("_", "<i>", 1)
            line = line.replace("*", "</i>").replace("_", "</i>", 1)
            html_content.append(f"<p>{line}</p>")
        
        # Convert links ([text](url))
        elif "[" in line and "]" in line and "(" in line and ")" in line:
            while "[" in line and "]" in line and "(" in line and ")" in line:
                start_text = line.index("[")
                end_text = line.index("]")
                start_url = line.index("(", end_text)
                end_url = line.index(")", start_url)
                text = line[start_text + 1:end_text]
                url = line[start_url + 1:end_url]
                line = line[:start_text] + f'<a href="{url}">{text}</a>' + line[end_url + 1:]
            html_content.append(f"<p>{line}</p>")
        
        # Wrap plain text in <p> tags
        else:
            html_content.append(f"<p>{line}</p>")

    return "\n".join(html_content)

def main():
    # Check the number of arguments
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    # Extract arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if the input file exists
    if not os.path.isfile(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    # Read the Markdown file and convert it to HTML
    try:
        with open(input_file, 'r', encoding='utf-8') as markdown_file:
            markdown_content = markdown_file.read()

        html_content = convert_markdown_to_html(markdown_content)

        # Write the HTML to the output file
        with open(output_file, 'w', encoding='utf-8') as html_file:
            html_file.write(html_content)

        sys.exit(0)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
