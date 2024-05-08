#!/usr/bin/python3
for e in range(0, 10):
    for a in range(1, 10):
        if e >= a:
            continue
        elif e == 8 and a == 9:
            print("{}{}".format(e, a))
        else:
            print("{}{}, ".format(e, a), end="")
       