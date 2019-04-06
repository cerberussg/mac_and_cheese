# Mac & Cheese

## Mac address spoofer

- MAC spoofer written in Python 3. 
- Must have admin access or sudo capability.

## Usage

### Spoof MAC on interface adapter en9, randomizes the MAC address

```shell
python3 mac_and_cheese.py -i en9
```

### Specify a specific MAC address on interface adapter en9

```shell
python3 mac_and_cheese.py -i en9 -m 0c:bb:20:de:9c:0f
```

### Run the script from command line without arguments

```shell
python3 mac_and_cheese.py
```

## Compatible OS

- [x] Linux
- [x] MacOS
- [ ] Windows