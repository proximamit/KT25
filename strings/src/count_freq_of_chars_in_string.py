# Write a python program to find the first non-repeating character in a given string.  for example string - "Swiss"

def first_non_repeating_char(s):
    """Find the first character in a given string that appears only once. """
    # Convert to lowercase to make the check case-insensitive (optional)
    s = s.lower()          # make the string lowercase so that uppercase and lowercase versions of the same letter are treated equally

    # Count frequency of each character
    # Create a dictionary that will store characters as keys and how many times they appear as values
    char_count = {}                                     # create an empty dictionary named char_count
    for char in s:                                      # for loop to go through each character in the string
        # Use .get() method of Python dictionary to retrieve the value for given key
        # dict.get(key, default_value)
        # key = the key to look up in the dictionary
        # default_value (optional) - The value to return if the key is not found

        #                        dict.get(key, default_value)
        char_count[char] = char_count.get(char, 0) + 1
        # char_count[char] = ...            --> to save the new updated count back into the dictionary
        # char_count.get(char, 0)     --> 
        # Check if the character is already in the dictionary.
        # If it is, return its current count.
        # If it’s not, returns 0 (the default).
        # + 1  ---> Add 1 to the count (because we just saw the character again).

    # Find the first character with count 1
    for char in s:                          # go through the string again
        if char_count[char] == 1:           # check each character to see if it only appears once
            return char                     # The first such character is returned
    # If no non-repeating character is found, the function returns None
    return None  # If all characters repeat

# Test the function
input_str = "Swiss"
#input_str = "Malayalam"
#input_str = "Never odd or even"
#input_str = "A nut for a jar of tuna"

result = first_non_repeating_char(input_str)

if result:
    print(f"In the given string:- {input_str}, the first non-repeating character is: '{result}'")
else:
    print(f"There is no non-repeating character in the given string :- {input_str}.")
