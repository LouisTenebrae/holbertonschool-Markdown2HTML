#!/usr/bin/python3
"""Markdown to HTML"""

import os
import sys

if (len(sys.argv) < 3):
    sys.stderr.write("Usage: ./markdown2html.py README.md README.html")
    exit(1)

if not (os.path.isfile(sys.argv[1])):
    sys.stderr.write("Missing " + sys.argv[1])
    exit(1)

exit(0)