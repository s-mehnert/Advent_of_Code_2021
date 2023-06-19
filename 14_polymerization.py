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

polymer_template = "VOKKVSKKPSBVOOKVCFOV"

# create pair insertion dictionary

rules_dict = {rule[0] : rule[1] for rule in import_input_data}

print()
for pair, rule in rules_dict.items():
    print(pair, " -> ", rule)


# create polymer class

class Polymer:
    def __init__(self, template):
        self.template = template
        self.growth = template[:]
        
# create method to automatically insert values between pairs simultaneously

    def grow(self, rules_dict, num_steps):
        for time in range(num_steps):
            insertions = self.growth[0]
            for i in range(len(self.growth)-1):
                insertions += (rules_dict[self.growth[i]+self.growth[i+1]] + self.growth[i+1])
            self.growth = insertions

# create method to calculate desired result taking in number of steps as parameter

    def calculate_result(self):
        count_dict = dict()
        for element in set(self.growth):
            count_dict[element] = self.growth.count(element)
        return max(count_dict.values()) - min(count_dict.values())
        

# Testing

test_polymer = Polymer(polymer_template)

print()
print(test_polymer.growth)

test_polymer.grow(rules_dict, 40)

print()
print(test_polymer.calculate_result())