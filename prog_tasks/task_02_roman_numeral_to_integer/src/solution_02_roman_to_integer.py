import re


class RomanNumeralError(ValueError):
    """Custom exception for invalid Roman numerals."""
    pass


class RomanNumeralConverter:
    """
    Utility class for converting Roman numerals to integers.
    Supports standard Roman numerals from 1 to 3999.
    """

    ROMAN_MAP = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    # Strict Roman numeral validation pattern
    VALID_ROMAN_PATTERN = re.compile(
        r"^M{0,3}"
        r"(CM|CD|D?C{0,3})"
        r"(XC|XL|L?X{0,3})"
        r"(IX|IV|V?I{0,3})$"
    )

    @classmethod
    def validate(cls, roman: str) -> None:
        """
        Validate whether the given string is a proper Roman numeral.

        Raises:
            RomanNumeralError: If invalid Roman numeral.
        """
        if not roman:
            raise RomanNumeralError("Roman numeral cannot be empty.")

        if not isinstance(roman, str):
            raise RomanNumeralError("Input must be a string.")

        roman = roman.upper()

        if not cls.VALID_ROMAN_PATTERN.fullmatch(roman):
            raise RomanNumeralError(
                f"Invalid Roman numeral: '{roman}'"
            )

    @classmethod
    def to_integer(cls, roman: str) -> int:
        """
        Convert a Roman numeral to an integer.

        Args:
            roman: Roman numeral string.

        Returns:
            Integer representation.

        Raises:
            RomanNumeralError: If input is invalid.
        """
        cls.validate(roman)

        roman = roman.upper()
        total = 0
        previous_value = 0

        for char in reversed(roman):
            current_value = cls.ROMAN_MAP[char]

            if current_value < previous_value:
                total -= current_value
            else:
                total += current_value

            previous_value = current_value

        return total


if __name__ == "__main__":
    """
    try:
        roman_input = input("Enter a Roman numeral: ").strip()
        result = RomanNumeralConverter.to_integer(roman_input)
        print(f"Integer value: {result}")

    except RomanNumeralError as error:
        print(f"Error: {error}")
    """
    

    test_roman_numerals = ("MMMCMXCIX", "IIII", "VV", "IC", "XM", "AZ")
    for roman_numeral in test_roman_numerals:
        try:
            print(f"Evaluating Roman Numeral {roman_numeral}")
            print("equivalent integer:", RomanNumeralConverter.to_integer(roman_numeral))
            print("\n")
        except RomanNumeralError as error:
            print(f"Error: {error}\n")

