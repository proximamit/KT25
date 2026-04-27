# String Compression Program

---

Write a Python program to compress a sring.
Example 1 - Given an input word = "abcde", the output is "1a1b1c1d1e"

Example 2 - Give an input word = "aaaaabb", the output is "5a2b"

---

# Run-Length Encoding (RLE) String Compression

- Program which compresses a string by replacing consecutive repeating characters with their count followed by the character. 

- count consecutive characters and append the count followed by the character.
- traversing the string and counting consecutive occurrences of the same character.

---

# Approach

- Iterate through the string.
- Count consecutive repeating characters.
- When the character changes, store the count + previous character.

--- 

# Efficiency: 
Using a list to collect parts and then joining them with .join() is more efficient than repeated string concatenation, which creates a new string object in each step.

# Logic: 
The manual approach uses a while loop to scan ahead and find the end of each consecutive group before moving the pointer to the next new character

---

### How it works:
1.  **Initialize:** We start with a `count` of 1 and an empty list `compressed` to store our results. Using a list and `"".join()` is more memory-efficient than repeatedly adding to a string in Python.
2.  **The Loop:** We compare the current character `word[i]` with the previous one `word[i-1]`.
    * If they match, we increment the counter.
    * If they don't match, we've reached the end of a "run." We save the count and the character, then reset the counter to 1.
3.  **The Final Step:** Since the loop ends when it reaches the last character, the final character's count and value haven't been added yet. We append them manually after the loop finishes.

