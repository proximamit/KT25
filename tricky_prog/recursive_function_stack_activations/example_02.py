#Consider the following Python code snippet.

def f(a,b):
    if (a==0):
        return b
    if (a%2==1):
        return 2*f((a-1)/2,b)
    return b+f(a-1,b)
print(f(15,10))         # Output: 160

"""
The value printed by the code snippet is

(Answer in integer)
"""
