# Example: Print numbers from 1 to 20, but skip 3 and multiples of 3
for i in range(1, 21):
    if i % 3 == 0:
        #pass
        print("Laddu")  # Skip 3 and multiples of 3
        # Skip the iteration if i is divisible by 3
        continue  # Example of continue statement 
    print(i)

