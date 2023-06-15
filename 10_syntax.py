#***** ADVENT OF CODE 2021 *****
#************ DAY 10 ************
#****************** Part 1 *****


# get input data

import_input_data = list()

with open("10_syntax_input.txt") as input:
    for line in input.readlines():
        import_input_data.append(line.strip("\n"))

opening_chunk = ["(", "[", "{", "<"]
closing_chunk = [")", "]", "}", ">"]
pairs = ["()", "[]", "{}", "<>"]

# simulate stack

def check_for_corrupted_lines(chunk_list):
    check_stack = list()
    for char in chunk_list:
        if char in opening_chunk:
            check_stack.append(char)
        elif check_stack[-1] + char in pairs:
            check_stack.pop()
        else:
            print("Line corrupted. Wrong closing bracket found:", char)
            return char
    
# find corrupted lines

errors_found = list()

for line in import_input_data:
    errors_found.append(check_for_corrupted_lines(line))

print(errors_found)
    
