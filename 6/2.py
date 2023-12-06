#!/usr/bin/python3

import re

file = open("input.txt", "r")

duration = int(''.join(re.findall(r"\d+", file.readline())))
distance = int(''.join(re.findall(r"\d+", file.readline())))
file.close()

print("Duration: %d - Distance: %d" % (duration, distance))
solutions_counter = 0

for i in range(1, duration + 1):
    if i * (duration - i) > distance:
        solutions_counter += 1

print("Total solutions: %d" % solutions_counter)

