def compress_string(s):
    if not s:
        return ""

    compressed = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(str(count) + s[i - 1])
            count = 1

    # Add the last character group
    compressed.append(str(count) + s[-1])

    return "".join(compressed)


# Examples
print(compress_string("abcde"))     # Output: 1a1b1c1d1e
print(compress_string("aaaaabb"))   # Output: 5a2b