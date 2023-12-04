#!/usr/bin/python3

import re

file = open("input.txt", "r")
total = 0

for scratch_card in file:
    (my_numbers, winning_numbers) = scratch_card.split('|')
    my_numbers = list(map(int, re.findall(r"(-?\d+)", my_numbers)))
    my_numbers.pop(0)
    winning_numbers = list(map(int, re.findall(r"(-?\d+)", winning_numbers)))
    
    in_common = set(winning_numbers) & set(my_numbers)
    matches = len(in_common)
    if matches > 0:
        total += pow(2, (matches - 1))

print(int(total))
file.close()
