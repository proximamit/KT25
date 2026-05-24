call_counter = 0

def f(a, b):
    global call_counter

    # Increase call count
    call_counter += 1
    current_call = call_counter

    # Print current function call details
    print(f"\nCall {current_call}: f(a={a}, b={b})")

    # Base case
    if a == 0:
        print(f"Call {current_call}: a == 0, returning {b}")
        return b

    # Odd case
    if a % 2 == 1:
        # If `a` is odd:

        # subtract 1
        # divide by 2
        # recursively call `f`
        # multiply result by 2

        print(f"Call {current_call}: {a} is odd")
        print(f"Call {current_call}: calling f(({a}-1)/2, {b}) = f({(a-1)//2}, {b})")

        result = 2 * f((a - 1) // 2, b)

        print(f"Call {current_call}: returned value after multiplying by 2 = {result}")
        return result

    # Even case
    print(f"Call {current_call}: {a} is even")
    print(f"Call {current_call}: calling f({a-1}, {b})")
    # If `a` is even:

    # add `b`
    # recursively call with `a-1`
    result = b + f(a - 1, b)

    print(f"Call {current_call}: returned value after adding b ({b}) = {result}")
    return result


# Driver code
answer = f(15, 10)

print("\nFinal Answer =", answer)