#***** ADVENT OF CODE 2021 *****
#************ DAY 16 ***********
#****************** Part 1 *****


# get input data

hexadecimal_string = "D2FE28"

hexadecimal_number = hex(int(hexadecimal_string, 16))

print(hexadecimal_number)

binary_number = bin(int(hexadecimal_string, 16))

print(binary_number)

binary_string = str(binary_number)[2:]

print(binary_string)
print(len(binary_string))

# create helper functions



# decode the packets

version = binary_string[:3]
type = binary_string[3:6]

rest_of_string = binary_string[6:]
literal = ""
if type == "100":
    next_packet = rest_of_string[:5]
    print("next", next_packet)
    literal += next_packet[1:]
    rest_of_string = rest_of_string[5:]
    while next_packet[0] == "1":
        next_packet = rest_of_string[:5]
        print("still next", next_packet)
        literal += next_packet[1:]
        rest_of_string = rest_of_string[5:]
    else:
        rest_of_string = rest_of_string[5:]

print(literal)
int_result = int(literal, 2)
print(int_result)

