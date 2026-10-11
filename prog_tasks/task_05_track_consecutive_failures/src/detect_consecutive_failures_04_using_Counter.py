# Detect consecutive failures

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


from collections import Counter

failure_counts = Counter()
alerts = set()

for device_id, status in results:
    if status:
        failure_counts[device_id] = 0
    else:
        failure_counts[device_id] += 1

        if failure_counts[device_id] == 3:
            alerts.add(device_id)

print(list(alerts))
