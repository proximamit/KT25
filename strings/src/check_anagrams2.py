# Anagrams are 
# Strings that contain the same characters in a different order


# Python program to check whether the two strings in each tuple are anagrams

from collections import Counter

def is_anagram(str1, str2):
    # Using Counter to count the frequency of each character after
    # removing spaces and convert to lowercase for fair comparison
    return Counter(str1.replace(" ", "").lower()) == Counter(
        str2.replace(" ", "").lower())


def check_anagrams(pair_of_strings):
    for a_pair in pair_of_strings:
        # tuple unpacking
        s1, s2 = a_pair
        if is_anagram(s1, s2):
            print(f"{s1} and {s2} are anagrams.")
        else:
            print(f"{s1} and {s2} are not anagrams.")



given_pairs_of_strings = [('earth', 'heart'), 
                ('apple', 'palle'),
                ('evil', 'vile'), ('rat', 'tar')
]

check_anagrams(given_pairs_of_strings)
