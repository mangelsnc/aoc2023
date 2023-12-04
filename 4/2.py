#!/usr/bin/python3

import re

file = open("input.txt", "r")
total = 0
copies = [1 for line in file]
file.seek(0)

i = 0
for scratch_card in file:
    (my_numbers, winning_numbers) = scratch_card.split('|')
    my_numbers = list(map(int, re.findall(r"(-?\d+)", my_numbers)))
    my_numbers.pop(0)
    winning_numbers = list(map(int, re.findall(r"(-?\d+)", winning_numbers)))
    
    in_common = set(winning_numbers) & set(my_numbers)
    matches = len(in_common)
    print(matches)
    
    for j in range(i + 1, (i + matches + 1)):
        if j < len(copies):
            copies[j] = copies[j] + (1 * copies[i])

    print(copies)
    i += 1

print(sum(copies))
file.close()
