import subprocess
# subprocess module allow us to run linux commands in python
import optparse
#optparse package helps to pass command line arguments



# ** 3-Introducing Functions & beautifying the code**
def get_user_input():
    parse_object = optparse.OptionParser()
    # desination inside parse_object will be the variable which will taken as input from user & taking input from user 
    parse_object.add_option("-i","--interface",dest="interface",help="interface to change!")
    parse_object.add_option("-m","--mac",dest="mac_address",help="new mac-address")

    return parse_object.parse_args()

def change_mac_address(user_interface,user_mac_address):
    subprocess.call(["ifconfig",user_interface,"down"])
    subprocess.call(["ifconfig",user_interface,"hw","ether",user_mac_address])
    subprocess.call(["ifconfig",user_interface,"up"])

print("Mac Changer Started!")
change_mac_address(user_input.interface,user_input.mac_address)
