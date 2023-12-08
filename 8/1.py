#!/usr/bin/python3

import re

file = open('input.txt', 'r')

directions = list(file.readline().strip())
print(directions)
file.readline()

map = {}

for mapping in file:
    (position, left, right) = re.findall(r"^(\w{3}) = \((\w{3}), (\w{3})\)$", mapping)[0]
    map[position] = {'L': left, 'R': right}
file.close()

map = dict(sorted(map.items()))

current_node = 'AAA'
steps = 0

while current_node != 'ZZZ':
    direction = directions[steps % len(directions)]
    steps += 1
    current_node = map[current_node][direction]

print(steps)
