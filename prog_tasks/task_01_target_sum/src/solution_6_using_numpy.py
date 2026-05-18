import numpy as np

def two_sum(nums, target):
    nums = np.array(nums)

    for i, num in enumerate(nums):
        complement = target - num

        indices = np.where(nums[i+1:] == complement)[0]

        if len(indices):
            return [i, indices[0] + i + 1]
        
if __name__ == "__main__":
    nums = [5, 4, 8, 1]
    target = 12
    print(two_sum(nums, target)) 