import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst ="FF:FF:FF:FF:FF:FF")
    arp_request_broadcast = broadcast / arp_request
    print(arp_request_broadcast.summary())
    arp_request_broadcast.show()


scan("192.168.0.1/24")