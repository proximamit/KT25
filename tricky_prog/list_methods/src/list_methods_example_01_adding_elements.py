# Python 3.10 or above

import sys

list_method_question = """

Consider the following Python declarations of two lists.
A=[1,2,3]
B=[4,5,6]
Which one of the following statements results in A = [1, 2, 3, 4, 5, 6]?

Options:

(A) A.extend(B)
(B) A.append(B)
(C) A.update(B)
(D) A.insert(B)

"""
print(list_method_question)

A=[1,2,3]
B=[4,5,6]

# Get user input
choice = input("Enter your choice (A, B, C, or D): ").upper()
match choice:
    case 'A':
        A.extend(B)
    case 'B':
        A.append(B)
    case 'C':
        # AttributeError: 'list' object has no attribute 'update'
        A.update(B)
    case 'D':
        # TypeError: insert expected 2 arguments, got 1
        A.insert(B)
    # The underscore acts as the 'default' or catch-all case
    case _:
        print("Invalid choice.")
        sys.exit(1)
print(A)
