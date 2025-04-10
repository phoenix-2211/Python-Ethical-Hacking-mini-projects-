import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m","--mac", dest="new_mac",help="New mac address")
    (options,arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] please specify an interface for help use --help")
    elif not options.new_mac:
        parser.error("[-] please specify new mac address for help use --help ")
    return options

def change_mac(interface, new_mac):
    print("[+] changing MAC address for "+interface+" to "+new_mac)
    subprocess.run(["ifconfig" ,interface, "down"])
    subprocess.run(["ifconfig" ,interface, "hw","ether", new_mac])
    subprocess.run(["ifconfig" ,interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig",interface])
    

    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig_result))
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address")

options = get_arguments()
current_mac = get_current_mac(options.interface)
print("current mac = " + str(current_mac))
change_mac(options.interface,options.new_mac)
current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] Mac address successfully changed to : "+ current_mac)
else:
    print("[-] the mac address did not changed")









# 1. execute and read ifconfig
# 2. read the mac address from output
# 3. check if mac in ifconfig is what the user requested
# 4. print appropriate message.