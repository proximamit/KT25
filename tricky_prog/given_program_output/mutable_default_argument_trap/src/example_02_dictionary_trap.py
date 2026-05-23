def count_word(word, counts={}):
    counts[word] = counts.get(word, 0) + 1
    return counts

print(count_word.__defaults__)
print(count_word("a"))  # Output: {'a': 1}
print(count_word("b"))  # Output: {'a': 1, 'b': 1}
print(count_word("a"))  # Output: {'a': 2, 'b': 1}
print(count_word.__defaults__)
