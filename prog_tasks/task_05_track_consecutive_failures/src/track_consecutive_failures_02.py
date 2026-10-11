results = [
    ("node_01", True),
    ("node_01", False),
    ("node_01", False),
    ("node_01", False),
    ("node_02", False),
    ("node_02", True),
    ("node_03", False),
    ("node_03", False),
    ("node_03", False),
    ("node_03", False),
]

alert_nodes = set()
consecutive_failures = 0
prev_node = None

for node, success in results:
    # Reset count if we switch to a new node
    if node != prev_node:
        consecutive_failures = 0
        prev_node = node
    
    # Track failures
    if not success:
        consecutive_failures += 1
        if consecutive_failures >= 3:
            alert_nodes.add(node)
    else:
        consecutive_failures = 0

# Convert set to list to match expected output format
output = list(alert_nodes)
print(output)
