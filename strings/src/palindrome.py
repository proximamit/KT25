# Function to check if a string is palindrome
def is_palindrome(str):
    # return str == str[::-1]
    return str.replace(" ", "").lower() == str[::-1].replace(" ", "").lower()

# List of words to test 
words = ['pop', 'Noon', 'Level', 'Madam', 'hello', 'racecar', 'Python', 'radar', 'Kayak', 'Rotator', 'Hannah' ]

sentences =["Never odd or even",
            "No lemon, no melon",
            "Was it a car or a cat I saw"]

# Check each word
for word in words + sentences:
    if is_palindrome(word):
        print(f"{word} is a palindrome")
    else:
        print(f"{word} is not a palindrome")
