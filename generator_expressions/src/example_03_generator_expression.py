# a concise way to find a specific item in a list of dictionaries

#  a list containing three dictionaries, 
# each representing a user with an id and a name

users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"},
]

# Generator
# loop through the list looking for a dictionary where the id is 2
# The next() function grabs the first item that satisfies the condition

# If the code looks through the whole list and doesn't find id == 2, 
# it will return None instead of crashing with an error
user = next((u for u in users if u["id"] == 2), None)

print(user)

# Advantage of using generator
# Stops immediately after first match
# No intermediate list

# next((x for x in items if cond(x)), default)
