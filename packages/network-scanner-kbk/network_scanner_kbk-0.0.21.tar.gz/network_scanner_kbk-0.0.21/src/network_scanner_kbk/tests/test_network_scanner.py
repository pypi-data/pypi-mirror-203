#!/usr/bin/env python3
"""

Unit tests for the network_scanner class.

"""

from unittest import TestCase, main
from unittest.mock import patch
from io import StringIO


class TestNetworkScanner(TestCase):
    def __init__(self, *args):
        super(TestNetworkScanner, self).__init__(*args)
        self.nominal_subnet1 = "192.168.0.0/24"
        self.nominal_subnet2 = "192.168.1.0/24"
        self.ns_mock = None  # For tests that need the ping method mocked.

    def test_no_cidr(self):
        """ Test to verify CIDR substring is ignored. """
        ns = NetworkScanner()
        subnet2 = "192.168.0.0"  # No /24 CIDR
        try:
            ns.find_singularly_reachable_devices(self.nominal_subnet1, subnet2)
            self.assertTrue(False)  # Test fails if no exception is generated
        except ValueError:
            self.assertTrue(True)

    def test_invalid_ip_format(self):
        """ Test to verify invalid ip formats are rejected. """
        ns = NetworkScanner()
        subnet2 = "199.192.168.1.0/24"  # Invalid ip address
        try:
            ns.find_singularly_reachable_devices(self.nominal_subnet1, subnet2)
            self.assertTrue(False)  # Test fails if no exception is generated
        except ValueError:
            self.assertTrue(True)

    def test_invalid_retries(self):
        """ Test to check an invalid retries input. """
        ns = NetworkScanner()
        retries = 4  # Retries value too high
        try:
            ns.find_singularly_reachable_devices(self.nominal_subnet1,
                                                 self.nominal_subnet2,
                                                 retries=retries)
            self.assertTrue(False)  # Test fails if no exception is generated
        except ValueError:
            self.assertTrue(True)

    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_ignore_list(self, stdout):
        """ Test to verify the ignore_list works as expected. """
        self.ns_mock = NetworkScanner()
        self.ns_mock.ping = self.ping_mock  # Mock the ping method
        ignore_list = [254, 255, 300]  # 254 & 255 are valid, 256 is invalid
        self.ns_mock.find_singularly_reachable_devices(self.nominal_subnet1,
                                                       self.nominal_subnet2,
                                                       ignore_list=ignore_list)

        # Verify that a warning is provided for invalid value
        if "Invalid" in str(stdout.getvalue()):
            self.assertTrue(False)

        # Verify host_ids 254 & 255 are skipped resulting in 254 ping results.
        if len(self.ns_mock.ping_status[self.ns_mock.SUBNET1_IDX]) != 254:
            self.assertTrue(False)

    def test_nominal(self):
        """ Nominal test to verify the network scanner logic is working. """
        self.ns_mock = NetworkScanner()
        self.ns_mock.ping = self.ping_mock  # Mock the ping method
        # Over 80 characters to see if anyone at Joby notices
        ips = self.ns_mock.find_singularly_reachable_devices(self.nominal_subnet1,
                                                             self.nominal_subnet2)

        # Verify 10 ips were found that were reachable from exactly one subnet
        if len(ips) == 10:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def ping_mock(self, octet, subnet_idx, retries):
        """
        mock interface.  This method simulates subnet 1 having 10 devices:
             [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        and subnet 2 having 10 devices:
             [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        
        10 devices: [1, 2, 3, 4, 5, 11, 12, 13, 14, 15] are reachable from
        exactly one subnet.
        """
        # Subnet 1 devices
        if subnet_idx == self.ns_mock.SUBNET1_IDX and octet in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            reachable = True
        # Subnet 2 devices
        elif subnet_idx == self.ns_mock.SUBNET2_IDX and octet in [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]:
            reachable = True
        else:
            reachable = False
        self.ns_mock.ping_status[subnet_idx][octet] = reachable


if __name__ == '__main__':
    from network_scanner_kbk import NetworkScanner
    main()
