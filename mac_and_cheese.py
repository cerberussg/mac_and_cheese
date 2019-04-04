#!/usr/local/bin/env python3

import subprocess
import random
import sys
from argparse import ArgumentParser
from pyfiglet import Figlet

parser = ArgumentParser(description='MAC spoofer written in Python')
parser.add_argument('-i', '--interface', dest='interface', help='Interface adapter name to change MAC address on.')
parser.add_argument('-m', '--mac', dest='new_mac', help='Assign a MAC address to interface instead of a random one.')
args = parser.parse_args()
custom_font = Figlet(font='doom')
print(custom_font.renderText("Mac & Cheese"))


def rand_mac():
    return "%02x:%02x:%02x:%02x:%02x:%02x" % (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
        )


def darwin(face, mac):
    subprocess.call(["sudo", "ifconfig", face, "ether", mac])
    subprocess.call(["sudo", "ifconfig", face, "up"])
    print(f'[+] Changing MAC address for {face}')
    print(f'[+] Assigning MAC address: {mac}')
    print(f'[+] Bringing network {face} up')


interface = args.interface
new_mac = args.new_mac
if new_mac is None:
    new_mac = rand_mac()


if sys.platform.startswith('darwin'):
    darwin(interface, new_mac)
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
