def remove_vowel_words(sentence):
    vowels = ('a', 'e', 'i', 'o', 'u')

    # Split sentence into words
    words = sentence.split()

    # Filter out words that start with a vowel (case-insensitive)
    filtered_words = filter(lambda word: word[0].lower() not in vowels, words)

    # Join the filtered words back into a sentence
    result = ' '.join(filtered_words)
    return result

# Example usage
input_sentence = "An elephant is outside the office waiting for us"
output_sentence = remove_vowel_words(input_sentence)
print("Original:", input_sentence)
print("Filtered:", output_sentence)
