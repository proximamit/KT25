import keyword
number_of_keywords = len(keyword.kwlist)
print(f"There are {number_of_keywords} keywords in Python.")
for index, word in enumerate(keyword.kwlist):
    print(f"{index + 1}.", word)