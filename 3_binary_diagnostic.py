#***** ADVENT OF CODE 2021 *****
#************ DAY 3 ************
#****************** Part 1 *****


# get input data

import_input_data = list()

with open("3_binary_diagnostic_input.txt") as input:
    for line in input.readlines():
        import_input_data.append(line.strip("\n"))

# calculate gamma rate

gamma_rate = ""

for i in range(len(import_input_data[0])):
    temp_binary = ""
    for binary in import_input_data:
        temp_binary += binary[i]
        zero_count = temp_binary.count("0")
        one_count = temp_binary.count("1")
    most_common = max(zero_count, one_count)
    if most_common == zero_count:
        gamma_rate += "0"
    else:
        gamma_rate += "1"

