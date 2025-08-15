from functools import reduce

def longest_common_substr(strings):
    if not strings:
        return ""

    # Function to generate all substrings of a string
    substrings = lambda s: set(s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1))

    """
    Explanation :- 
    Suppose s = "abc", len(s) = 3
    for i in range(len(s)) => i = 0 to 2 

    Outer loop: i = 0 
        Inner loop: j = 1, 2, 3
        Substrings: s[0:1] = 'a' , s[0:2] = 'ab', s[0:3] = 'abc'

    Outer loop: i = 1 
        Inner loop: j = 2, 3
        Substrings: s[1:2] = 'b', s[1:3] = 'bc'

    Outer loop: i = 2
        Inner loop: j = 3
        Substrings: s[2:3] = 'c'

    All substrings generated - 
    ['a', 'ab', 'abc', 'b', 'bc', 'c']
    """

    # Reduce to find common substrings across all strings

    '''
    reduce(function, iterable, initializer) 
    '''

    common_substrings = reduce(
        lambda acc, s: acc & substrings(s),
        strings[1:],
        substrings(strings[0])
    )
    # Return the longest one
    return max(common_substrings, key=len) if common_substrings else ""

    """
    lambda acc, s: acc & substrings(s)

    acc - accumulated set of common substrings so far 
    s is the next string in the list
    acc & substrings(s) performs a set intersection between
    the current common substrings
    and all substrings of s 

    reduce(
        function,  lambda function
        iterable,  all strings except the first one 
        initializer all substrings of the first string
        ) 
    """

arr = ["interspecies", "interstellar", "interstate"]
print(longest_common_substr(arr))
