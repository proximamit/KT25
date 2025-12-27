# Example: Print numbers from 1 to 10, but stop when we reach 5
for i in range(1, 11):
    if i == 5:
        print("Breaking the loop at i =", i)
        break  # Exit the loop when i equals 5
    print(i)

