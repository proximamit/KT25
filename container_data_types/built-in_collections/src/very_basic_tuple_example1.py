"""
with tuples, we can
- Iterate over them
- Use slicing
- Concatenate or repeat
- Count and find index of items
- Nest them
- Use them as dictionary keys or in sets

"""
# Simple tuple
tuple1 = (1, 2, 3)
print(tuple1)                   # Output : (1, 2, 3)

# tuple with mixed data types
tuple2 = (1, 'hello', 3.5, True)
print(tuple2)                   # Output : (1, 'hello', 3.5, True)

# Nested tuple
tuple3 = (1, (2, 3), [4, 5])
print(tuple3)                   # Output : (1, (2, 3), [4, 5])

# tuple without parentheses
tuple4 = 1, 2, 3, 4
print(type(tuple4), tuple4)     # Output : <class 'tuple'> (1, 2, 3, 4)

# Single element tuple
tuple5 = (5, )
test = (5)
print(type(tuple5), tuple5)     # Output : <class 'tuple'> (5,)
print(type(test), test)         # Output : <class 'int'> 5

## Accessing tuple elements
my_tuple = ('a', 'b', 'c', 'd', 'e')
print(my_tuple[0])              # Output : a
print(my_tuple[-1])             # Output : e
print(my_tuple[1:4])             # Output : ('b', 'c', 'd')

## Iterating over a tuple
tuple6 = (10, 20, 30)
for num in tuple6:
    print(num)

### Tuple Operations

tuple7 = (1, 2)
tuple8 = (99, 100)
## Concatenation
tuple9 = tuple7 + tuple8
print(tuple9)                   # Output : (1, 2, 99, 100)

# Repetition
print(tuple7 * 3)               # Output : (1, 2, 1, 2, 1, 2)

# Membership
tuple10 = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
print('c' in tuple10)           # Output : True
print('h' not in tuple10)       # Output : True
print('z'in tuple10)            # Output : False

## Tuple methods
# Tuple have only 2 methods

# count(value) - Returns the number of times a value appears
tuple11 = (1, 1, 2, 2, 2, 4, 4, 4, 4)
print("Count =", tuple11.count(2))         # Output : Count = 3

# index(value) -  Returns the first index of a value
print ("Index =", tuple9.index(99))         # Output : Index = 2


### tuple packing
tuple12 = 11, 22, 33
print(tuple12)                              # Output : (11, 22, 33)

### tuple unpacking
a, b, c = tuple12
for item in tuple12:
    print(item)

## extended packing
tuple13 = (11, 22, 33, 44, 55)
x, *y, z = tuple13
print("x =", x)                         # Output : x = 11
print("y =", y)                         # Output : y = [22, 33, 44]
print("z =", z)                         # Output : z = 55


## Swapping variables

a = 100
b = 200
print(a, b)                             # Output : 100 200
a, b = b, a 
print(a, b)                             # Output : 200 100

# Returning multiple values from functions

def min_max(nums):
    return min(nums), max(nums)

result = min_max([100, 50, 25, 200, 20, 40])
print(type(result), result)             # Output : <class 'tuple'> (20, 200)

### Tuples are immutable, 
### but if they contain MUTABLE elements like lists,
### those can be modified

tuple_with_nested_list = (11, [22, 33], 55)
print(tuple_with_nested_list)           # Output : (11, [22, 33], 55)
tuple_with_nested_list[1].append(44)
print(tuple_with_nested_list)           # Output : (11, [22, 33, 44], 55)

days = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
weekdays = days[1:-1]
print(weekdays)      # Output : ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')

# Example of using tuple as keys of dictionary
employee_records = {
    (101, "Sales"): {"name": "Alice", "position": "Sales Manager", "salary": 75000},
    (102, "HR"): {"name": "Bob", "position": "HR Specialist", "salary": 65000},
    (103, "IT"): {"name": "Charlie", "position": "Developer", "salary": 80000},
    (101, "IT"): {"name": "Alice", "position": "Project Lead", "salary": 85000}  # Same ID, different dept
}

print(type(employee_records))
# Access record of employee with ID 101 in the IT department
employee101 = employee_records[(101, "IT")]
print(type(employee101))
print(employee101["name"])       # Output: Alice
print(employee101["position"])   # Output: Project Lead

my_tuple = (10, 20, 30)
values = ["Ten", "Twenty", "Thirty"]

my_dict = {}

for key, value in zip(my_tuple, values):
    my_dict[key] = value

print(my_dict)
# Output: {10: 'Ten', 20: 'Twenty', 30: 'Thirty'}
