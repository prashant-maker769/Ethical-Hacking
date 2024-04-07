# subprocess module allow us to run linux commands in python
import subprocess
#optparse package helps to pass command line arguments
import optparse
#importing regular expression
import re



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

# saving subprocess 
def control_new_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig",interface])
    
# To check the mac_address has been changed or not for that we need to extract the mac-address of interface before and after code execution
# For that REGEX (reglular expression) will help us, it is used to match the strings of text such as particular words, characters, pattern, etc.
    #\w means any word character as we have 12 charcater for mac-address
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig))
    if new_mac:
        return new_mac.group(0)
    else:
        return None

print("Mac Changer Started!")
(user_input, arguments) = get_user_input()
change_mac_address(user_input.interface,user_input.mac_address)
finalized_mac = control_new_mac(str(user_input.interface)):
if finalized_,ac == user_input.mac_address:
    print("Success!")
else:
    print("error?????????")
