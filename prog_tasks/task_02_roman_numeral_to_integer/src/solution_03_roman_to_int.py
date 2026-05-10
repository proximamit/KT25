import re

def roman_to_int(roman):
    # 1. Validation using Regex
    # This pattern ensures standard rules (no more than 3 Is, valid subtractions, etc.)
    pattern = r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
    
    # r'...' - r means raw string
    # ^ = start of string
    # $ = end of string
    # {0,3} = repeat 0 to 3 times
    # M{0,3} - Thousands Place

    # (CM|CD|D?C{0,3}) - Hundreds Place

    # (XC|XL|L?X{0,3}) - Tens Place

    # (IX|IV|V?I{0,3}) - Ones Place

    if not re.match(pattern, roman):
        return None  # Or raise a ValueError

    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    prev_value = 0

    # Traverse from right to left
    for char in reversed(roman):
        # Handle potential KeyError if invalid chars exist but passed regex
        value = roman_values.get(char, 0)

        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    return total

if __name__ == "__main__":
    # Test cases including invalid ones
    test_roman_numerals = ("MMMCMXCIX", "IIX", "VX", 
                           "IIII", "VV", "IC", "XCIX", "AZ", "XIV", "MCMXCIV", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "MMXXVI")
    
    for roman in test_roman_numerals:
        result = roman_to_int(roman)
        if result:
            print(f"Roman: {roman:10} | Integer: {result}")
        else:
            print(f"Roman: {roman:10} | Status: INVALID")