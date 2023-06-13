#***** ADVENT OF CODE 2021 *****
#************ DAY 5 ************
#****************** Part 1 *****


# get input data

import_input_data = list()

with open("5_hydrothermal_vents_input.txt") as input:
    for line in input.readlines():
        import_input_data.append(line.strip("\n").split(" -> "))


vent_lines = [[coord.split(",") for coord in line] for line in import_input_data]
vent_lines = [[tuple([int(xy) for xy in coord]) for coord in vent] for vent in vent_lines]

for line in vent_lines:
    print(line)

# create grid

grid = [[(x, y) for x in range(10)] for y in range(10)]

playing_grid = [[". " for coord in row] for row in grid]

def print_grid(grid):
    for row in grid:
        print()
        for coord in row:
            print(coord, end=" ")

print_grid(playing_grid)

