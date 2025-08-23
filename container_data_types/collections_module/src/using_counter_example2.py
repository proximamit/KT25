from collections import Counter

word = "banana"
char_freq = Counter(word)
print(dict(char_freq))          # Output: {'b': 1, 'a': 3, 'n': 2}
