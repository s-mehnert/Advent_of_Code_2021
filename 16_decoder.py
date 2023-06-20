#***** ADVENT OF CODE 2021 *****
#************ DAY 16 ***********
#****************** Part 1 *****


# get input data

hexadecimal_string_old1 = "D2FE28"
hexadecimal_string_old12 = "38006F45291200"
hexadecimal_string = "8A004A801A8002F478"


dec_dict = {
    "0" : "0000",
    "1" : "0001",
    "2" : "0010",
    "3" : "0011",
    "4" : "0100",
    "5" : "0101",
    "6" : "0110",
    "7" : "0111",
    "8" : "1000",
    "9" : "1001",
    "A" : "1010",
    "B" : "1011",
    "C" : "1100",
    "D" : "1101",
    "E" : "1110",
    "F" : "1111"
    }


binary_string = ""
for char in hexadecimal_string:
    binary_string += dec_dict[char]

print(binary_string)
print(len(binary_string))

# create helper functions

def decode_header(binary_string):
    version = binary_string[:3]
    type_id = binary_string[3:6]
    rest_of_string = binary_string[6:]
    return version, type_id, rest_of_string

def decode_literal(rest_of_string):
    next_packet = rest_of_string[:5]
    literal = next_packet[1:]
    rest_of_string = rest_of_string[5:]
    while next_packet[0] == "1":
        next_packet = rest_of_string[:5]
        literal += next_packet[1:]
        rest_of_string = rest_of_string[5:]
    else:
        rest_of_string = rest_of_string[5:]
    return literal, rest_of_string

def decode_subpackets(subpackets):
    packets_decoded = list()
    while subpackets:
        packet_decoded, subpackets = decode_packet(subpackets)
        packets_decoded.append(packet_decoded)
    return packets_decoded

def decode_subpackets_2(rest_of_string, num_of_packets): # this one needs fixing all others are working
    packets_decoded = list()
    while len(packets_decoded) < num_of_packets:
        packet_decoded, rest_of_string = decode_packet(rest_of_string)
        packets_decoded.append(packet_decoded)
    return packets_decoded

def decode_packet(binary_string):
    packet_list = list()
    version, type_id, rest_of_string = decode_header(binary_string)
    packet_list.append(version)
    length_type = None
    literal = ""
    subpackets = ""
    if type_id == "100":
        literal, rest_of_string = decode_literal(rest_of_string)
        return packet_list, rest_of_string
    else: # all other types of packets are operator packets
        length_type = rest_of_string[0]
        if length_type == "0":
            length_in_bits = int(rest_of_string[1:16], 2)
            rest_of_string = rest_of_string[16:]
            subpackets = rest_of_string[:length_in_bits]
            rest_of_string = rest_of_string[length_in_bits:]
            return packet_list + decode_subpackets(subpackets), rest_of_string # make it work for more than one subpackets (if first is literal)
        else:
            num_of_packets = int(rest_of_string[1:12], 2)
            rest_of_string = rest_of_string[12:]
            subpackets = rest_of_string
            return packet_list + decode_subpackets_2(subpackets, num_of_packets), rest_of_string
        
packet_list = decode_packet(binary_string)[0]

print()
print(packet_list)

def flatten(lst):
    flat_lst = list()
    for item in lst:
        if isinstance(item, list):
            return flat_lst + flatten(item)
        flat_lst.append(item)
    return flat_lst


result_lst = flatten(packet_list)

result = 0
for item in result_lst:
    result += int(item, 2)

print(result)


# # decode the packets

# packet_list = list()

# version, type_id, rest_of_string = decode_header(binary_string)
# packet_list.append(int(version, 2))

# literal = ""
# length_type = None

# subpackets = ""

# if type_id == "100":
#     literal, rest_of_string = decode_literal(rest_of_string)

# else: # all other types of packets are operator packets
#     length_type = rest_of_string[0]
#     if length_type == "0":
#         length_in_bits = int(rest_of_string[1:16], 2)
#         rest_of_string = rest_of_string[16:]
#         subpackets = rest_of_string[:length_in_bits]
#         rest_of_string = rest_of_string[length_in_bits]
#     else:
#         num_of_packets = rest_of_string[1:12]
#         rest_of_string = rest_of_string[12:]
#         subpackets = rest_of_string


# print("Version:", version)
# print("Type:", type_id)
# print("Length Id:", length_type)
# print("Subpackets:", subpackets)
# print("Literal:", literal)
# print("Rest of string:", rest_of_string)
