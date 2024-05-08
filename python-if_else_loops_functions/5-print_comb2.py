#!/usr/bin/python3
for e in range(0, 100):
    if e < 99:
        print("{:02d}, ".format(e), end="")
    else:
        print("99")
