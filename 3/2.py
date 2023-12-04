#!/usr/bin/python3

import string

file = open("input.txt", "r")

symbol_chars = string.digits + "."

line_count = 0
digits = []
lines = []
gears = []

for line in file:
    lines.append(line)
    current_digit = ''
    
    for i in range(0, len(line)):
        if line[i].isdigit():
            current_digit += line[i]
        
        if not line[i].isdigit() and len(current_digit) > 0:
            digit = current_digit
            starts_at = (i - len(digit))
            digits.append({ 
                "value": int(digit), 
                "line_number": line_count, 
                "start_pos": starts_at, 
                "end_pos": i-1
            })
            current_digit = ''
        
        if line[i] == '*':
            gears.append({
                "value": '*', 
                "line_number": line_count, 
                "position": i, 
            })
            continue

    line_count += 1

total = 0

for gear in gears:
    print("Gear L%d:%d" % (gear['line_number'], gear['position']))
    mult_digits = [] 
    for digit in digits:
        if digit['line_number'] == (gear['line_number'] - 1):
             if (digit['start_pos'] in range(gear['position'] - 1, gear['position'] + 2)) or (digit['end_pos'] in range(gear['position'] - 1, gear['position'] + 2)):
                mult_digits.append(digit['value'])

        if digit['line_number'] == (gear['line_number'] + 1):
             if (digit['start_pos'] in range(gear['position'] - 1, gear['position'] + 2)) or (digit['end_pos'] in range(gear['position'] - 1, gear['position'] + 2)):
                mult_digits.append(digit['value'])

        if digit['line_number'] == gear['line_number']:
            if digit['start_pos'] == gear['position'] + 1 or digit['end_pos'] == gear['position'] - 1:
                mult_digits.append(digit['value'])

    if len(mult_digits) == 2:
        total += mult_digits[0] * mult_digits[1]

print(total)
file.close()
