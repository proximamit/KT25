trim_trailing_vowels = lambda s: s.rstrip("aeiou")

print(trim_trailing_vowels("idea"))   # "id"
print(trim_trailing_vowels("aeiou"))  # ""
print(trim_trailing_vowels("hello"))  # "hell"
