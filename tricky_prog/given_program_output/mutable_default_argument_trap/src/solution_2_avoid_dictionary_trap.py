def count_word(word, counts=None):
    if counts is None:
        counts = {}

    counts[word] = counts.get(word, 0) + 1
    return counts

print(count_word("a"))  # Output: {'a': 1}
print(count_word("b"))  # Output: {'b': 1}
