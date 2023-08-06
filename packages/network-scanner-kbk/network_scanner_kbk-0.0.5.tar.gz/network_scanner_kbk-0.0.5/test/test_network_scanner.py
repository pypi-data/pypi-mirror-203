#!/usr/bin/python

import datetime
import calendar
import os
import time
#from dpm_constants import all_ccnote_db_types, all_ccnote_complaints, hash_tags


class TestNetworkViewer():
    def __init__(self):
        """ This class can operate on a database data.  It can also operate on the actual database given a database pointer. """
        self.host_prefix_subnet1 = None
        self.host_prefix_subnet2 = None
        
        self.OCTET_MAX_VALUE = 255
        self.MAX_PING_RETRIES = 3
        
        self.singularly_accesible_nodes = []
    
    def validate_subnet_input(self, subnet_input):
        """ Validate that the subnet_input is valid and return the host prefix portion of
            the subnet_input.  eg. given "192.168.1.0/24, return: "192.168.1." (including the trailing ".")
        """
        
        if not subnet_input.endswith("/24"):
             raise ValueError("Unrecognized format for subnet input: " + subnet_input)
        subnet = subnet_input.replace("/24", "")
        
        if subnet_input.count(".") != 3:
             raise ValueError("Unrecognized format for subnet input: " + subnet_input)
        host_prefix = subnet_input[0:subnet_input.rfind(".") + 1]
        
        # host_prefix could be validated further here to verify correct format.
        return host_prefix

    def validate_ignore_list(self, ignore_list):
        """ Validate that all the values in ignore_list are valid ip address octets.
            Return a validated ignore_list with invalid octets removed.  """
        validated_ignore_list = []
        
        for i in ignore_list:
            if i >= 0 and i <= self.OCTET_MAX_VALUE:
                validated_ignore_list.append(i)
            else:
                print("Warning: invalid octet value provided in ignore_list: " + str(i))
    
        return validated_ignore_list

    def validate_retries(self, retries):
        """ Validate that retries is in a valid range for the network_viewer. """
        if not (retries >= 0 and retries <= self.MAX_PING_RETRIES):
            raise ValueError("Invalid value for retries: " + retries)
    
    
    def find_singularly_accesible_nodes(self, subnet1, subnet2, retries=1, ignore_list=[]):
        """ 
            For every device in the network, find all devices that are reachable via only 1 unique IP. 

            subnet1
            subnet2
            retries
            ignore_list

        """
        
        # Validate all input arguments here
        self.host_prefix_subnet1 = self.validate_subnet_input(subnet1)
        self.host_prefix_subnet2 = self.validate_subnet_input(subnet2)        
        validated_ignore_list = self.validate_ignore_list(ignore_list)
        self.validate_retries(retries)
        
        print("In - find_single_addr_devices")
        return self.singularly_accesible_nodes
          
  
if __name__ == "__main__":
    print ("Testing TestNetworkViewer...")
    
    subnet1 = "192.168.1.0/24"
    subnet2 = "192.168.2.0/24"
    retries = 1
    #ignore_list = [23, 45, -1, 256]
    ignore_list = []
    
    nv = TestNetworkViewer()
    nodes = nv.find_singularly_accesible_nodes(subnet1, subnet2, retries, ignore_list)


    print("Singularly accesible nodes:")
    print(nodes)
    print ("Done Testing TestNetworkViewer...")


    