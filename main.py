import sys
from stats import (all_symbols, num_words, sorted_symbols)
if len(sys.argv) > 1:
    relative_path = sys.argv[1]
else:
    print('Usage: "python main.py <path_to_book>"')
    sys.exit[1]
def get_book_text(relative_path):
    with open(relative_path) as file:
        return file.read()
def main():
    text = get_book_text(relative_path)
    word_count = num_words(text)
    symbol_count = all_symbols(text)
    sorted_symbol = sorted_symbols(symbol_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {relative_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for symbol_dict in sorted_symbol:
        print(f"{symbol_dict['char']}: {symbol_dict['num']}")
    print("============= END ===============")

main()
