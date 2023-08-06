#!/usr/bin/python

import datetime
import calendar
import os
import time
from threading import Thread
from multiprocessing import Process
import subprocess
from collections import OrderedDict

##from scapy.all import *


class NetworkScanner():
    def __init__(self):
        """ This class provides a library of functions to view network properties on the
            Joby Challenge Problem Device Network. """
        self.host_prefix = [None, None] # Contains the host prefixes for each of the 2 subnets (subnet1 and subnet2)
        
        ping_status_subnet1 = OrderedDict()  # Dictionary to hold ping return code status for each host on subnet1
        ping_status_subnet2 = OrderedDict()  # Dictionary to hold ping return code status for each host on subnet2
        self.ping_status = [ping_status_subnet1, ping_status_subnet2]  # List with 1 entry for each subnet
        
        self.OCTET_MAX_VALUE = 255
        self.MAX_PING_RETRIES = 3
        self.SUBNET1_IDX = 0
        self.SUBNET2_IDX = 1
        
        self.singularly_accesible_nodes = []
    
    def validate_subnet_input(self, subnet_input):
        """ Validate that the subnet_input is valid and return the host prefix portion of
            the subnet_input.  eg. given "192.168.1.0/24, return: "192.168.1." (including the trailing ".")
        """
        error_msg = "Unrecognized format for subnet input: " + subnet_input
        
        if not subnet_input.endswith("/24"):
             raise ValueError(error_msg)
        subnet = subnet_input.replace("/24", "")
        
        octets = subnet.split(".")
        if len(octets) != 4:
             raise ValueError(error_msg)
        
        for o in octets:
            if not (o.isnumeric() and int(o) >= 0 and int(o) <= self.OCTET_MAX_VALUE):
                raise ValueError(error_msg)
        
        host_prefix = subnet_input[0:subnet_input.rfind(".") + 1]
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
            raise ValueError("Invalid value for retries: " + str(retries))
    
    
#    def xxx(self, subnet1, subnet2, retries=1, ignore_list=[]):
#        packets = IP(dst=["www.google.com", "www.google.fr"])/ICMP()
#        results = sr(packets)
    
    
    
    def find_singularly_accesible_nodes(self, subnet1, subnet2, retries=1, ignore_list=[]):
        """ 
            For every device in the network, find all devices that are reachable via only 1 unique IP. 

            subnet1
            subnet2
            retries
            ignore_list

        """
        
        # Validate all input arguments here
        self.host_prefix[self.SUBNET1_IDX] = self.validate_subnet_input(subnet1)
        self.host_prefix[self.SUBNET2_IDX] = self.validate_subnet_input(subnet2)        
        validated_ignore_list = self.validate_ignore_list(ignore_list)
        self.validate_retries(retries)
        
        print("Launching ping threads")
        
        thread_ids = []
        for host_id in range(self.OCTET_MAX_VALUE):
            #for subnet_idx in [self.SUBNET1_IDX, self.SUBNET2_IDX]:  # Split ping requests accross networks to balance/releive traffic
            for subnet_idx in [self.SUBNET2_IDX]:
                #print("Pinging ip: " + str(ip))
                t = Thread(target=self.ping, args=(host_id, subnet_idx, retries,))
                #t = Process(target=self.ping, args=(ip, subnet_idx, retries,))
                t.start()
                thread_ids.append(t)
        print("All threads started..")
        for t in thread_ids:
            t.join()
        
        print("All threads completed")
        
        return self.singularly_accesible_nodes
        
    def ping(self, host_id, subnet_idx, retries):
        tries = retries + 1
        ip = self.host_prefix[subnet_idx] + str(host_id)
        subprocess_cmd = 'ping -n ' + str(tries) + ' -w 3000 ' + ip
        #####print("ping called with subnet_idx, subprocess_cmd: " + str(subnet_idx) + ", " + str(subprocess_cmd))
        #returncode = subprocess.run(subprocess_cmd).returncode
        sp = subprocess.run(subprocess_cmd, capture_output=True, text=True)
        returncode = sp.returncode
        stdout = sp.stdout
        
        # Simplest way to determine if ip is reachable. ping -c requires admin privedlges (which would make this package require admin.)
        returncode = ""
        if "time=" in stdout:
            returncode = True
        
        ####print("ping status: " + str(ip) + ": " + str(returncode))
        #print("ping status: " + str(ip) + ": " + str(returncode) + str(stdout))
        self.ping_status[subnet_idx][host_id] = returncode
        #raw_list.append(host+ ' '+ str((subprocess.run('ping -n 3 -w 800 '+host).returncode)))        
          
  
if __name__ == "__main__":
    print ("Testing NetworkScanner...")
    
    last_round = None
    #for i in range(0, 1):
    for i in range(0, 4):
        subnet1 = "192.168.0.0/24"
        subnet2 = "192.168.1.0/24"
        
        # subnet1 = "192.168." + str(i%2) + ".0/24"
        # subnet2 = "192.168." + str(2*i + 1) + ".0/24"
        print("\n\n\n" + subnet1 + subnet2)
        retries = 0
        #ignore_list = [23, 45, -1, 256]
        ignore_list = []
        
        nv = NetworkScanner()
        #nodes = nv.xxx(subnet1, subnet2, retries, ignore_list)
        nodes = nv.find_singularly_accesible_nodes(subnet1, subnet2, retries, ignore_list)


        print("Singularly accesible nodes:")
        print(nodes)
        
        print("Subnet1:")
        for key in sorted(nv.ping_status[0]):
            s = "%s: %s" % (key, nv.ping_status[0][key])
            print(s.ljust(10), end ="")
        
        print("Subnet2:")
        total = 0
        for key in sorted(nv.ping_status[1]):
            s = "%s: %s" % (key, nv.ping_status[1][key])
            if nv.ping_status[1][key] == True:
                total += 1
            print(s.ljust(10), end ="")
                
        
        print("\n\nTOTAL: " + str(total))
        if last_round is not None:
            for key in sorted(nv.ping_status[1]):
                if nv.ping_status[1][key] != last_round[key]:
                    if last_round[key] == True:
                        print("DISAPPEARED: " + str(key))
                    else:
                        print("APPEARED: " + str(key))
        last_round = nv.ping_status[1]     
            
        #print ("Done Testing NetworkScanner...")


    