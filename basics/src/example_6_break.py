import datetime

# Example: Print numbers from 1 to 10, but stop when we reach 5
for i in range(1, 11):
    if i == 5:
        print("Breaking the loop at i =", i)
        break  # Exit the loop when i equals 5
    print(i)



# Get today's actual date
today = datetime.date.today()
today_day = today.day

print("Guess today's date (day of the month)!")

# Infinite Loop
while True:
    try:
        # Ask the user for their guess
        guess = int(input("Enter a number from 1 to 31: "))

        # Check if the guess is within a valid range for a day
        if not (1 <= guess <= 31):
            print("Please enter a number between 1 and 31.")
            continue

        # Check if the guess is correct
        if guess == today_day:
            print(f"Correct! Today's date is indeed {today_day}.")
            break  # Exit the loop if the guess is correct
        else:
            print("Incorrect guess. Try again.")
            # The loop continues automatically to the next iteration

    except ValueError:
        # Handle cases where the user inputs something that is not an integer
        print("Invalid input. Please enter a whole number.")

print("Thank You.")
