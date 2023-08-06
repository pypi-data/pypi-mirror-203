"""

This script provides an example of using the network_scanner utility to
scan 2 given subnets and look for devices that can only be accessed through
exactly one of the subnets.

"""

# Import the NetworkScanner class
from network_scanner_kbk import NetworkScanner

# Create an instance of the NetworkScanner class
ns = NetworkScanner()

# Provide 2 subnet addresses in CIDR /24 notation
subnet1 = "192.168.0.0/24"
subnet2 = "192.168.1.0/24"

# Select a list of devices/nodes to avoid pinging
ignore_list = [1, 100, 101, 102, 103]

# Call find_singularly_reachable_devices() to obtain the list of devices (ips)
devices = ns.find_singularly_reachable_devices(subnet1, subnet2,
                                               ignore_list=ignore_list)

print("List of devices accessible on exactly one subnet:")
for d in devices:
    print(d)

# This package comes with unit tests.  They can be run as follows.
