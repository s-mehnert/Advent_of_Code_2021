#***** ADVENT OF CODE 2021 *****
#************ DAY 11 ************
#****************** Part 1 *****


# get input data

import_input_data = list()

with open("11_octopus_input.txt") as input:
    for line in input.readlines():
        import_input_data.append(line.strip("\n"))


# create octopus class

class Octopus:
    def __init__(self, energy_level):
        self.energy_level = energy_level
        self.neighbors = list()
    
    ### with method to increase energy
    def increase_energy_level(self):
        if self.energy_level != "*":
            if self.energy_level < 9:
                self.energy_level += 1
            else:
                self.flash()

    ### with method to flash
    def flash(self):
        print("Octopus flashing ...")
        self.energy_level = "*"
        if self.neighbors:
            for octopus in self.neighbors:
                octopus.increase_energy_level()
    
    ### with method to reset energy level to zero
    def reset_energy_level(self):
        self.energy_level = 0
    
    ### with method to add neighbors
    def add_neighbor(self, octopus):
        self.neighbors.append(octopus)

# fill grid with octopuses

matrix = [[Octopus(int(octopus)) for octopus in line] for line in import_input_data]

print()
for row in matrix:
    print()
    for octopus in row:
        print(octopus.energy_level, end= " ")
print()

positions_in_matrix = [[(row, col) for col in range(len(matrix[0]))] for row in range(len(matrix))]

# establish neighboring relationships



# create function to simulate one day

# 1 - for a count of 100 days increase energy level of all octopuses
# 2 - after each day reset the energy level of the octopuses that flashed in the last step


# create function to mark flashed octopusses (so as not to increase them due to neighboring flashes)

# create function to find neighboring octopusses in matrix (in order to increase their count)
