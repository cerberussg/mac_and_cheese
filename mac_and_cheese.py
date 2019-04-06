#!/usr/local/bin/env python3

import subprocess
import random
import sys
from argparse import ArgumentParser
from pyfiglet import Figlet


def arguments():
    parser = ArgumentParser(description='MAC spoofer written in Python 3')
    parser.add_argument('-i', '--interface', dest='interface',
                        help='Interface adapter name to change MAC address on. Example: en9 or eth0.')
    parser.add_argument('-m', '--mac', dest='new_mac',
                        help='Assign a MAC address to interface instead of a random one.')
    args = parser.parse_args()
    if args.interface is None:
        args.interface = input("Enter interface you wish to change > ")
    if args.new_mac is None:
        args.new_mac = rand_mac()
    return args


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


custom_font = Figlet(font='doom')
print(custom_font.renderText("Mac & Cheese"))


arguments = arguments()

if sys.platform.startswith('darwin'):
    darwin(arguments.interface, arguments.new_mac)
elif sys.platform.startswith('linux'):
    linux(arguments.interface, arguments.new_mac)
elif sys.platform.startswith('win32'):
    # TODO: Windows code
    pass
