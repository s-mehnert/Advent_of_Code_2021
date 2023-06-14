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

for entry in input_digits:
    entry.sort(key=len)

input_sorted = [["".join(sorted(digit)) for digit in entry] for entry in input_digits]
output_sorted = [["".join(sorted(digit)) for digit in entry] for entry in output_digits]


print()
for input in input_sorted:
    print(input)
print()
for output in output_sorted:
    print(output)
print()

# find unique digits

unique_digit_count = 0 

for output in output_digits:
    for digit in output:
        if len(digit) in [2, 3, 4, 7]:
            unique_digit_count += 1

#print("Unique digit count:", unique_digit_count)



#****************** Part 2 *****


# decipher digits

def decipher(input_digit):
    digit_dict = dict()
    position_dict = {"top": [], "middle": [], "bottom": [], "left_upper": [], "left_lower": [], "right_upper": [], "right_lower": []}
    remaining_digits = input_digit[:]
    partly_deciphered = list()
    #get first four digits
    for digit in input_digit:
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
    #get number 2
    five_digits = remaining_digits[:3]

    search_fives = "".join(five_digits)
    
    for char in search_fives:
        if char not in position_dict.values() and char not in partly_deciphered:
            if search_fives.count(char) == 3:
                position_dict["bottom"] = char
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
    return digit_dict

list_of_digit_dicts = list()
for input in input_sorted:
    list_of_digit_dicts.append(decipher(input))

print()
#compare_dict = decipher(input_digits[2])
#print()
#print(input_digits[3])
#print()
#test_dict = decipher(input_digits[3])


print()
for dict in list_of_digit_dicts:
    print()
    for key, value in dict.items():
        print(key, " --> ", value)

# invert digit_dict

list_of_inverted_digit_dicts = list()

for dictionary in list_of_digit_dicts:
    inverted_dict = {value : key for key, value in dictionary.items()}
    list_of_inverted_digit_dicts.append(inverted_dict)

for entry in list_of_inverted_digit_dicts:
    print(entry)

# decode outputs

def decode(output, dictionary):
    value = ""
    for digit in output:
        value += str(dictionary[digit])
    return value

# Testing

print(decode(output_sorted[0], list_of_inverted_digit_dicts[0]))