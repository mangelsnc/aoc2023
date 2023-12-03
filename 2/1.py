#!/usr/bin/python3

import re

TOTAL_RED_CUBES = 12
TOTAL_GREEN_CUBES = 13
TOTAL_BLUE_CUBES = 14

file = open("input.txt", "r")

RE_GAME_ID = r"^Game (\d+)"
total_game_id = 0

for line in file:
    game_id = int(re.findall(RE_GAME_ID, line)[0])
    
    blue_cubes = True
    for cubes in re.findall(r"(\d+) blue", line):
        if int(cubes) > TOTAL_BLUE_CUBES:
            blue_cubes = False

    red_cubes = True
    for cubes in re.findall(r"(\d+) red", line):
        if int(cubes) > TOTAL_RED_CUBES:
            red_cubes = False

    green_cubes = True
    for cubes in re.findall(r"(\d+) green", line):
        if int(cubes) > TOTAL_GREEN_CUBES:
            green_cubes = False

    if blue_cubes and red_cubes and green_cubes:
        total_game_id += game_id

print(total_game_id)
file.close()
