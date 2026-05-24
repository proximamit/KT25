"""
Program to demonstrate classic inefficiency of naive recursion:

- repeated work
- exponential growth in calls

and show why:

- recursion can become slow
- memoization/dynamic programming are often used
"""


call_count = 0

def mystery(n, depth=0):
    global call_count

    # Count this function activation
    call_count += 1

    print("  " * depth + f"Entering mystery({n})")

    if n <= 0:
        print("  " * depth + f"Returning 1 from mystery({n})")
        return 1

    result = mystery(n - 1, depth + 1) + mystery(n - 2, depth + 1)

    print("  " * depth + f"Returning {result} from mystery({n})")

    return result


answer = mystery(4)

print("\nFinal Answer:", answer)
print("Total Stack Activations (Function Calls):", call_count)
