# Consider the following Python code snippet.

A={"this","that"}
B={"that","other"}
C={"other","this"}

print(type(A))
print("\n\n\tInitial values:")
print("A:-", A)
print("B:-", B)
print("C:-", C)
print("\n\n")
count = 0
while "other" in C:
    count += 1
    print(f"--- {count} ---")
    if "this" in A:
        A,B,C=A-B,B-C,C-A
    if "that" in B:
        A,B,C=C|A,A|B,B|C
    print("A:-", A)
    print("B:-", B)
    print("C:-", C)
print("\n\n\tOutput:")
print("A:-", A)    # Output: A:- {'other'}
print("B:-", B)    # Output: B:- {'this'}
print("C:-", C)    # Output: C:- {'that'}

"""
When the above program is executed, at the end, which of the following sets
contains "this"?

(A)Only A
(B)Only B
(C)Only C
(D)A, C
"""
