import subprocess
from threading import Thread
from collections import OrderedDict

# In addition to being part of a module, this script can be run directly.
if __name__ == "__main__":
    from ns_logger import NSLogger
else:
    from .ns_logger import NSLogger


class NetworkScanner():
    def __init__(self):
        """
        This class provides a library of functions to view network
        properties on the Joby Challenge Problem Device Network.
        """
        # Contains host prefixes for each subnet (subnet1 and subnet2)
        self.host_prefix = [None, None]

        # Pingability status for each host on subnet1, keyed by octet value
        ping_status_subnet1 = OrderedDict()
        # Pingability status for each host on subnet2, keyed by octet value
        ping_status_subnet2 = OrderedDict()
        # List with 1 entry for each subnet
        self.ping_status = [ping_status_subnet1, ping_status_subnet2]

        self.OCTET_MAX_VALUE = 255
        self.MAX_PING_RETRIES = 3
        self.SUBNET1_IDX = 0
        self.SUBNET2_IDX = 1

        self.ns_log = NSLogger()  # Network Scanner Log

    def validate_subnet(self, subnet_input):
        """
        Validate that the subnet_input is valid and return the host
        prefix portion of the subnet_input.  eg. given "192.168.1.0/24,
        return: "192.168.1." (including the trailing ".")
        """
        error_msg = "Unrecognized format for subnet input: " + subnet_input

        if not subnet_input.endswith("/24"):
            raise ValueError(error_msg)
        subnet = subnet_input.replace("/24", "")

        octets = subnet.split(".")
        if len(octets) != 4:
            raise ValueError(error_msg)

        for o in octets:
            if not (o.isnumeric() and int(o) >= 0 and
                    int(o) <= self.OCTET_MAX_VALUE):
                raise ValueError(error_msg)

        host_prefix = subnet_input[0:subnet_input.rfind(".") + 1]
        return host_prefix

    def validate_ignore_list(self, ignore_list):
        """
        Validate that all the values in ignore_list are valid octet values.
        Return a validated ignore_list with invalid octets removed.
        """
        validated_ignore_list = []

        for i in ignore_list:
            if i >= 0 and i <= self.OCTET_MAX_VALUE:
                validated_ignore_list.append(i)
            else:
                self.ns_log.warning("Invalid octet in ignore_list: " + str(i))

        return validated_ignore_list

    def validate_retries(self, retries):
        """ Validate retries is in valid range for this package. """
        if not (retries >= 0 and retries <= self.MAX_PING_RETRIES):
            raise ValueError("Invalid value for retries: " + str(retries))

    def find_singularly_reachable_devices(self, subnet1, subnet2,
                                          retries=1, ignore_list=[]):
        """
        For every device in the network, find all devices that are reachable
        via exactly one subnet.

        Parameters:
            subnet1 (str):ip address for subnet1 in CIDR /24 notation
            subnet2 (str):ip address for subnet2 in CIDR /24 notation
            retries (int):number of additional times to attempt ping
            ignore_list (list):list of octets/host_ids to ignore each subnet

        Returns:
            ips_by_octet(list):List of singularily accesible ips

        """

        # Validate all input arguments
        self.host_prefix[self.SUBNET1_IDX] = self.validate_subnet(subnet1)
        self.host_prefix[self.SUBNET2_IDX] = self.validate_subnet(subnet2)
        validated_ignore_list = self.validate_ignore_list(ignore_list)
        self.validate_retries(retries)

        # For each octet, ping the same octet on each subnet, alternating
        # alternating between subnets to balance traffic accross subnets
        self.ns_log.info("Launching ping threads")
        thread_ids = []
        for octet in range(self.OCTET_MAX_VALUE):
            if octet not in validated_ignore_list:
                for idx in [self.SUBNET1_IDX, self.SUBNET2_IDX]:
                    t = Thread(target=self.ping, args=(octet, idx, retries,))
                    t.start()
                    thread_ids.append(t)
        self.ns_log.info("All threads started..")

        # Wait for all ping threads to complete
        for t in thread_ids:
            t.join()
        self.ns_log.info("All threads completed")

        return self.create_ip_dictionaries()

    def ping(self, octet, subnet_idx, retries):
        tries = retries + 1
        ip = self.host_prefix[subnet_idx] + str(octet)
        subprocess_cmd = 'ping -n ' + str(tries) + ' -w 3000 ' + ip
        self.ns_log.debug("ping called with subnet_idx, subprocess_cmd: "
                          + str(subnet_idx) + ", " + str(subprocess_cmd))

        sp = subprocess.run(subprocess_cmd, capture_output=True, text=True)
        stdout = sp.stdout

        # Simplest way to determine if ip is reachable is if the ping command
        # output contains "time=" followed by ping time in milliseconds.
        # ping -c has better output but requires admin privedlges to run.
        # The return code from ping does not seem to be a reliable indicator
        # of device presence.
        returncode = ""
        if "time=" in stdout:
            returncode = True

        self.ping_status[subnet_idx][octet] = returncode

    def create_ip_dictionaries(self):
        """
        Use the class data to form a list of dictionaries where each dictionary
        contains connectivity information for a single octect.  Octets with
        similar connetivity states are ommited from the dictionary.  Example:

        [
            {
                "192.168.1.25" : true,
                "192.168.1.25" : false
            },
            {
                "192.168.1.27" : false,
                "192.168.1.257" : true
            }
        ]
        """
        ips_by_octet = []

        for octet in sorted(self.ping_status[self.SUBNET1_IDX]):
            # Get the pingability status of octet for each subnet
            subnet1_octet_pingable = self.ping_status[self.SUBNET1_IDX][octet]
            subnet2_octet_pingable = self.ping_status[self.SUBNET2_IDX][octet]

            # If the given octet has a different pingability status on each
            # subnet, add ip and pingability status to output data structure
            if subnet1_octet_pingable != subnet2_octet_pingable:
                subnet1_ip = self.host_prefix[self.SUBNET1_IDX] + str(octet)
                subnet2_ip = self.host_prefix[self.SUBNET2_IDX] + str(octet)

                dict_entry = {subnet1_ip: subnet1_octet_pingable,
                              subnet2_ip: subnet2_octet_pingable}
                self.ns_log.debug("dict_entry: " + str(dict_entry))
                ips_by_octet.append(dict_entry)

        return ips_by_octet


if __name__ == "__main__":
    print("Testing NetworkScanner...")

    ns = NetworkScanner()

    subnet1 = "192.168.0.0/24"
    subnet2 = "192.168.1.0/24"
    retries = 0
    ignore_list = [1, 256]
    print("\n\n" + str(subnet1).ljust(15) + str(subnet2).ljust(15)
          + str(retries).ljust(15) + str(ignore_list).ljust(15))

    devices = ns.find_singularly_reachable_devices(subnet1, subnet2,
                                                   retries, ignore_list)

    print("List of devices reachable on exactly one subnet:")
    for d in devices:
        print(d)
