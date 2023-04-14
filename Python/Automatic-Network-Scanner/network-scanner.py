''' import modules '''

import ifaddr
import ipaddress

import scapy.all as scapy


def main():
    
    print("\n*************************************************************************************************")
    print("\n* Automatic Network Scanner(ANS)  *")
    print("\n* Copyright of GNINGHAYE Malcolmx, 2022 *")
    print("\n* Linkedin: https://www.linkedin.com/in/malcolmx-hassler-gninghaye-guemandeu-77a5b11b0/ *")
    print("\n* GitHub: https://github.com/MalcolmxHassler  *")
    print("\n*************************************************************************************************")
    
    adapters = ifaddr.get_adapters()
    # To get the adapter name
    for adapter in adapters:
        
        for ip in adapter.ips:
            adap="%s/%s" % (ip.ip, ip.network_prefix)
            if not(float(adap.split("/")[-1])>=32 or adap.startswith("169.254") or adap.startswith("127")):
                print('\n')
                print("[+]NETWORK ADAPTER : " + adapter.nice_name)
                host=ipaddress.ip_interface(adap).network.compressed ## get the network address

                scanning = scapy.arping(host) # Scanning for the entire network using ARP protocol


if __name__ == "__main__":

    main()
