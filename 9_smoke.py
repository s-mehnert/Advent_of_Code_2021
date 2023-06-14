#***** ADVENT OF CODE 2021 *****
#************ DAY 9 ************
#****************** Part 1 *****


# get input data

import_input_data = list()

with open("9_smoke_input.txt") as input:
    for line in input.readlines():
        import_input_data.append(line.strip("\n"))

matrix = [[int(char) for char in line] for line in import_input_data]

print()
print(matrix)
for row in matrix:
    print(row)


