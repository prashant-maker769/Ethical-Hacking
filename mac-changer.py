import subprocess
# subprocess module allow us to run linux commands in python
import optparse
#optparse package helps to pass command line arguments

# 1-Passing linux commands to python code to change mac-address
"""
subprocess.call(["ifconfig","eth0","down"])
subprocess.call(["ifconfig","eth0","hw","ether","00:11:22:33:44:55"])
subprocess.call(["ifconfig","eth0","up"])
"""

# ** 2-Introducing varibales in subprocess module **
parse_object = optparse.OptionParser()
# desination inside parse_object will be the variable which will taken as input from user
# taking input from user 
parse_object.add_option("-i","--interface",dest="interface",help="interface to change!")
parse_object.add_option("-m","--mac",dest="mac_address",help="new mac-address")

# To print
#print(parse_object.parse_args())

# Seperating input took from user or command line
# parse returns output in tuples, so
(user_input, argument)= parse_object.parse_args()
# it  is stord with destination name
#print(user_input.interface)
#print(user_input.mac_address)
user_interface = user_input.interface
uer_mac_address = user_input.mac_address

subprocess.call(["ifconfig",user_interface,"down"])
subprocess.call(["ifconfig",user_interface,"hw","ether",uer_mac_address])
subprocess.call(["ifconfig",user_interface,"up"])
