# Generator expression inside dict()

words = ["apple", "banana", "kiwi"]

lengths = dict(
    (w, len(w))
    for w in words
)

print(lengths)


# dict comprehension
# {w: len(w) for w in words}

print({w: len(w) for w in words})
