from network_scanner_kbk import NetworkScanner()

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


    