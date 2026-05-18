def merge_sorted_arrays(numbers_list_1, m, numbers_list_2, n):
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1

    while p1 >= 0 and p2 >= 0:
        if numbers_list_1[p1] > numbers_list_2[p2]:
            numbers_list_1[p] = numbers_list_1[p1]
            p1 -= 1
        else:
            numbers_list_1[p] = numbers_list_2[p2]
            p2 -= 1
        p -= 1

    # Copy remaining elements from numbers_list_2
    while p2 >= 0:
        numbers_list_1[p] = numbers_list_2[p2]
        p2 -= 1
        p -= 1


if __name__ == "__main__":

    numbers_list_1 = [2, 4, 6, 8, 11, 20, 0, 0, 0]
    m = 6

    numbers_list_2 = [4, 5, 10]
    n = 3

    merge_sorted_arrays(numbers_list_1, m, numbers_list_2, n)

    print("Merged Array:", numbers_list_1)