#!/usr/bin/env python3

def print_platform(platform):
    for row in platform:
        print("".join(row))
    print("\n\n")


def tilt_north(platform):
    for i, current_row in enumerate(platform):
        j = i + 1
        if j >= len(platform):
            break
        
        while j > 0:
            for k, tile in enumerate(platform[j]):
                if tile == 'O' and platform[j-1][k] == '.':
                    platform[j-1][k] = 'O'
                    platform[j][k] = '.'
            j -= 1

    return platform

def tilt_west(platform):
    for row in platform:
        for current, tile in enumerate(row):
            next = current + 1
            if next >= len(row):
                break

            while next > 0:
                if row[next] == 'O' and row[next - 1] == '.':
                    row[next - 1] = 'O'
                    row[next] = '.'
                next -= 1
        
    return platform

def tilt_south(platform):
    platform.reverse()
    tilt_north(platform)    
    platform.reverse()

    return platform

def tilt_east(platform):
    for row in platform:
        for current, tile in enumerate(row):
            next = current + 1
            if next >= len(row):
                break

            while next > 0:
                if row[next] == '.' and row[next - 1] == 'O':
                    row[next - 1] = '.'
                    row[next] = 'O'
                next -= 1
        
    return platform

def cycle(platform):
    platform = tilt_north(platform)
    platform = tilt_west(platform)
    platform = tilt_south(platform)
    platform = tilt_east(platform)

    return platform

if __name__ == "__main__":
 
    file = open('example.txt', 'r')
    platform = [list(row.strip()) for row in file]
    file.close()
   
    for i in range(0, 1000000000):
        platform = cycle(platform)

    max_load = len(platform)
    total_load = 0

    for offset, row in enumerate(platform):
        rocks = row.count('O')

        load = rocks * (max_load - offset)
        total_load += load

    print(total_load)
