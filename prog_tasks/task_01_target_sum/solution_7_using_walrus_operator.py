#  Using Walrus Operator (:=) to calculate the difference and 
# assign it to a variable inside the if statement simultaneously

def two_sum(nums, target):
    # create an empty dictionary to store numbers as keys and 
    # their positions (indices) as values.
    seen = {}

    # iterate through the list nums, keeping track of the current number (num) 
    # and its index (i)
    for i, num in enumerate(nums):
        # For every number, calculate the "complement" — 
        # the exact value needed to reach the target 
        if (diff := target - num) in seen:
            # If that complement is already in the dictionary, it means we found
            #  the pair! It returns the index of the complement and 
            # the current index
            return [seen[diff], i]
        # If not, it adds the current number and its index to the dictionary 
        # and moves to the next one
        seen[num] = i

if __name__ == "__main__":
    nums = [5, 4, 8, 1]
    target = 12
    print(two_sum(nums, target))  # Output: [1, 2]

"""
Example Walkthrough 
(nums: [5, 4, 8, 1], target: 12):

Step 1: Is 12 - 5 (7) in seen? No. Add {5: 0}.
Step 2: Is 12 - 4 (8) in seen? No. Add {5: 0, 4: 1}.
Step 3: Is 12 - 8 (4) in seen? Yes! (4 was stored at index 1).
Result: It returns [1, 2]
"""

