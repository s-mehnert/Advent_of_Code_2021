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

# calculate epsilon rate

epsilon_rate = "".join(["0" if binary == "1" else "1" for binary in gamma_rate])

# calculate result

result = int(gamma_rate, 2) * int(epsilon_rate, 2)
print(result)


#****************** Part 1 *****


# determine most common bit

def find_most_common_bit(array, position):
    for i in range(position-1, position):
        temp_binary = ""
        for binary in array:
            temp_binary += binary[i]
        zero_count = temp_binary.count("0")
        one_count = temp_binary.count("1")
        most_common = max(zero_count, one_count)
        if zero_count == one_count or most_common == one_count:
            return "1"
        else:
            return "0"

# filter binary numbers

def filter_binary_list_for_most_common(array):
    for i in range(len(array[0])):
        if len(array) == 1:
            return array[0]
        keep = find_most_common_bit(array, i+1)
        array = [binary for binary in array if binary[i] == keep]
    return array[0]
        
# calculate oxygen generator rating

oxygen_generator_rating = filter_binary_list_for_most_common(import_input_data)

print(oxygen_generator_rating)

# reverse functions for calculation of CO2 scrubber rating

def filter_binary_list_for_least_common(array):
    for i in range(len(array[0])):
        if len(array) == 1:
            return array[0]
        keep = find_most_common_bit(array, i+1)
        if keep == "1":
            keep = "0"
        else:
            keep = "1"
        array = [binary for binary in array if binary[i] == keep]
    return array[0]

co2_scrubber_rating = filter_binary_list_for_least_common(import_input_data)

print(co2_scrubber_rating)
