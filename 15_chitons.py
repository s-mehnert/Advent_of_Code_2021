#***** ADVENT OF CODE 2021 *****
#************ DAY 15 ***********
#****************** Part 1 *****


# get input data

import_input_data = list()

with open("15_chitons_input.txt") as input:
    for line in input.readlines():
        import_input_data.append(list(line.strip("\n")))

cave_map = [[int(pos) for pos in line] for line in import_input_data]

print()
for row in cave_map:
    print(row)


# create a graph with risk level as weighted edges


# find lowest cost path through graph