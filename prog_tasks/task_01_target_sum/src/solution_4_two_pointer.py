def two_sum(nums, target):
    arr = sorted(enumerate(nums), key=lambda x: x[1])

    left, right = 0, len(arr) - 1

    while left < right:
        curr_sum = arr[left][1] + arr[right][1]

        if curr_sum == target:
            return [arr[left][0], arr[right][0]]

        elif curr_sum < target:
            left += 1
        else:
            right -= 1

if __name__ == "__main__":
    nums = [5, 4, 8, 1]
    target = 12
    print(two_sum(nums, target))