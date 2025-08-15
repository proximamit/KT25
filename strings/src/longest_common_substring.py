# Write a program to find Longest common substring in an array of strings

# ["international", "intermission", "interval", "interesting"]
# Longest common substring - inter


# 1. Generate all substings of the first string
#.2. For each substring, check if it exists in all other strings
# 3. Return the longest string from the common ones 

def get_all_substrings(s):
    """ Generates all substrings of a string s """
    substrings = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.append(s[i:j])
    return substrings

def is_common_substring(sub, strings):
    """ Checks whether a substring sub is present in all strings in the list """
    for s in strings:
        if sub not in s:
            return False
    return True

def longest_common_substring(strings):
    """ iterate over all substrings and update longest if a longer common one is found """
    if not strings:
        return ""
    
    all_subs = get_all_substrings(strings[0])
    longest = ""

    for sub in all_subs:
        if is_common_substring(sub, strings) and len(sub) > len(longest):
            longest = sub
    return longest


words = ["international", "intermission", "interval", "interesting"]
print(longest_common_substring(words))