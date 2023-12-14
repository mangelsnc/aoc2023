#!/usr/bin/env python3

from itertools import permutations, product, combinations
import re

def get_matches(string, groups):
    permutations = list(product('#.', repeat=string.count('?')))

    indices = [x.start() for x in re.finditer('\?', string)]

    permutated_strings = []
    for permutation in permutations:
        string_list = list(string)
        for replacement_char, index in zip(list(permutation), indices):
            string_list[index] = replacement_char
        
        permuted_string = ''.join(string_list)
        permutated_strings.append(permuted_string)
    
    pattern_tuple = ["#{%d}\.+" * len(groups)]
    pattern = "\.+".join(pattern_tuple)   
    pattern = pattern[:-1] % tuple(groups)

    regex_pattern = "^\.*%s*$" % (pattern)
    
    matches = 0
    for permuted_string in permutated_strings:
        if re.match(regex_pattern, permuted_string):
            matches += 1

    return matches

file = open('input.txt', 'r')

matches = 0
for line in file:
    (string, groups) = line.split(' ')
    groups = [int(i) for i in groups.split(',')]

    partial_matches = get_matches(string, groups)
    matches += partial_matches


print(matches)

file.close()
