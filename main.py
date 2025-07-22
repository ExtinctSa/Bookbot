from stats import (all_symbols, num_words)
relative_path = "books/frankenstein.txt"
def get_book_text(relative_path):
    with open(relative_path) as file:
        return file.read()
def main():
    text = get_book_text(relative_path)
    word_count = num_words(text)
    symbol_count = all_symbols(text)
    print(f"{word_count} words found in the document", symbol_count)


main()
