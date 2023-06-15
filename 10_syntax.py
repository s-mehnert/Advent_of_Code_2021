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

errors_found = list()

# simulate stack

check_stack = list()

for char in import_input_data[0]:
    if char in opening_chunk:
        check_stack.append(char)
    elif check_stack[-1] + char in pairs:
        check_stack.pop()
    else:
        print("Line corrupted. Wrong closing bracket found:", char)
        errors_found.append(char)

print(check_stack)