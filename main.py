relative_path = "books/frankenstein.txt"
def get_book_text(relative_path):
    with open(relative_path) as file:
        return file.read()
def main():
    text = get_book_text(relative_path)
    word_count = num_words(text)
    print(f"{word_count} words found in the document")
def num_words(text):
    words = text.split()
    return len(words)

main()
