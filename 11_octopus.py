#***** ADVENT OF CODE 2021 *****
#************ DAY 11 ************
#****************** Part 1 *****


# get input data

import_input_data = list()

with open("11_octopus_input.txt") as input:
    for line in input.readlines():
        import_input_data.append(line.strip("\n"))

print(import_input_data)
for line in import_input_data:
    print(line)


matrix = [[int(octopus) for octopus in line] for line in import_input_data]

print()
for row in matrix:
    print(row)
print()

positions_in_matrix = [[(row, col) for col in range(len(matrix[0]))] for row in range(len(matrix))]

print()
for row in positions_in_matrix:
    print(row)
print()


# create octopus class


### with method to increase energy

### with method to flash


# create function to simulate one day

# create function to mark flashed octopusses (so as not to increase them due to neighboring flashes)

# create function to find neighboring octopusses in matrix (in order to increase their count)
