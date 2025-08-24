# Write a python program to find the first non-repeating character in a string "Swiss"

from collections import Counter

def first_non_repeating_char(s):
    s = s.lower()       # for case-insensitive comparison
    # count each character in the string
    count = Counter(s)  # create a dictionary-like object with character counts

    for char in s:
        if count[char] == 1:
            return char
    return None

# Example
#input_str = "Swiss"
input_str = "Malayalam"
#input_str = "Never odd or even"
#input_str = "A nut for a jar of tuna"
result = first_non_repeating_char(input_str)

if result:
    print(f"The first non-repeating character in \n{input_str} is: '{result}'")
else:
    print(f"There is no non-repeating character in the string:- \n{input_str}.")
