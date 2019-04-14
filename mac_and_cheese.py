#!/usr/local/bin python3

import subprocess
import random
import sys
import os
import re
from argparse import ArgumentParser
from pyfiglet import Figlet


def arguments():
    parser = ArgumentParser(description='MAC spoofer written in Python 3. Must have admin access or sudo capability')
    parser.add_argument('-i', '--interface', dest='interface',
                        help='Interface adapter name to change MAC address: (ex. eth0, en1)')
    parser.add_argument('-m', '--mac', dest='new_mac',
                        help='Assign a MAC address to interface instead of a randomly generated one.')
    args = parser.parse_args()
    if args.interface is None:
        args.interface = input('Enter interface you wish to change $ ')
        if not args.interface:
            parser.error('[-] Please specify an interface (ex. eth0, en1), use --help for more info.')
    if args.new_mac is None:
        args.new_mac = rand_mac()
    return args


def admin_check():
    uid = os.getuid()
    if uid != 0:
        print('[-] Not and admin. Please run this command elevated using sudo.')
        exit()


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
    subprocess.call(["ifconfig", face, "ether", mac])
    subprocess.call(["ifconfig", face, "up"])
    message(face, mac)


def linux(face, mac):
    subprocess.call(["ifconfig", face, "down"])
    subprocess.call(["ifconfig", face, "hw", "ether", mac])
    subprocess.call(["ifconfig", face, "up"])
    message(face, mac)


def win32(face, mac):
    # TODO: Windows Code
    pass


def message(face, mac):
    print(f'[+] Changing MAC address for {face}')
    print(f'[+] Assigning MAC address: {mac}')
    print(f'[+] Bringing network {face} up')


def spoof_attempt(arguments):
    if sys.platform.startswith('darwin'):
        darwin(arguments.interface, arguments.new_mac)
        spoof_outcome(arguments.interface, arguments.new_mac)
    elif sys.platform.startswith('linux'):
        linux(arguments.interface, arguments.new_mac)
        spoof_outcome(arguments.interface, arguments.new_mac)
    elif sys.platform.startswith('win32'):
        win32(arguments.interface, arguments.new_mac)
        # TODO: spoof_outcome_win32(arguments.interface, arguments.new_mac)


def spoof_outcome(face, mac):
    ether = subprocess.run(["ifconfig", face], stdout=subprocess.PIPE)
    ether = ether.stdout.decode('utf-8')
    eth = re.search('(?:[0-9a-fA-F]:?){12}', ether)
    if eth.group(0) == mac:
        print('[+] MAC address successfully spoofed.')
    else:
        print('[-] MAC address failed to be spoofed.')


custom_font = Figlet(font='doom')
print(custom_font.renderText("MAC & Cheese"))
admin_check()
arguments = arguments()
spoof_attempt(arguments)
