def count(child_dict, i):
    """
    Count total nodes in the subtree rooted at node `i`.

    Raises:
        ValueError:
            If node `i` does not exist in the tree.
    """

    # Build set of all nodes
    valid_nodes = set(child_dict.keys())
    #print("Set of valid nodes: ", valid_nodes)

    for children in child_dict.values():
        valid_nodes.update(children)

    # Validate input node
    if i not in valid_nodes:
        raise ValueError(f"Node {i} does not exist in the tree")

    # Internal recursive helper
    def _count(node):
        if node not in child_dict:
            return 1

        ans = 1

        for child in child_dict[node]:
            ans += _count(child)

        return ans

    return _count(i)

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