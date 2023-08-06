# network_scanner_kbk
Project to impliment a network scanner for comparing subnets

# Example Usage

Example of using the network_scanner utility to scan 2 given subnets and look
for devices that can only be accessed through exactly one of the subnets.

```
# Import the NetworkScanner class
from network_scanner_kbk import NetworkScanner

# Create an instance of the NetworkScanner class
ns = NetworkScanner()

# Provide 2 subnet addresses in CIDR /24 notation
subnet1 = "192.168.0.0/24"
subnet2 = "192.168.1.0/24"

# Call find_singularly_reachable_devices() to obtain the list of devices (ips)
devices = ns.find_singularly_reachable_devices(subnet1, subnet2)

print("List of devices accessible on exactly one subnet:")
for d in devices:
    print(d)
```

This package comes with unit tests.  They can be run as follows:
```
cd network_scanner_kbk/tests
python test_network_scanner.py
```
