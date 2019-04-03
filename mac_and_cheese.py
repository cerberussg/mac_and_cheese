#!/usr/local/bin/env python3

import subprocess
import random
import sys
from argparse import ArgumentParser
from pyfiglet import Figlet

parser = ArgumentParser(description='MAC spoofer written in Python')
parser.add_argument('-i', '--interface', dest='interface', help='Interface adapter name to change MAC address on.')
parser.add_argument('-m', '--mac_address', dest='new_mac', help='Assign a MAC address to interface instead of a random one.')
args = parser.parse_args()


def rand_mac():
    return "%02x:%02x:%02x:%02x:%02x:%02x" % (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
        )


def darwin():
    new_mac = rand_mac()
    interface = input("Enter interface you wish to change > ")
    subprocess.call(["sudo", "ifconfig", interface, "ether", new_mac])
    print(f'[+] Changing MAC address for {interface}')
    print(f'[+] Assigning MAC address: {new_mac}')
    print(f'[+] Bringing network {interface} up')
    subprocess.call(["sudo", "ifconfig", interface, "up"])


custom_font = Figlet(font='doom')
print(custom_font.renderText("Mac & Cheese"))
# print(sys.platform.startswith('darwin'))

if sys.platform.startswith('darwin'):
    darwin()
elif sys.platform.startswith('linux'):
    # TODO: linux code
    pass
elif sys.platform.startswith('win32'):
    # TODO: Windows code
    pass

# new_mac = rand_mac()
# interface = input("Enter interface you wish to change > ")
# print(f'[+] Changing MAC address for {interface}')
# subprocess.call(["sudo", "ifconfig", interface, "down"])
# print(f'[+] Bringing network {interface} down')
# subprocess.call(["sudo", "ifconfig", interface, "ether", new_mac])
# print(f'[+] Assigning MAC address: {new_mac}')
# subprocess.call(["sudo", "ifconfig", interface, "up"])
# print(f'[+] Bringing network {interface} up')
