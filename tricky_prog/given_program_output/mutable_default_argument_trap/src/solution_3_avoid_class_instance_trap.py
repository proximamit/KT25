class Cache:
    def __init__(self, data=None):
        self.data = {} if data is None else data

a = Cache()
b = Cache()

a.data["x"] = 1

print(b.data)       # Output: {}
