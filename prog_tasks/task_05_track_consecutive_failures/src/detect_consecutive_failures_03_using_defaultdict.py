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


from collections import defaultdict

failure_counts = defaultdict(int)
alerts = set()

for device_id, status in results:
    if status:
        failure_counts[device_id] = 0
    else:
        failure_counts[device_id] += 1

        if failure_counts[device_id] == 3:
            alerts.add(device_id)

print(list(alerts))

'''
- defaultdict(int) automatically initializes counters to zero.
- No need for .get(device_id, 0).
- The == 3 check raises an alert exactly when the third consecutive failure occurs.
- A set avoids duplicate alerts.
'''
