class Cache:
    def __init__(self, data={}):
        self.data = data

a = Cache()
b = Cache()

a.data["x"] = 1

print(b.data)       # Output: {'x': 1}
