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


def linux(face, mac):
    print(f'[+] Bringing network {face} down')
    subprocess.call(["sudo", "ifconfig", face, "down"])
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
    linux(interface, new_mac)
elif sys.platform.startswith('win32'):
    # TODO: Windows code
    pass
