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

submarine_pos = [0, 0]
for instr in instructions:
    if instr[0] == "f":
        submarine_pos[0] += instr[1]
    elif instr[0] == "d":
        submarine_pos[1] += instr[1]
    elif instr[0] == "u":
        submarine_pos[1] -= instr[1]
    else:
        print("Sorry, cannot carry out instruction")

result = submarine_pos[0] * submarine_pos[1]

# output result

print(f"\nThe new submarine position is {submarine_pos} and the resulting calculation is {result}.\n")


#****************** Part 2 *****


# adapt position calculation

submarine_data = [0, 0, 0]
for instr in instructions:
    if instr[0] == "f":
        submarine_data[0] += instr[1]
        submarine_data[1] += instr[1] * submarine_data[2]
    elif instr[0] == "d":
        submarine_data[2] += instr[1]
    elif instr[0] == "u":
        submarine_data[2] -= instr[1]
    else:
        print("Sorry, cannot carry out instruction")

result_2 = submarine_data[0] * submarine_data[1]

# output result

print(f"\nThe new submarine position is {submarine_data[:2]} and the resulting calculation is {result_2}.\n")

