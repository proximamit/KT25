def fun(L, i=0):
    if i >= len(L)-1:
        return 0
    if L[i] > L[i+1]:
        L[i+1], L[i] = L[i], L[i+1]
        return 1+fun(L, i+1)
    else:
        return fun(L, i+1)

if __name__ == "__main__":
    data = [5, 3, 4, 1, 2] 
    count = 0 
    for _ in range(len(data)): 
        count += fun(data) 
    # Print sum of swaps from all iterations of Bubble Sort
    print(count)    # Output: 8
