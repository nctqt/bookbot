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

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_text(book_path)

    total_words = word_count(book_text)
    print(f"There are {total_words} words in the file.")
    
    char_dict = character_count(book_text)
    print(char_dict)



main()