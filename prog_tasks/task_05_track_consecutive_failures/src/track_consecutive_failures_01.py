# Task - Track Consecutive Failures

"""
if 3 or more consecutive failures are detected then raise alert 

"""


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

# Expected output:
# [node_01, node_03]

failure_counts = {}
alerted_devices = set()

for device_id, status in results:
    if status is False:
        failure_counts[device_id] = failure_counts.get(device_id, 0) + 1

        if failure_counts[device_id] >= 3:
            alerted_devices.add(device_id)
    else:
        failure_counts[device_id] = 0

alerts = list(alerted_devices)

print(alerts)
