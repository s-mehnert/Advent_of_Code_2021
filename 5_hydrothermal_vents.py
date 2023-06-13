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

# create grid

grid = [[(x, y) for x in range(1000)] for y in range(1000)]

playing_grid = [["." for coord in row] for row in grid]

def print_grid(grid):
    for row in grid:
        print()
        for coord in row:
            print(coord, end=" ")

# mark vent lines in grid

def mark_vents(vent_line, grid):
    start_x = vent_line[0][0]
    end_x = vent_line[1][0]
    start_y = vent_line[0][1]
    end_y = vent_line[1][1]
    if start_y == end_y:
        print("Horizontal vent line found")
        for i in range(min(start_x, end_x), max(start_x, end_x)+1):
            if grid[start_y][i] == ".":
                print("New vent found")
                grid[start_y][i] = "1"
            else:
                print("Overlapping vent lines found")
                num = int(grid[start_y][i])
                grid[start_y][i] = str(num + 1)
    elif start_x == end_x:
        print("Vertical vent line found")
        for i in range(min(start_y, end_y), max(start_y, end_y)+1):
            if grid[i][start_x] == ".":
                print("New vent found")
                grid[i][start_x] = "1"
            else:
                print("Overlapping vent lines found")
                num = int(grid[i][start_x])
                grid[i][start_x] = str(num + 1)
    else:
        print("Diagonal vent line found. Skipping...")
    return grid

# mark vent lines in grid

print()
for vent_line in vent_lines:
    print(vent_line)
    mark_vents(vent_line, playing_grid)

print()
print_grid(playing_grid)

# find extra dangerous coordinates

extra_danger_count = 0

print()
for row in playing_grid:
    for coord in row:
        if coord not in [".", "1"]:
            extra_danger_count += 1

print()
print("Danger count:", extra_danger_count)
