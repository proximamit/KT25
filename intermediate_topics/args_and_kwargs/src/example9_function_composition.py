# Function Composition / Pipelines

def pipeline(data, *functions):
    for func in functions:
        data = func(data)
    return data

def double(x): return x * 2
def square(x): return x ** 2

print(pipeline(3, double, square))  # (3*2)^2 = 36
