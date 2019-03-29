#!/usr/local/bin/env python3

import subprocess
import random
from pyfiglet import Figlet


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
interface = "en6"
new_mac = rand_mac()

print(custom_font.renderText("Mac & Cheese"))
print(f'[+] Changing MAC address for {interface}')
# subprocess.call("sudo ifconfig en7 down", shell=True)
# print("Bringing network en7 down")
subprocess.call(f'sudo ifconfig {interface} ether {new_mac}', shell=True)
print(f'[+] Assigning MAC address: {new_mac}')
subprocess.call(f'sudo ifconfig {interface} up', shell=True)
print(f'[+] Bringing network {interface} up')
