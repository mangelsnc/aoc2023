#!/usr/bin/python3

import re

file = open("input.txt", "r")

durations = [int(duration) for duration in re.findall(r"\d+", file.readline())]
distances = [int(distance) for distance in re.findall(r"\d+", file.readline())]
file.close()

total = 1
for duration, distance in zip(durations, distances):
    print("Duration: %d - Distance: %d" % (duration, distance))
    solutions_counter = 0
    
    for i in range(1, duration + 1):
        if i * (duration - i) > distance:
            solutions_counter += 1

    print("Total solutions: %d" % solutions_counter)
    total *= solutions_counter

print("\nAnswer: %d" % total)
