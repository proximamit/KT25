# Consider the following Python code snippet.

A={"this","that"}
B={"that","other"}
C={"other","this"}

while "other" in C:
    if "this" in A:
        A,B,C=A-B,B-C,C-A
    if "that" in B:
        A,B,C=C|A,A|B,B|C

"""
When the above program is executed, at the end, which of the following sets
contains "this"?

(A)Only A
(B)Only B
(C)Only C
(D)A, C
"""

print("A:-", A)    # Output: A:- {'other'}
print("B:-", B)    # Output: B:- {'this'}
print("C:-", C)    # Output: C:- {'that'}
