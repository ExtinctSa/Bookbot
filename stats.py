
def num_words(text):
    words = text.split()
    return len(words)

def all_symbols(words):
    symbols = {}
    lowercase = words.lower()
    for symbol in lowercase:
        if symbol not in symbols:
            symbols[symbol] = 1
        elif symbol in symbols:
            symbols[symbol] += 1
    return symbols
def sorted_symbols(all_symbols):
    list_of_dicts = [{"char": key, "num": value} for key, value in all_symbols.items() if key.isalpha()]
    sorted_by_value = sorted(list_of_dicts, key=lambda item: item["num"],reverse=True)

    return sorted_by_value
