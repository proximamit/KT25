def int_to_roman(num):
    # Mapping of integer values to Roman symbols in descending order
    # Includes special subtractive cases like 4 (IV) and 900 (CM)
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    
    roman_num = ""
    i = 0
    while num > 0:
        # Determine how many times the symbol fits into the current number
        count = num // val[i]
        roman_num += syb[i] * count
        # Subtract the total value processed and move to the next smaller symbol
        num %= val[i]
        i += 1
        
    return roman_num

if __name__ == "__main__":
    # Example usage:
    #number = 1984
    #print(f"The Roman numeral for {number} is: {int_to_roman(number)}")
    # Output: MCMLXXXIV

    numbers = (1991, 1988, 2025, 4021)
    for number in numbers:
        print(f"The Roman numeral for {number} is: {int_to_roman(number)}")
