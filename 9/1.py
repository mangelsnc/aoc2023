#!/usr/bin/env python3

import re

file = open('input.txt', 'r')

total = 0
for line in file:
    history = [int(i) for i in re.findall(r"\-?\d+", line.strip())]
   
    step = 0
    steps = [history]

    while(any(steps[step]) == True):
        new_history = []
        for i in range(0, len(steps[step]) - 1):
            new_history.append(steps[step][i + 1] - steps[step][i])
        step += 1
        steps.append(new_history)
    previous_step = None
    for step in reversed(steps):
        if previous_step == None:
            step.append(0)
        else:
            step.append(step[-1] + previous_step[-1])
        previous_step = step
    
    predicted_value = step[-1]
    total += predicted_value
    
print("Total final: %d" % total)
file.close()
