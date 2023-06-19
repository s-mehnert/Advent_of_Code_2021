#***** ADVENT OF CODE 2021 *****
#************ DAY 14 ***********
#****************** Part 1 *****


# get input data

import_input_data = list()

with open("14_polymerization_rules.txt") as rules:
    for line in rules.readlines():
        import_input_data.append(line.strip("\n").split(" -> "))

print()
print(import_input_data)

polymer_template = "NNCB"

# create pair insertion dictionary

rules_dict = {rule[0] : rule[1] for rule in import_input_data}

print()
for pair, rule in rules_dict.items():
    print(pair, " -> ", rule)


# create polymer class

# create method to automatically insert values between pairs simultaneously

# create method to calculate desired result taking in number of steps as parameter




