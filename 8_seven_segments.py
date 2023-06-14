#***** ADVENT OF CODE 2021 *****
#************ DAY 8 ************
#****************** Part 1 *****


# get input data

import_input_data = list()

with open("8_seven_segments_input.txt") as input:
    for line in input.readlines():
        import_input_data.append(line.strip("\n").split(" | "))

print(import_input_data)
for line in import_input_data:
    print(line)

output_digits = [entry[1].split() for entry in import_input_data]

print(output_digits)
for output in output_digits:
    print(output)

# find unique digits

unique_digit_count = 0 

for output in output_digits:
    for digit in output:
        if len(digit) in [2, 3, 4, 7]:
            unique_digit_count += 1

print("Unique digit count:", unique_digit_count)