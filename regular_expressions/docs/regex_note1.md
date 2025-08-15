# Regular Expressions 

- We need to `import re` for regular expressions

> A **regular expression** is a sequence of characters that defines a search pattern  

These patterns can be used to:

* Find specific text (e.g., email addresses, phone numbers)
* Validate input (e.g., ensure a password meets complexity rules)
* Replace text within a string
* Split strings into parts

## Notes:
- It is a common practice to use raw strings (like r"\bcat\b") for regular expressions in Python

### The Dot Regex
The dot(.) is a metacharacter that matches any character except a newline(\n) by default.

### Word Boundary (\b)
The metacharacter `\b` represents a word boundary
