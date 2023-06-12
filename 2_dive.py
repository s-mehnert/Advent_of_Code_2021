#***** ADVENT OF CODE 2021 *****
#************ DAY 2 ************
#****************** Part 1 *****


# get input data

import_input_data = list()

with open("2_dive_input.txt") as input:
    for line in input.readlines():
        import_input_data.append(line.strip("\n").split())
    
instructions = list()
for instr in import_input_data:
    instructions.append((instr[0][0], int(instr[1])))

# perform calculation


