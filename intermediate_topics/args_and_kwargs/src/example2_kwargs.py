def print_user(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_user(name="Stuart", age=30)
