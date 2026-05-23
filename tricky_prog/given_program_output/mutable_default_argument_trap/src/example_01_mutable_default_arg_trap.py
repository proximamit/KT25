
#  mutable default argument trap.

def append_to_lst(val, lst=[]):
    #print(id(lst))
    lst.append(val)
    return lst
print(append_to_lst(1))         # Output: [1]
print(append_to_lst(2))         # Output: [1, 2]
print(append_to_lst(3, []))     # Output: [3]
print(append_to_lst(4))         # Output: [1, 2, 4]
print(append_to_lst(5, []))     # Output: [5]
