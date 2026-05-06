
def trim_trailing_vowels(str1):
    vowels = "aeiou"
    
    # Start from the end of the string
    i = len(str1) - 1
    
    # Move backwards while characters are vowels
    while i >= 0 and str1[i] in vowels:
        i -= 1
    
    # Return the string up to the last non-vowel
    return str1[:i+1]

if __name__ == "__main__":
# Example usage
    str1 = "idea"
    result = trim_trailing_vowels(str1)
    #print(result)  # Output: "id"
    print("\n")
    print(f"When the string '{str1}' is trimmed of trailing vowels, ")
    print(f"we get the string '{result}'")
    print("\n")
    print(trim_trailing_vowels("hello"))   # "hell"
    print(trim_trailing_vowels("aeiou"))   # "" (all vowels removed)
    print(trim_trailing_vowels("data"))    # "dat"
    print(trim_trailing_vowels("sky"))     # "sky" (no trailing vowels)
    
