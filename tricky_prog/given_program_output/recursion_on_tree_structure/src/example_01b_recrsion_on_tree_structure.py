def count(child_dict, i):
    """
    Recursively counts the total number of nodes in the subtree
    rooted at node `i`.

    Raises:
        ValueError:
            If the node does not exist in the tree.
    """

    # Collect all valid nodes in the tree
    valid_nodes = set(child_dict.keys())

    for children in child_dict.values():
        valid_nodes.update(children)

    # Check whether node exists
    if i not in valid_nodes:
        raise ValueError(f"Node {i} does not exist in the tree")

    # Leaf node
    if i not in child_dict:
        return 1

    ans = 1

    for j in child_dict[i]:
        ans += count(child_dict, j)

    return ans

 # Issue:

"""
The above function recomputes all valid nodes during every recursive call.

That is inefficient.

A cleaner approach is:

- validate once before recursion
- use a helper recursive function internally

"""

if __name__ == "__main__":
    child_dict = dict()
    child_dict[0] = [1,2]
    child_dict[1] = [3,4,5]
    child_dict[2] = [6,7,8]
    print(count(child_dict,0))      # Output: 9
    print(count(child_dict,1))      # Output: 4
    print(count(child_dict,3))      # Output: 1

    # print(count(child_dict,9))      
    # Output: ValueError: Node 9 does not exist in the tree
