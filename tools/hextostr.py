#!/usr/bin/env python3

import sys

hexstr = input("hex> ")

all_bytes = []
byte = ""
for i, n in enumerate(hexstr):
    if i % 2 == 0:
        byte = n
        continue
    byte += n
    #print("0x" + byte)
    #print(eval("0x" + byte))
    #print(eval("chr(0x" + byte + ")"))
    all_bytes.append(eval("chr(0x" + byte + ")"))

print("string:")
print("------------------------------------------------")
sys.stdout.write("".join(all_bytes))
print("------------------------------------------------")

