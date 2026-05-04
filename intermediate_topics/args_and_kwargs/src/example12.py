# Error Handling with Flexible Arguments

def safe_execute(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as e:
        return {"error": str(e)}

print(safe_execute(int, "123"))
print(safe_execute(int, "abc"))


