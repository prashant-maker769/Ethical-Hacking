#scapy helps to create arp requests
import scapy.all as scapy
import optparse
# 1. ARP request
# 2. broadcast packet
# 3. processing the response

def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--ip_address", dest="ip_Address", help="Enter the IP address")
    (user_input, arguments) = parse_object.parse_args()
  
    if not user_input.ip_Address:
      print("Enter the IP Address")
    return user_input

def scan_my_network(ip):
    arp_request_packet = scapy.ARP(pdst=ip)
    
    #scapy.ls helps us to get all the parameers required in scapy.ARP
    #scapy.ls(scapy.ARP())
    
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #scapy.ls helps us to get all the parameers required in scapy.Ether
    #scapy.ls(scapy.Ether())
    
    #adding the broadcast and arp packets before sending arp request
    combine_packet = broadcast_packet/arp_request_packet
    
    #output will be in answered and unanswered list as a tuple
    (answered_list, unanswered_list) = scapy.srp(combine_packet, timeout=1)
    #print(list(answered_list))
    answered_list.summary()

user_ip_address = get_user_input()
scan_my_network(user_ip_address.ip_Address)
