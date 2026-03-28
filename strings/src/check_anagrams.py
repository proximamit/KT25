# Write a Python program to check if two strings are Anagrams (or not)

def is_anagram(str1, str2):
    """Check if two strings are anagrams by removing spaces, 
    converting to lowercase) and sorting."""

    return sorted(str1.replace(" ", "").lower()) == sorted(
                  str2.replace(" ", "").lower())

if __name__ == "__main__":
    print(is_anagram("race", "care"))  # True

    # Example(s)
    #s1 = 'listen'
    #s2 = 'silent'

    #s1= 'hello'
    #s2 = 'world'

    s1= 'triangle'
    s2 = 'integral'

    if is_anagram(s1, s2):
        print(f"'{s1}' and '{s2}' are anagrams.")
    else:
        print(f"'{s1}' and '{s2}' are not anagrams.")
