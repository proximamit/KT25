def int_to_roman(num):
    # Standard Roman Numerals only support 1 - 3,999
    if not (0 < num < 4000):
        return "Invalid Input (Must be between 1 and 3,999)"

    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    
    roman_num = ""
    for i in range(len(val)):
        while num >= val[i]:
            roman_num += syb[i]
            num -= val[i]
            
    return roman_num

if __name__ == "__main__":
    # Test with some numbers
    numbers = (1991, 1988, 2025, 4021)
    for number in numbers:
        print(f"{number}: {int_to_roman(number)}")
