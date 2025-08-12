#!/opt/homebrew/bin/python3

import sys
from stats import word_count

if len(sys.argv) != 2:
    print(f"Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_text(path):
    with open(path) as f:
        text = f.read()
    return text

def character_count(text):
    char_count = {}
    text = text.lower()
    for char in text:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1

    return char_count

def sort_on(dict):
    return dict["number"]

def dict_sort(chars):
    alpha_dict = {}
    for key in chars:
        if key.isalpha():
            alpha_dict[key] = chars[key]
    new_list = []
    for key, value in alpha_dict.items():
        new_list.append({"alpha": key, "number": value})
    new_list.sort(reverse=True, key=sort_on)
    return new_list

def main():
    book_path = sys.argv[1]
    book_text = get_text(book_path)
    total_words = word_count(book_text)
    char_dict = character_count(book_text)

    print(f"--- Begin report of {book_path} ---")
    print(f"There are {total_words} words found in the document.\n")
    sorted_count = dict_sort(char_dict)
    for item in sorted_count:
        print(f"{item["alpha"]}: {item["number"]}")

main()