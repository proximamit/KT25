from itertools import permutations

def is_anagram(s1, s2):
    return s2 in map(''.join, permutations(s1))

print(is_anagram('silent', 'listen'))
