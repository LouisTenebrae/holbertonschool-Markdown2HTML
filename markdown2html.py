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

    with open(output_file, "w") as out:
        with open(input_file, "r") as int:
            datas = int.readlines()
            for i in range(len(datas)):
                if "**" in datas[i]:
                    datas[i] = datas[i].replace("**", "<b>")
                    rev = datas[i][::-1]
                    start = rev.index(">b<")
                    end = start + 3
                    sett = f"{rev[:start]}>b/<{rev[end:]}"
                    datas[i] = sett[::-1]
                if "__" in datas[i]:
                    datas[i] = datas[i].replace("__", "<em>")
                    rev = datas[i][::-1]
                    start = rev.index(">me<")
                    end = start + 4
                    sett = f"{rev[:start]}>me/<{rev[end:]}"
                    datas[i] = sett[::-1]
                if "((" in datas[i]:
                    ss = datas[i].replace("((", "")
                    ss = ss.replace("))", "").replace("c", "").replace("C", "")
                    datas[i] = ss
                if "[[" in datas[i]:
                    first = datas[i].index("[[")
                    last = datas[i].index("]]")
                    rev = f"{datas[i][:first]}8b1a9953c4611296a827abf8c47804d7{datas[i][last+2:]}"                    
                    datas[i] = rev
                if datas[i].startswith("#"):
                    num = datas[i].count("#")
                    text = datas[i].replace("#", "")[1:]
                    text = text.replace("\n", "")
                    string = f"<h{num}>{text}</h{num}>\n"
                    out.write(string)
                if datas[i].startswith("-"):
                    if datas[i][0] == "-" and datas[i-1][0] != "-":
                        string = "<ul>\n"
                        out.write(string)
                    text = datas[i].replace("- ", "")
                    text = text.replace("\n", "")
                    string = f"<li>{text}</li>\n"
                    out.write(string)
                    if i + 1 < len(datas) and datas[i + 1][0] != "-":
                        string = "</ul>\n"
                        out.write(string)
                    if i + 1 == len(datas):
                        string = "</ul>\n"
                        out.write(string)
                if datas[i].startswith("* "):
                    if datas[i][0] == "*" and datas[i-1][0] != "*":
                        string = "<ol>\n"
                        out.write(string)
                    text = datas[i].replace("* ", "")
                    text = text.replace("\n", "")
                    string = f"<li>{text}</li>\n"
                    out.write(string)
                    if i + 1 < len(datas) and datas[i + 1][0] != "*":
                        string = "</ol>\n"
                        out.write(string)
                    if i + 1 == len(datas):
                        string = "</ol>\n"
                        out.write(string)
                if not datas[i].startswith("#") and not datas[i].startswith("-") and not datas[i].startswith("* "):
                    if not datas[i].startswith("\n"):
                        if datas[i - 1] == "\n" and i + 1 < len(datas):
                            out.write(f"<p>\n{datas[i]}")
                            if datas[i + 1] == "\n" and i + 1 < len(datas):
                                out.write("</p>\n")
                        if datas[i - 1] != "\n" and i + 1 < len(datas):
                            out.write(f"<br/>\n{datas[i]}")
                            if datas[i + 1] == "\n" and i + 1 < len(datas):
                                out.write("</p>\n")
                        if i + 1 == len(datas):
                            if datas[i - 1] != '\n':
                                out.write("<br/>\n")
                            if datas[i] != '\n':
                                out.write(f"<p>\n{datas[i]}</p>")

    sys.exit(0)