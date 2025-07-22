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
