def universal_logger(*args, **kwargs):
    print(f"Positional: {args}") # A tuple
    print(f"Keyword: {kwargs}")   # A dictionary

universal_logger(1, 2, 3, site="https://www.wikipedia.org/", status=200)
# Output:
# Positional: (1, 2, 3)
# Keyword: {'site': 'https://www.wikipedia.org/', 'status': 200}
