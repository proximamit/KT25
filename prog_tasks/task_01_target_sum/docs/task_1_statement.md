# Two Sum

Python program to solve the "Two Sum" problem: 
Finding the indices of two numbers in a list that add up to a specific target.

Given an array of integers `nums` and an integer `target`, return indices of the
two numbers such that they add up to `target`

### Assumption

Assume that each input would have ***exactly one solution***, and we may not 
use same element twice

### Example 1

Input:

```python
nums = [4, 9, 11, 15]
target = 13
```

Output:
```
[0, 1]
```

Because nums[0] + nums[1] == 13, we return [0, 1]

### Example 2

Input:

```python
nums = [5, 4, 8, 1]
target = 12
```

Output:
```
[1, 2]
```

### Example 3

Input:

```python
nums = [1, 2, 5, 5]
target = 10
```

Output:
```
[2, 3]
```
