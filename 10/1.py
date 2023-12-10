#!/usr/bin/env python3

from collections import deque
from typing import Dict, List, Tuple, Deque

STARTING_POINT = 'S'

def get_starting_point(map):
    starting_point_x = None
    starting_point_y = None
    
    for y, row in enumerate(map):
        starting_point_y = y
        try:
            starting_point_x = row.index('S')

            return starting_point_x, starting_point_y
        except ValueError:
            pass

PIPE_TO_DIRECTIONS_MAPPING = {
    "|": ["N", "S"],
    "-": ["W", "E"],
    "L": ["N", "E"],
    "J": ["N", "W"],
    "7": ["S", "W"],
    "F": ["S", "E"],
    STARTING_POINT: ["N", "S", "W", "E"],
}

DIRECTIONS_OFFSETS = {
    "N": (0, -1),
    "S": (0, 1),
    "W": (-1, 0),
    "E": (1, 0),
}

def get_pipe_directions(pipe: str) -> List[tuple[int, int]]:
    possible_directions = PIPE_TO_DIRECTIONS_MAPPING[pipe]

    return [DIRECTIONS_OFFSETS[possible_direction] for possible_direction in possible_directions]


if __name__ == '__main__':
    
    file = open('example-1.txt', 'r')
    map = [list(line.strip()) for line in file]
    file.close()

    starting_point = get_starting_point(map)
    print(f"Animal starts at position {starting_point}")

    current_value = None
    pipe_connections: Dict[Tuple[int, int], List[Tuple[int, int]]] = { # A dictionary which uses a tuple as a key and a list as value: { (1,1): [(0,1), (-1,1), (2,1), (1,0), (1,-1), (1,2)], ... }
        (starting_point): [],
    }

    for y, row in enumerate(map):
        for x, tile in enumerate(row):
            moves: List[Tuple[int, int]] = [] # A list of tuples: [(1,1), (2, 1), (3, 1)]...
            
            if tile not in PIPE_TO_DIRECTIONS_MAPPING:
                print('Not a pipe')
                continue

            possible_directions = get_pipe_directions(tile)
            moves = [(possible_direction[0] + x, possible_direction[1] + y) for possible_direction in possible_directions]

            for move in moves:
                if starting_point == move:
                    pipe_connections[starting_point].append((x, y))

            if starting_point != (x, y):
                pipe_connections[(x, y)] = moves

    distances: Dict[Tuple[int, int], int] = {(starting_point): 0}
    queue: Deque[Tuple[int, int]] = deque([starting_point])

    while queue:
        print(f"\nQueue: {queue}")
        current = queue.popleft()
        print(f"Current element: {current}")
        print(f"Connections for current element: {pipe_connections[current]}")
        for connection in pipe_connections[current]:
            if connection not in distances:
                distances[connection] = distances[current] + 1
                queue.append(connection)
        print(f"Distances: {distances}")

    print(f"\n\nMax distance: {max(distances.values())}")
