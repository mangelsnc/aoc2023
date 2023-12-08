#!/usr/bin/python3

import re
from itertools import cycle
from math import lcm

file = open('input.txt', 'r')

directions = list(file.readline().strip())
file.readline()

map = {}

for mapping in file:
    (position, left, right) = re.findall(r"^(\w{3}) = \((\w{3}), (\w{3})\)$", mapping)[0]
    map[position] = {'L': left, 'R': right}
file.close()

map = dict(sorted(map.items()))
starting_nodes = [label for label in map.keys() if label.endswith('A')]
steps_list = []

for node in starting_nodes:
    for step, direction in enumerate(cycle(directions)):
        if node.endswith('Z'):
            steps_list.append(step)
            break
        node = map[node][direction]


print(lcm(*steps_list))
