import re

text = "A black cat, a white rat, a catfish, a rattle snake, and a tomcat"

# Match the whole word "cat"
pattern1 = r"\bcat\b"
match1 = re.search(pattern1, text)
if match1:
    print(f"Found: {match1.group()}")       # Output: Found: cat
    matches1 = re.findall(pattern1, text)
    print(matches1)

# Match "rat" at the beginning of a word 
match2 = re.search(r"\brat", text)
if match2:
    print(f"Found: {match2.group()}")       # Output: Found: rat

# Match "fish" at the end of a word 
match3 = re.search(r"fish\b", text)
if match3:
    print(f"Found: {match3.group()}")       # Output: Found: fish
