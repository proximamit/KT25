import keyword

#print(keyword.kwlist)
#print(keyword.softkwlist)

number_of_keywords = len(keyword.kwlist)
print(f"There are {number_of_keywords} keywords in Python.")
for index, word in enumerate(keyword.kwlist):
    print(f"{index + 1}.", word)

print(f"\nIn Addition, there are {len(keyword.softkwlist)} Soft Keywords")
for soft_keyword in keyword.softkwlist:
    print(soft_keyword)

