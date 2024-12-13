#!/opt/homebrew/bin/python3

def get_text(path):
    with open(path) as f:
        text = f.read()
    return text

def word_count(text):
    return len(text.split())

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
    book_path = "books/frankenstein.txt"
    book_text = get_text(book_path)
    total_words = word_count(book_text)
    char_dict = character_count(book_text)

    print(f"--- Begin report of {book_path} ---")
    print(f"There are {total_words} words in the text.\n")
    sorted_count = dict_sort(char_dict)
    for item in sorted_count:
        print(f"The {item["alpha"]} character was found {item["number"]} times.")

main()