def merge_sorted_arrays(numbers_list_1, m, numbers_list_2, n):
    # Pointers for the last valid elements in numbers_list_1 and numbers_list_2
    p1 = m - 1
    p2 = n - 1
    
    # Pointer for the last position in numbers_list_1
    p = m + n - 1
    
    # Merge in reverse order
    while p1 >= 0 and p2 >= 0:
        if numbers_list_1[p1] > numbers_list_2[p2]:
            numbers_list_1[p] = numbers_list_1[p1]
            p1 -= 1
        else:
            numbers_list_1[p] = numbers_list_2[p2]
            p2 -= 1
        p -= 1
        
    # If there are any remaining elements in numbers_list_2, add them
    numbers_list_1[:p2 + 1] = numbers_list_2[:p2 + 1]

if __name__ == "__main__":

    # Example Usage:
    #numbers_list_1 = [2, 4, 6, 0, 0, 0]
    numbers_list_1 = [2, 4, 6, 8, 11, 20]
    m = 6
    numbers_list_2 = [4, 5, 10]
    n = 3

    merge_sorted_arrays(numbers_list_1, m, numbers_list_2, n)
    print("Merged Array:", numbers_list_1)

