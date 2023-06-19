#***** ADVENT OF CODE 2021 *****
#************ DAY 13 ***********
#****************** Part 1 *****


# get input data

import_input_data = list()

with open("13_origami_input.txt") as input:
    for line in input.readlines():
        import_input_data.append(line.strip("\n").split(","))

dot_distribution = [(int(line[0]), int(line[1])) for line in import_input_data]

print("\nDot distribution:")
for line in dot_distribution:
    print(line)

# get instructions

import_instructions = list()

with open("13_origami_instructions.txt") as instrs:
    for instr in instrs.readlines():
        import_instructions.append(instr.strip("\n").split())

decoded_instructions = list()

for instr in import_instructions:
    for part in instr:
        if "=" in part:
            decoded_instructions.append(part.split("="))

print("\nInstructions:")
for line in decoded_instructions:
    print(line)

