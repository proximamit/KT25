words = ["apple", "banana", "kiwi"]

result = sorted(
    (w.upper() for w in words),
    key=len
)

print(result)
