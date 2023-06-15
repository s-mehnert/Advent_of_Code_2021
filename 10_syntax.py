#***** ADVENT OF CODE 2021 *****
#************ DAY 10 ************
#****************** Part 1 *****


# get input data

import_input_data = list()

with open("10_syntax_input.txt") as input:
    for line in input.readlines():
        import_input_data.append(line.strip("\n"))

print(import_input_data)
for line in import_input_data:
    print(line)