# Python program to 
# Take a URL as input from the user
# Fetch the URL
# Using regular expressions, search for phone numbers
# print the phone numbers found (if any)

import re
import requests

def extract_phone_numbers(text):
    # Regular expression to find phone numbers
    phone_pattern = re.compile(
        r'''
        (?:(?:\+?\d{1,3})?            # Optional country code
        [\s\-\.]?)?                   # Optional separator
        (?:\(?\d{2,4}\)?[\s\-\.]?)?   # Optional area code
        \d{3,4}[\s\-\.]?\d{3,4}       # Local number
        ''', 
        re.VERBOSE
    )
    return phone_pattern.findall(text)

# """
# The VERBOSE flag 

# re.VERBOSE flag allows us to write the regular expression over multiple lines and include 
# comments for readability
# 1. 
# (?:(?:\+?\d{1,3})?            # Optional country code

# (?:...): A non-capturing group, meaning it groups the pattern but does not capture it for back-referencing.

# \+?: An optional + symbol. The + is escaped with \ because it's a special regex character.

# \d{1,3} : Matches 1 to 3 digits 
# this represents the country code, e.g., +1, +91, etc.
# """

# '''
# 2. [\s\-\.]?     # Optional separator

#  A character class that matches a single separator character:

#    \s: Any whitespace (like space or tab)
#    \-: A literal dash - (escaped to avoid interpretation as range)
#    \.: A literal dot .
#  ?: Makes this separator optional.
#  This allows for separators like space, dash, or dot between number components, such as:

#    +91 1234 5678
#    +91-1234-5678
#    +91.1234.5678
# '''

# """
# 3. (?:\(?\d{2,4}\)?[\s\-\.]?)?      # Optional area code

# This part matches the area code.

#  \(?: Optional opening parenthesis ( (escaped)
#  \d{2,4}: 2 to 4 digits (area codes vary in length)
#  \)?: Optional closing parenthesis )
#  [\s\-\.]?: Optional separator after area code
#  Entire group is optional: (?: ... )?

# Examples matched:

#  (040)
#  040
#  040-
#  (040) 

# """

# '''
# 4. \d{3,4}[\s\-\.]?\d{3,4}          # Local number

# This is the core of the phone number the local number part.

#  \d{3,4}: First part 3 or 4 digits
#  [\s\-\.]?: Optional separator
#  \d{3,4}: Second part 3 or 4 digits

#  Examples matched:

#  1234567
#  123-4567
#  1234 5678
#  123.4567

# '''


def main():
    url = input("Enter the full URL of the page : ").strip()

    try:
        print(f"\nFetching page: {url}")
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        html_content = response.text

        phone_numbers = extract_phone_numbers(html_content)
        if phone_numbers:
            print("\nPhone numbers found:")
            for number in sorted(set(n.strip() for n in phone_numbers if n.strip())):
                print(number)
        else:
            print("\nNo phone numbers found.")
    except requests.RequestException as e:
        print(f"\nError fetching the webpage: {e}")

if __name__ == "__main__":
    main()