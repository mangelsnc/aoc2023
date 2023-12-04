#!/usr/bin/python3

import string

file = open("example.txt", "r")

symbol_chars = string.digits + "."

line_count = 0
digits = []
lines = []

for line in file:
    lines.append(line)
    current_digit = ''
    
    for i in range(0, len(line)):
        if line[i].isdigit():
            current_digit += line[i]
        elif not line[i].isdigit() and len(current_digit) > 0:
            digit = current_digit
            starts_at = (i - len(digit))
            digits.append([int(digit), line_count, starts_at, i-1])
            current_digit = ''
        elif line[i] == '*':
            digits.append(['*', line_count, i, i])
            continue

    line_count += 1

print(digits)
total = 0

for digit_object in digits:
    digit = digit_object[0]
    line = digit_object[1]
    starts_at = digit_object[2]
    ends_at = digit_object[3]

    if digit != '*':
        continue
    
    print('gear found')

    for digit_object2 in digits:
        digit2 = digit_object[0]
        line2 = digit_object[1]
        starts_at2 = digit_object[2]
        ends_at2 = digit_object[3]



#    found = False
#    if line > 0:
#        for i in range((starts_at - 1), (ends_at + 1)):
#            if i < 0 or i > len(lines[line - 1]):
#                continue

#            if lines[line - 1][i] not in symbol_chars:
#                print("First rule: Add %d to total" % (digit))
#                total += digit
#                found = True
#                break

#    if line < (len(lines) - 1) and found == False:
#        for i in range((starts_at - 1), (ends_at + 1)):
#            if i < 0 or i > len(lines[line + 1]):
#                continue

#            if lines[line + 1][i] not in symbol_chars:
#                print("Second rule: Add %d to total" % (digit))
#                total += digit
#                found = True
#                break
    
#    if found == True:
#        continue

#    for i in range((starts_at - 1), (ends_at + 1)):
#        if i < 0 or i > len(lines[line]):
#            continue
        
#        if lines[line][i] not in symbol_chars:
#            print("Third rule: Add %d to total" % (digit))
#            total += digit
#            break

print(total)
file.close()
