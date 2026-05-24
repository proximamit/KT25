call_count = 0

def mystery(n, depth=0):
    global call_count

    # Count stack activation
    call_count += 1

    indent = "  " * depth

    print(indent + f"Entering mystery({n})")

    # Base case
    if n <= 0:
        print(indent + f"Base case reached in mystery({n}), returning 1")
        return 1

    # First recursive call
    print(indent + f"1. --> Calling mystery({n-1}) from mystery({n})")
    left = mystery(n - 1, depth + 1)

    # Second recursive call
    print(indent + f"2. --> Calling mystery({n-2}) from mystery({n})")
    right = mystery(n - 2, depth + 1)

    result = left + right

    print(indent + f"Returning {result} from mystery({n})")

    return result


answer = mystery(4)

print("\nFinal Answer:", answer)
print("Total Stack Activations:", call_count)
