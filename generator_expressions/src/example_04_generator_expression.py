with open("huge.log") as f:
    error_count = sum(
        1
        for line in f
        if "ERROR" in line
    )

print(error_count)

# Advantages of generator 
# Reads lazily
# Constant memory
