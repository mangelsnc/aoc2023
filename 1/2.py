#!/usr/bin/python3

import string

f = open("input.txt", "r")
total = 0
letters = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numbers = ["o1e", "t2o", "t3e", "4", "f5e", "6", "s7n", "e8t", "n9e"]

for line in f:
    for letter, number in zip(letters, numbers):
        line = line.replace(letter, number)

    line = line.translate({ord(i): None for i in string.ascii_letters}).strip()
    to_number = int("%s%s" % (line[0], line[-1]))
    total += to_number

print(total)
