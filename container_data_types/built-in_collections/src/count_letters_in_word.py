word = "banana"
freq_counter = {}

# for loop to iterate over the letters in word
for letter in word:
    # condition to check if letter is not yet added as a key in the freq_counter dict
    if letter not in freq_counter:
        freq_counter[letter] = 0         # initialize the count to 0
    freq_counter[letter] += 1            # each time a letter is repeated, increment the counter

print(freq_counter)          # Output: {'b': 1, 'a': 3, 'n': 2}