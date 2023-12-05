#!/usr/bin/python3

import re

file = open("input.txt", "r")
content = file.read()

seeds_raw = re.findall(r"^seeds: ((\d+\s?)*)", content)
seeds = [int(i) for i in seeds_raw[0][0].strip().split()]

seed_to_soil_map_raw = re.findall(r"seed-to-soil map:\n((\d+\s?)*)", content)
seed_to_soil_map = []
for mapping in seed_to_soil_map_raw[0][0].strip().split('\n'):
    seed_to_soil_map.append([int(i) for i in mapping.split()])

soil_to_fertilizer_map_raw = re.findall(r"soil-to-fertilizer map:\n((\d+\s?)*)", content)
soil_to_fertilizer_map = []
for mapping in soil_to_fertilizer_map_raw[0][0].strip().split('\n'):
    soil_to_fertilizer_map.append([int(i) for i in mapping.split()])

fertilizer_to_water_map_raw = re.findall(r"fertilizer-to-water map:\n((\d+\s?)*)", content)
fertilizer_to_water_map = []
for mapping in fertilizer_to_water_map_raw[0][0].strip().split('\n'):
    fertilizer_to_water_map.append([int(i) for i in mapping.split()])

water_to_light_map_raw = re.findall(r"water-to-light map:\n((\d+\s?)*)", content)
water_to_light_map = []
for mapping in water_to_light_map_raw[0][0].strip().split('\n'):
    water_to_light_map.append([int(i) for i in mapping.split()])

light_to_temperature_map_raw = re.findall(r"light-to-temperature map:\n((\d+\s?)*)", content)
light_to_temperature_map = []
for mapping in light_to_temperature_map_raw[0][0].strip().split('\n'):
    light_to_temperature_map.append([int(i) for i in mapping.split()])

temperature_to_humidity_map_raw = re.findall(r"temperature-to-humidity map:\n((\d+\s?)*)", content)
temperature_to_humidity_map = []
for mapping in temperature_to_humidity_map_raw[0][0].strip().split('\n'):
    temperature_to_humidity_map.append([int(i) for i in mapping.split()])

humidity_to_location_map_raw = re.findall(r"humidity-to-location map:\n((\d+\s?)*)", content)
humidity_to_location_map = []
for mapping in humidity_to_location_map_raw[0][0].strip().split('\n'):
    humidity_to_location_map.append([int(i) for i in mapping.split()])

resources = []
maps = [seed_to_soil_map, soil_to_fertilizer_map, fertilizer_to_water_map, water_to_light_map, light_to_temperature_map, temperature_to_humidity_map, humidity_to_location_map]

for seed in seeds:
    resource = seed

    for map in maps:
        for range in map:
            destination_range_start = int(mapping[0])
            source_range_start = int(mapping[1])
            range_length = int(mapping[2])
            
            if resource >= source_range_start and resource < (source_range_start + range_length):
                range_shift = destination_range_start - source_range_start
                resource += range_shift
                break
    
    resources.append(resource)
    
print(min(resources))

file.close()
