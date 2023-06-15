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
        self.flash_count = 0
    
    ### with method to increase energy
    def increase_energy_level(self):
        if self.energy_level != "*":
            if self.energy_level < 9:
                self.energy_level += 1
            else:
                self.flash()

    ### with method to flash
    def flash(self):
        self.energy_level = "*"
        self.flash_count += 1
        if self.neighbors:
            for octopus in self.neighbors:
                octopus.increase_energy_level()
    
    ### with method to reset energy level to zero
    def reset_energy_level(self):
        if self.energy_level == "*":
            self.energy_level = 0
    
    ### with method to add neighbors
    def add_neighbor(self, octopus):
        self.neighbors.append(octopus)

# fill grid with octopuses

matrix = [[Octopus(int(octopus)) for octopus in line] for line in import_input_data]

print("\nStart status:")
for row in matrix:
    print()
    for octopus in row:
        print(octopus.energy_level, end= " ")
print()

positions_in_matrix = [[(row, col) for col in range(len(matrix[0]))] for row in range(len(matrix))]

# establish neighboring relationships

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if i < len(matrix)-1:
            matrix[i][j].add_neighbor(matrix[i+1][j])
            if j < len(matrix[0])-1:
                matrix[i][j].add_neighbor(matrix[i][j+1])
                matrix[i][j].add_neighbor(matrix[i+1][j+1])
            if j > 0:
                matrix[i][j].add_neighbor(matrix[i][j-1])
                matrix[i][j].add_neighbor(matrix[i+1][j-1])
        if i > 0:
            matrix[i][j].add_neighbor(matrix[i-1][j])
            if j < len(matrix[0])-1:
                matrix[i][j].add_neighbor(matrix[i-1][j+1])
            if j > 0:
                matrix[i][j].add_neighbor(matrix[i-1][j-1])
        if i == len(matrix)-1:
            if j < len(matrix[0])-1:
                matrix[i][j].add_neighbor(matrix[i][j+1])
            if j > 0:
                matrix[i][j].add_neighbor(matrix[i][j-1])


#print()
#for octopus in matrix[4]:
#    print([octi.energy_level for octi in octopus.neighbors])
#print()

# create function to simulate one day

def simulate_day(matrix):
    for row in matrix:
        for octopus in row:
            octopus.increase_energy_level()
    for row in matrix:
        for octopus in row:
            octopus.reset_energy_level()
    return matrix

# for a count of x days increase energy level of all octopuses

list_of_days = list()
for i in range(100):
    simulate_day(matrix)

print("\nEnd status:")
for row in matrix:
    print()
    for octopus in row:
        print(octopus.energy_level, end=" ")
print()

# count how many times octopuses have flashed

total_flash_count = 0

for row in matrix:
    for octopus in row:
        total_flash_count += octopus.flash_count

print("\nTotal of flashes:", total_flash_count)