data = [
    ("Alice", 24, 4500.50),
    ("Bob", 30, 12000.00),
    ("Charlie", 19, 850.75)
]

# Print table headers
print(f"{'Name':<12} {'Age':^6} {'Balance':>12}")
print("-" * 32)

# Print rows
for name, age, balance in data:
    print(f"{name:<12} {age:^6} {balance:>12,.2f}")
