#!/usr/bin/python3

import re

file = open("input.txt", "r")

total_power = 0

for line in file:
    blue_cubes = max([int(i) for i in re.findall(r"(\d+) blue", line)])
    red_cubes = max([int(i) for i in re.findall(r"(\d+) red", line)])
    green_cubes = max([int(i) for i in re.findall(r"(\d+) green", line)])

    total_power += (blue_cubes * red_cubes * green_cubes)

print(total_power)

file.close()
