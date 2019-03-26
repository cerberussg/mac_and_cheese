#!/usr/bin/env python

import subprocess

subprocess.call("ifconfig eth0 down", shell=True)
print("Bringing network eth0 down")
subprocess.call("ifconfig eth0 hw ether 08:00:27:F8:42:A7", shell=True)
print("Changing MAC address on eth0 to: 08:00:27:F8:42:A7")
subprocess.call("ifconfig eth0 up", shell=True)
print("Bringing network eth0 up")
