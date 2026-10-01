"""
finds substring corresponding to email addresses and the following 100 characters in the input text
"""


import re
import sys
import argparse


def process_input(text):
    email_pattern = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
    results = []

    for match in email_pattern.finditer(text):
        email = match.group()
        start_index = match.end()
        next_100 = text[start_index:start_index + 100]
        results.append({"email": email, "next_100": next_100})

    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()
    with open(args.file, "r", encoding="utf-8") as f:
        text = f.read()
    for item in process_input(text):
        print(item)


if __name__ == "__main__":
    main()
    