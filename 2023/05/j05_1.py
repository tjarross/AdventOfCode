import re


seeds = []
seed_to_soil = {"start_ranges": [], "destination_ranges": []}
soil_to_fertilizer = {"start_ranges": [], "destination_ranges": []}
fertilizer_to_water = {"start_ranges": [], "destination_ranges": []}
water_to_light = {"start_ranges": [], "destination_ranges": []}
light_to_temperature = {"start_ranges": [], "destination_ranges": []}
temperature_to_humidity = {"start_ranges": [], "destination_ranges": []}
humidity_to_location = {"start_ranges": [], "destination_ranges": []}


def get_seed_location(seed: int):
    soil = seed
    for i, r in enumerate(seed_to_soil["start_ranges"]):
        if seed in r:
            soil = seed_to_soil["destination_ranges"][i][seed_to_soil["start_ranges"][i].index(seed)]
            break
    
    fertilizer = soil
    for i, r in enumerate(soil_to_fertilizer["start_ranges"]):
        if soil in r:
            fertilizer = soil_to_fertilizer["destination_ranges"][i][soil_to_fertilizer["start_ranges"][i].index(soil)]
            break
    
    water = fertilizer
    for i, r in enumerate(fertilizer_to_water["start_ranges"]):
        if fertilizer in r:
            water = fertilizer_to_water["destination_ranges"][i][fertilizer_to_water["start_ranges"][i].index(fertilizer)]
            break
    
    light = water
    for i, r in enumerate(water_to_light["start_ranges"]):
        if water in r:
            light = water_to_light["destination_ranges"][i][water_to_light["start_ranges"][i].index(water)]
            break
    
    temperature = light
    for i, r in enumerate(light_to_temperature["start_ranges"]):
        if light in r:
            temperature = light_to_temperature["destination_ranges"][i][light_to_temperature["start_ranges"][i].index(light)]
            break
    
    humidity = temperature
    for i, r in enumerate(temperature_to_humidity["start_ranges"]):
        if temperature in r:
            humidity = temperature_to_humidity["destination_ranges"][i][temperature_to_humidity["start_ranges"][i].index(temperature)]
            break
    
    location = humidity
    for i, r in enumerate(humidity_to_location["start_ranges"]):
        if humidity in r:
            location = humidity_to_location["destination_ranges"][i][humidity_to_location["start_ranges"][i].index(humidity)]
            break

    return location


def parse_ranges(lines: list):
    start_range_list = []
    destination_range_list = []
    for line in lines:
        if line == "":
            break
        destination_range, start_range, range_length = line.split()
        start_range_list.append(range(int(start_range), int(start_range) + int(range_length)))
        destination_range_list.append(range(int(destination_range), int(destination_range) + int(range_length)))
    return start_range_list, destination_range_list


def main():
    global seeds
    with open("input.txt") as file:
        lines = file.read().split("\n")[:-1]
        
        for  i, line in enumerate(lines):
            if line.startswith("seeds:"):
                seeds = re.match(r"seeds: ((\d+\s?)+)", lines[0]).group(1).split()
            if line == "seed-to-soil map:":
                start_range_list, destination_range_list = parse_ranges(lines[i + 1:])
                seed_to_soil["start_ranges"] = start_range_list
                seed_to_soil["destination_ranges"] = destination_range_list

            if line == "soil-to-fertilizer map:":
                start_range_list, destination_range_list = parse_ranges(lines[i + 1:])
                soil_to_fertilizer["start_ranges"] = start_range_list
                soil_to_fertilizer["destination_ranges"] = destination_range_list

            if line == "fertilizer-to-water map:":
                start_range_list, destination_range_list = parse_ranges(lines[i + 1:])
                fertilizer_to_water["start_ranges"] = start_range_list
                fertilizer_to_water["destination_ranges"] = destination_range_list

            if line == "water-to-light map:":
                start_range_list, destination_range_list = parse_ranges(lines[i + 1:])
                water_to_light["start_ranges"] = start_range_list
                water_to_light["destination_ranges"] = destination_range_list

            if line == "light-to-temperature map:":
                start_range_list, destination_range_list = parse_ranges(lines[i + 1:])
                light_to_temperature["start_ranges"] = start_range_list
                light_to_temperature["destination_ranges"] = destination_range_list

            if line == "temperature-to-humidity map:":
                start_range_list, destination_range_list = parse_ranges(lines[i + 1:])
                temperature_to_humidity["start_ranges"] = start_range_list
                temperature_to_humidity["destination_ranges"] = destination_range_list

            if line == "humidity-to-location map:":
                start_range_list, destination_range_list = parse_ranges(lines[i + 1:])
                humidity_to_location["start_ranges"] = start_range_list
                humidity_to_location["destination_ranges"] = destination_range_list

        print(min([get_seed_location(int(seed)) for seed in seeds]))
        

if __name__ == "__main__":
    main()