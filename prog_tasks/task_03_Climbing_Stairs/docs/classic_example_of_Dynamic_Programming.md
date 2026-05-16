# Climbing Stairs program 

## Task 
---

### Write a Python program for the following "Climbing Stairs" scenario

You are climbing a staircase. It takes n steps to reach the top. 

Each time you can either climb 1 or 2 steps. 
In how many distinct ways can you climb to the top?

### Example 1:
Input: n = 2  
Output: 2  
Explanation:  
There are 2 ways to climb to the top
1. 1 step + 1 step  
2. 2 steps  

### Example 2:
Input: n = 3  
Output = 3  
Explanation:  
There are 3 ways to climb to the top
1. 1 step + 1 step + 1 step  
2. 1 step + 2 steps  
3. 2 steps + 1 step  

### Constraints

`1<= n <= 45`

---

### Dynamic Programming is used when a problem has:

- Overlapping Subproblems
- Optimal Substructure

--- 

This problem is a classic example of Dynamic Programming (DP)
It uses the same logic as the Fibonacci sequence

---

# Algorithm 

1. Start
2. Read value of n
3. If n <= 2:
       return n
4. Initialize:
       first = 1
       second = 2
5. Repeat from 3 to n:
       current = first + second
       first = second
       second = current
6. Return second
7. End

---

| Method       | Best For                      |
| ------------ | ----------------------------- |
| Recursion    | Learning recursion            |
| DP Array     | Understanding DP              |
| Optimized DP | Interviews & practical coding |
| Memoization  | Elegant Python solution       |
| Mathematical | Theory                        |

---
