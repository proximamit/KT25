def compress_string(word):
    if not word:
        return ""

    compressed = []
    count = 1
    
    # Iterate through the string starting from the second character
    for i in range(1, len(word)):
        if word[i] == word[i-1]:
            count += 1
        else:
            # Append the count and the previous character
            compressed.append(f"{count}{word[i-1]}")
            count = 1
            
    # Don't forget the last group of characters
    compressed.append(f"{count}{word[-1]}")
    
    return "".join(compressed)

# Test Cases
print(f"Input: 'abcde'   -> Output: '{compress_string('abcde')}'")
print(f"Input: 'aaaaabb' -> Output: '{compress_string('aaaaabb')}'")