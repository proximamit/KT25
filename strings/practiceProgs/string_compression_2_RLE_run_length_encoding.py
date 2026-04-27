def compress_string(word):
    if not word:
        return ""
    
    res = []
    i = 0
    while i < len(word):
        count = 1
        # Count consecutive identical characters
        while i + 1 < len(word) and word[i] == word[i+1]:
            count += 1
            i += 1
        
        # Append count and character to result list
        res.append(f"{count}{word[i]}")
        i += 1
        
    return "".join(res)

# Example 1
print(compress_string("abcde"))    # Output: "1a1b1c1d1e"

# Example 2
print(compress_string("aaaaabb"))  # Output: "5a2b"