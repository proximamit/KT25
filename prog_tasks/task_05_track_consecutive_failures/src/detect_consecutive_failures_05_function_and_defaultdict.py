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

def detect_consecutive_failures(results, threshold=3):
    failure_counts = defaultdict(int)
    alerts = set()

    for device_id, status in results:
        if status:
            failure_counts[device_id] = 0
        else:
            failure_counts[device_id] += 1

            if failure_counts[device_id] == threshold:
                alerts.add(device_id)

    return list(alerts)

alerts = detect_consecutive_failures(results)
print(alerts)
