#!/usr/bin/env python3

def print_platform(platform):
    for row in platform:
        print(row)
    print("\n\n")

file = open('input.txt', 'r')
platform = [list(row.strip()) for row in file]
file.close()
print_platform(platform)

for i, current_row in enumerate(platform):
    j = i + 1
    if j >= len(platform):
        break
    
    while j > 0:
        print(j)
        for k, tile in enumerate(platform[j]):
            if tile == 'O' and platform[j-1][k] == '.':
                platform[j-1][k] = 'O'
                platform[j][k] = '.'
        j -= 1

max_load = len(platform)
total_load = 0

for offset, row in enumerate(platform):
    rocks = row.count('O')

    load = rocks * (max_load - offset)
    total_load += load

print(total_load)
