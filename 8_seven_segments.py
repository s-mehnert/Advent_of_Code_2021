#***** ADVENT OF CODE 2021 *****
#************ DAY 8 ************
#****************** Part 1 *****


# get input data

import_input_data = list()

with open("8_seven_segments_input.txt") as input:
    for line in input.readlines():
        import_input_data.append(line.strip("\n").split(" | "))

output_digits = [entry[1].split() for entry in import_input_data]
input_digits = [entry[0].split() for entry in import_input_data]

# find unique digits

unique_digit_count = 0 

for output in output_digits:
    for digit in output:
        if len(digit) in [2, 3, 4, 7]:
            unique_digit_count += 1

#print("Unique digit count:", unique_digit_count)



#****************** Part 2 *****


# decipher digits

test_input = input_digits[0]
test_input.sort(key=len)
print(test_input)

digit_dict = dict()
position_dict = {"top": [], "middle": [], "bottom": [], "left_upper": [], "left_lower": [], "right_upper": [], "right_lower": []}
remaining_digits = test_input[:]
partly_deciphered = list()

for digit in test_input:
    if len(digit) == 2:
        digit_dict[1] = digit
        for char in digit:
            position_dict["right_upper"].append(char)
            position_dict["right_lower"].append(char)
            partly_deciphered.append(char)
        remaining_digits.remove(digit)
    elif len(digit) == 3:
        digit_dict[7] = digit
        for char in digit:
            if char not in digit_dict[1]:
                position_dict["top"] = char
        remaining_digits.remove(digit)
    elif len(digit) == 4:
        digit_dict[4] = digit
        for char in digit:
            if char not in digit_dict[1]:
                position_dict["middle"].append(char)
                position_dict["left_upper"].append(char)
                partly_deciphered.append(char)
        remaining_digits.remove(digit)
    elif len(digit) == 7:
        digit_dict[8] = digit
        remaining_digits.remove(digit)

five_digits = remaining_digits[:3]

for digit in five_digits:
    unknown_positions = list()
    for char in digit:
        if char not in position_dict.values() and char not in partly_deciphered:
            unknown_positions.append(char)
    if len(unknown_positions) == 1:
        position_dict["bottom"] = unknown_positions[0]
    break

for digit in five_digits:
    unknown_positions = list()
    for char in digit:
        if char not in position_dict.values() and char not in partly_deciphered:
            unknown_positions.append(char)
    if len(unknown_positions) == 1:
        position_dict["left_lower"] = unknown_positions[0]
        digit_dict[2] = digit
        remaining_digits.remove(digit)
        break

for char in digit_dict[2]:
    if char not in position_dict.values() and char in position_dict["middle"]:
        position_dict["middle"] = char
        partly_deciphered.remove(char)
        for entry in position_dict["left_upper"]:
            if entry != char:
                position_dict["left_upper"] = entry
                partly_deciphered.remove(entry)

for digit in remaining_digits[:2]:
    if position_dict["left_upper"] in digit:
        digit_dict[5] = digit
        remaining_digits.remove(digit)
        for entry in position_dict["right_lower"]:
            if entry in digit:
                position_dict["right_lower"] = entry
                partly_deciphered.remove(entry)
                for char in position_dict["right_upper"]:
                    if char != entry:
                        position_dict["right_upper"] = char
                        partly_deciphered.remove(char)

digit_dict[3] = remaining_digits.pop(0)

for digit in remaining_digits:
    if position_dict["middle"] not in digit:
        digit_dict[0] = digit
    elif position_dict["left_lower"] not in digit:
        digit_dict[9] = digit
    else:
        digit_dict[6] = digit

for key, value in sorted(digit_dict.items()):
    print(key, " --> ", value)

