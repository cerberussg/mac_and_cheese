#!/usr/local/bin/env python3

import subprocess
import random
from optparse import OptionParser
from pyfiglet import Figlet

parser = OptionParser()


def rand_mac():
    return "%02x:%02x:%02x:%02x:%02x:%02x" % (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
        )


custom_font = Figlet(font='doom')
print(custom_font.renderText("Mac & Cheese"))

new_mac = rand_mac()
interface = input("Enter interface you wish to change > ")
print(f'[+] Changing MAC address for {interface}')
# subprocess.call(["sudo", "ifconfig", interface, "down"])
# print(f'[+] Bringing network {interface} down')
subprocess.call(["sudo", "ifconfig", interface, "ether", new_mac])
print(f'[+] Assigning MAC address: {new_mac}')
subprocess.call(["sudo", "ifconfig", interface, "up"])
print(f'[+] Bringing network {interface} up')
