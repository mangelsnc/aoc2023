#!/usr/bin/python3

import string

f = open("input.txt", "r")
total = 0
for line in f:
    line = line.translate({ord(i): None for i in string.ascii_letters}).strip()
    number = int("%s%s" % (line[0], line[-1]))
    total += number

print(total)
