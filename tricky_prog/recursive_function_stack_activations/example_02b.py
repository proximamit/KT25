call_counter = 0   # Counts total function calls (stack activations)

def f(a, b):
    global call_counter

    # Increment stack activation count
    call_counter += 1
    current_call = call_counter

    print(f"\n--- Stack Activation #{current_call} ---")
    print(f"Entering: f(a={a}, b={b})")

    # Base case
    if a == 0:
        print(f"Call {current_call}: Base case reached")
        print(f"Call {current_call}: Returning {b}")
        return b

    # Odd case
    if a % 2 == 1:
        print(f"Call {current_call}: {a} is ODD")

        next_a = (a - 1) // 2

        print(f"Call {current_call}: Next recursive call -> f({next_a}, {b})")

        result = 2 * f(next_a, b)

        print(f"Call {current_call}: After recursion")
        print(f"Call {current_call}: Returning 2 * child_result = {result}")

        return result

    # Even case
    print(f"Call {current_call}: {a} is EVEN")

    print(f"Call {current_call}: Next recursive call -> f({a-1}, {b})")

    result = b + f(a - 1, b)

    print(f"Call {current_call}: After recursion")
    print(f"Call {current_call}: Returning b + child_result = {result}")

    return result


# Driver Code
answer = f(15, 10)

print("\n==============================")
print("Final Answer =", answer)
print("Total Stack Activations =", call_counter)
print("==============================")
