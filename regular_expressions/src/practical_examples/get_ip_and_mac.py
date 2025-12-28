import subprocess
import re

def get_interface_info(interface_name):
    try:
        # Run ifconfig for the given interface
        result = subprocess.check_output(
            ["ifconfig", interface_name],
            stderr=subprocess.DEVNULL,
            text=True
        )
    except subprocess.CalledProcessError:
        print(f"{interface_name}: Interface not found")
        return

    # Regex patterns
    ipv4_pattern = r'inet (?:addr:)?(\d+\.\d+\.\d+\.\d+)'
    mac_pattern = r'(?:ether|HWaddr)\s([0-9a-fA-F:]{17})'

    ipv4_match = re.search(ipv4_pattern, result)
    mac_match = re.search(mac_pattern, result)

    ipv4 = ipv4_match.group(1) if ipv4_match else "Not found"
    mac = mac_match.group(1) if mac_match else "Not found"

    print(f"Interface: {interface_name}")
    print(f"  IPv4 Address: {ipv4}")
    print(f"  MAC Address:  {mac}")
    print("-" * 30)


# Interfaces to check
interfaces = ["eth0", "wlan0"]

for iface in interfaces:
    get_interface_info(iface)
