import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered = scapy.srp(arp_request_broadcast, timeout=1, verbose = False)[0]
    clients_list = []
    for element in answered:
        client_dict = {"ip":element[1].psrc, "mac":element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list

def print_result(result_list):
    print("IP\t\t\tMAC Address\n.....................................")
    for client in result_list:
        print(client["ip"]+"\t\t"+client["mac"]) 
   


scan_result = scan("10.0.2.1/24")
print_result(scan_result)


# design an algorithm to descover client on network
# 1. create arp request directed to broadcast mac asking for ip.
# 2. send packet and recieve response 
# 3. parse the response
# 4. print result