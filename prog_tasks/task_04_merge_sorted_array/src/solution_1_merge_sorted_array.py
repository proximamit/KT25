def merge_sorted_arrays(numbers_list_1, m, numbers_list_2, n):
    # Create a result list
    merged_list = []

    # Pointers for both arrays
    i = 0
    j = 0

    # Merge elements in sorted order
    while i < m and j < n:
        if numbers_list_1[i] <= numbers_list_2[j]:
            merged_list.append(numbers_list_1[i])
            i += 1
        else:
            merged_list.append(numbers_list_2[j])
            j += 1

    # Add remaining elements from numbers_list_1
    while i < m:
        merged_list.append(numbers_list_1[i])
        i += 1

    # Add remaining elements from numbers_list_2
    while j < n:
        merged_list.append(numbers_list_2[j])
        j += 1

    return merged_list

if __name__ == "__main__":
    # Example usage
    numbers_list_1 = [2, 4, 6, 0, 0, 0]
    numbers_list_2 = [4, 5, 10]

    m = 3   # Number of valid elements in numbers_list_1
    n = 3   # Number of elements in numbers_list_2

    result = merge_sorted_arrays(numbers_list_1, m, numbers_list_2, n)

    print("Merged Sorted Array:", result)
