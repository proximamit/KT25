# Regular Expressions 

- Regular expressions, are also known as ***regex***
- We need to `import re` for regular expressions
- All the regex functions in Python are in the `re` module

> **Regular Expressions** are descriptions for a pattern of text
---
> A **regular expression** is a sequence of characters that defines a search pattern  

These patterns can be used to:

* Find specific text (e.g., email addresses, phone numbers)
* Validate input (e.g., ensure a password meets complexity rules)
* Replace text within a string
* Split strings into parts

## Notes:
- It is a common practice to use raw strings (like r"\bcat\b") for regular expressions in Python, since regular expressions frequently use backslashes in the pattern.
- By putting an `r` before the first quote of the string, we can mark the string as a raw string, which does not escape characters

### The Dot Regex
The dot(.) is a metacharacter that matches any character except a newline(\n) by default.

### Word Boundary (\b)
The metacharacter `\b` represents a word boundary
