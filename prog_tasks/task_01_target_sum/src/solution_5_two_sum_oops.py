class TwoSumSolver:

    def __init__(self):
        # A dictionary to store numbers we've already seen and their indices
        self.lookup = {}

    def solve(self, nums, target):

        for i, num in enumerate(nums):
            # Calculate the 'complement' needed to reach the target
            complement = target - num

            # Check if this complement was already recorded in our dictionary
            if complement in self.lookup:
                # If found, return the index of the complement 
                # and the current index
                return [self.lookup[complement], i]
            # If not found, store the current number and its index 
            # for future checks
            self.lookup[num] = i

if __name__ == "__main__":
    nums = [4, 9, 11, 15]
    target = 13
    
    # Initialize the solver and run it
    solver = TwoSumSolver()
    result = solver.solve(nums, target)
    
    # Output: [0, 1] (because nums[0] + nums[1] is 4 + 9 = 13)
    print(f"Result: {result}")