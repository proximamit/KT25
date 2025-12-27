
# Take age input from the user
age = int(input("Enter your age: "))

if age < 13:
    print("Hello kid.")
elif age < 20:
    print("Hello teenager.", end=' ')
    if age < 18:
        years_to_wait = 18 - age
        print(f"You should wait for {years_to_wait} years to be eligible to vote")
    else:
        print("You are eligible to vote.")
else:
    print("You are an adult and eligible to vote")
