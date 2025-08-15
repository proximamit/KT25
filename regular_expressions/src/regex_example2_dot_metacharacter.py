import re

text = "cute cake cat cricket car cable care cut candle cctv"

# using . (dot) metacharacter to match any single character between c and t 
matches1 = re.findall(r"c.t", text)

# 
matches2 = re.findall(r"\bc.t\b", text)
print(matches1)         # Output: ['cut', 'cat', 'cut', 'cct']
print(matches2)         # Output: ['cat', 'cut']
