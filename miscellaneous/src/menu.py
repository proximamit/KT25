choices = {1: "Start", 2: "Edit", 3: "Quit"}

for key, value in choices.items():
    print("Press ", key, "to ", value )

user_input = int(input("Enter a number from 1 to 3: "))
if user_input in choices.keys():
    print("You chose", choices[user_input])
else:
    print("Unknown choice")