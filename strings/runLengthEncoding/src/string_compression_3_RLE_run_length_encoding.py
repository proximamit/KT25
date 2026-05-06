from itertools import groupby

def compress_string_v2(word):
    # Groups characters and joins their length + character
    return "".join(f"{len(list(group))}{char}" for char, group in groupby(word))

print(compress_string_v2("aaaaabb"))  # Output: "5a2b"
