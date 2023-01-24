def numeronymize(text, n=10):
    import re
    n = max(n, 3)
    pattern = r'\b[a-zA-Z]+\b'
    words = re.findall(pattern, text)

    for word in words:
        if len(word) >= n:
            numeronymized_word = f"{word[0]}{len(word) - 2}{word[-1]}"
            text = text.replace(word, numeronymized_word)

    return text