#  A classic example of recursion on a tree structure

# Purpose:- Recursively count the total number of nodes in a tree

"""
The tree is stored as a dictionary where:

- Key = parent node
- Value = list of child nodes

"""

def count(child_dict, i):
    # Assume any node not present as a parent is a leaf.
    if i not in child_dict.keys():
        return 1
    ans = 1
    for j in child_dict[i]:
        ans += count(child_dict, j)
    return ans
child_dict = dict()
child_dict[0] = [1,2]
child_dict[1] = [3,4,5]
child_dict[2] = [6,7,8]
print(count(child_dict,0))      # Output: 9
print(count(child_dict,1))      # Output: 4
print(count(child_dict,3))      # Output: 1

"""

a logical bug

node 9:

- is not a key
- is also not present anywhere in the tree

Yet the function treats it as a valid leaf node and returns 1
"""

print(count(child_dict,9))      # Output: 1

r'''
The dictionary creates this structure:


          0
        /   \
       1     2
     / | \  / | \
    3  4 5 6  7 8
'''

# A node that does not appear as a key is treated as a leaf node.

"""
Parameters:
        child_dict (dict):
            Dictionary representing parent-child relationships
            in the tree.

        i (int):
            The root node of the subtree to count.

    Returns:
        int:
            Total number of nodes in the subtree rooted at `i`,
            including the node itself.

"""

# Due to the assumption the function cannot distinguish between
# genuine leaves and non-existant nodes

'''
as
some nodes are genuine leaves
some nodes may not exist at all

'''
