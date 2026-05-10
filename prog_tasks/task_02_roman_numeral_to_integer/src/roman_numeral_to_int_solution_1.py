def roman_to_int(roman):
    # Dictionary to store Roman numeral values
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    # Traverse the Roman numeral from right to left
    for char in reversed(roman):
        value = roman_values[char]

        # If current value is smaller than previous, subtract it
        if value < prev_value:
            total -= value
        else:
            total += value

        prev_value = value

    return total

if __name__ == "__main__":
    # Example usage
    #roman_numeral = input("Enter a Roman numeral: ").upper()
    #print("Integer value:", roman_to_int(roman_numeral))

    # test_roman_numerals = ("MMMCMXCIX", "IIII", "VV", "IC", "XM", "AZ")
    test_roman_numerals = ("MMMCMXCIX", "IIII", "VV", "IC", "XM")
    for roman_numeral in test_roman_numerals:
        print(f"For Roman Numeral {roman_numeral}")
        print("equivalent integer value:", roman_to_int(roman_numeral))
        print("\n")
