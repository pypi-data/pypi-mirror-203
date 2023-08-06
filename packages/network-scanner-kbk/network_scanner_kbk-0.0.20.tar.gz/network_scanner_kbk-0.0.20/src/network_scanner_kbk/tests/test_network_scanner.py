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

    def test_no_cidr(self):
        ns = NetworkScanner()
        subnet2 = "192.168.0.0"  # No /24 CIDR
        try:
            ns.find_singularly_reachable_devices(self.nominal_subnet1, subnet2)
            self.assertTrue(False)  # Test fails if no exception is generated
        except ValueError:
            self.assertTrue(True)

    def test_invalid_ip_format(self):
        ns = NetworkScanner()
        subnet2 = "199.192.168.1.0/24"  # Invalid ip address
        try:
            ns.find_singularly_reachable_devices(self.nominal_subnet1, subnet2)
            self.assertTrue(False)  # Test fails if no exception is generated
        except ValueError:
            self.assertTrue(True)

    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_ignore_list(self, stdout):
        ns = NetworkScanner()
        ignore_list = [254, 255, 300]  # 254 & 255 are valid, 256 is invalid
        ns.find_singularly_reachable_devices(self.nominal_subnet1,
                                             self.nominal_subnet2,
                                             ignore_list=ignore_list)

        # Verify that a warning is provided for invalid value
        if "Invalid" in str(stdout.getvalue()):
            self.assertTrue(False)

        # Verify host_ids 254 & 255 are skipped resulting in 254 ping results.
        if len(ns.ping_status[ns.SUBNET1_IDX]) != 254:
            self.assertTrue(False)

    def test_invalid_retries(self):
        ns = NetworkScanner()
        retries = 4  # Retries value too high
        try:
            ns.find_singularly_reachable_devices(self.nominal_subnet1,
                                                 self.nominal_subnet2,
                                                 retries=retries)
            self.assertTrue(False)  # Test fails if no exception is generated
        except ValueError:
            self.assertTrue(True)


if __name__ == '__main__':
    from network_scanner_kbk import NetworkScanner
    main()
