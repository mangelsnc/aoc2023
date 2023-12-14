#!/usr/bin/env python3


def get_universe():
    file = open('input.txt', 'r')
    universe = [list(line.strip()) for line in file]
    file.close()

    return universe

def expand_universe(universe):
    columns_not_to_expand = []
    rows_not_expand = []

    for y, column in enumerate(universe):
        for x, row in enumerate(column):
            if universe[x][y] == '#':
                columns_not_to_expand.append(y)
                rows_not_expand.append(x)

    rows_not_expand = sorted(list(set(rows_not_expand)))
    columns_not_to_expand = sorted(list(set(columns_not_to_expand)))

    for i in range(0, len(universe)):
        if i in rows_not_expand:
            continue

        universe.insert(i+1, ['.'] * len(universe[0]))

    for y in range(0, len(universe)):
        offset = 0
        for x in range(0, len(universe[y])):
            if x in columns_not_to_expand:
                continue

            universe[y].insert(x+1+offset, '.')
            offset += 1

    return universe


def get_galaxies(universe):
    galaxies = []
    
    for y, column in enumerate(universe):
        for x, row in enumerate(column):
            if universe[y][x] == '#':
                galaxies.append((y, x))

    return sorted(galaxies)


def print_universe(universe):
    for row in universe:
        for col in row:
            print(col, end='')
        print("\r\n")

if __name__ == "__main__":
    universe = get_universe()
    print(f"Original universe size: {len(universe)}x{len(universe[0])}")
    universe = expand_universe(universe)
    print(f"Expanded universe size: {len(universe)}x{len(universe[0])}")
    print_universe(universe)

    galaxies = get_galaxies(universe)


    total_distance = 0
    pairs = 0
    shortest_paths = []
    for i, galaxy in enumerate(galaxies):
        for other_galaxy in galaxies[i+1:]:
            pairs += 1
            #print(f"Galaxy: {galaxy}")
            #print(f"Other galaxy: {other_galaxy}")

            distance = (abs(other_galaxy[0] - galaxy[0]) + abs(other_galaxy[1] - galaxy[1]))
            shortest_paths.append(distance)
            #print(f"Distance: {distance}\n\n")
            total_distance += distance

    print(f"Total galaxies: {len(galaxies)}")
    print(f"Total pairs: {pairs}")
    print(f"Shortest paths: {len(shortest_paths)}")
    print(f"Total distance: {total_distance}")
