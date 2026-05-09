def two_sum(nums, target):
    # Use a dictionary 'seen' to store numbers and their indices
    seen = {}  # stores number -> index

    # For each number, calculate the 'complement = target - num'
    for i, num in enumerate(nums):
        complement = target - num

        # Check if complement already exists in the dictionary
        if complement in seen:
            # If yes, return the two indices
            return [seen[complement], i]

        # Otherwise, store current number with its index
        seen[num] = i

def print_two_sum_output(nums_list, target_sum, output_indices):
    print(f"\nGiven list of integers {nums_list} and the target {target_sum}")
    print("The indices of the two integers whose sum leads to target \n ")
    print(f"{output_indices}")

if __name__ == "__main__":
    # Example 1
    nums1 = [4, 9, 11, 15]
    target1 = 13
    output1 = two_sum(nums1, target1)
    print_two_sum_output(nums1, target1, output1) # Output: [0, 1]

    # Example 2
    nums2 = [5, 4, 8, 1]
    target2 = 12
    output2 = two_sum(nums2, target2)
    print_two_sum_output(nums2, target2, output2) # Output: [1, 2]

    # Example 3
    nums3 = [1, 2, 5, 5]
    target3 = 10
    output3 = two_sum(nums3, target3)
    print_two_sum_output(nums3, target3, output3) # Output: [2, 3]
