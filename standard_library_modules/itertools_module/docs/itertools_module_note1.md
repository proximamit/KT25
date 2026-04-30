# Itertools Module

The Python itertools module provides memory-efficient, fast iterator building blocks for handling complex looping, permutations, combinations, and data grouping

- it provides a set of fast and memory efficient tools 
- Key Functions
    - combinations
    - permutations
    - groupby
    - chain
- Memory Efficiency: itertools functions return generators (lazy evaluation), which are crucial when dealing with massive datasets.
- Itertype module provides shortcut tools, and may not always be the optimal solution

---
# Caveats
- Permutations vs. Combinations: We need to always clarify if order matters (permutation) or not (combination).
- groupby requires sorting: groupby only groups consecutive items. We need to always sort the input data first if we want to group all identical items.
- Replacement: We need to use combinations_with_replacement when items can be reused

---

# Summary

| Problem Type      | Function       |
| ----------------- | -------------- |
| Cartesian product | `product`      |
| Permutations      | `permutations` |
| Combinations      | `combinations` |
| Running sum       | `accumulate`   |
| Flatten list      | `chain`        |
| Group elements    | `groupby`      |

---