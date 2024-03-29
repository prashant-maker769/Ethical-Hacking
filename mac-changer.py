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

# 2-Introducing varibales in subprocess module
# variables 
interface = 
subprocess.call(["ifconfig","eth0","down"])
subprocess.call(["ifconfig","eth0","hw","ether","00:11:22:33:44:55"])
subprocess.call(["ifconfig","eth0","up"])
