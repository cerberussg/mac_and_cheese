# Mac & Cheese

## Mac address spoofer

- MAC spoofer written in Python 3. 
- Must have admin access or sudo capability.
- Multi platform.

## Usage

### Spoof MAC on interface adapter en9, randomizes the MAC address

```shell
python3 mac_and_cheese.py -i en9
```

```shell
python3 mac_and_cheese.py --interface en9
```

### Specify a specific MAC address on interface adapter en9

```shell
python3 mac_and_cheese.py -i en9 -m 0c:bb:20:de:9c:0f
```

```shell
python3 mac_and_cheese.py --interface en9 --mac 0c:bb:20:de:9c:0f
```

### Invoke help from the command line

```shell
python3 mac_and_cheese.py -h
```

```shell
python3 mac_and_cheese.py --help
```

### Run the script from command line without arguments

```shell
python3 mac_and_cheese.py
```

## Compatible OS

- [x] Linux
- [x] MacOS
- [ ] Windows