#***** ADVENT OF CODE 2021 *****
#************ DAY 1 ************
#****************** Part 1 *****


# get input data
import_input_data = list()

with open("1_sonar_sweep_input.txt") as input:
    import_input_data = input.readlines()

sonar_data = list()
for line in import_input_data:
    sonar_data.append(int(line.strip("\n")))

# perform calculations

def get_increase_count(data):
    increase_count = 0
    current_data = data[0]
    for measurement in data:
        if measurement > current_data:
            increase_count += 1
        current_data = measurement
    return increase_count

# output result

print("Number of times the depth measurement increases:", get_increase_count(sonar_data))

