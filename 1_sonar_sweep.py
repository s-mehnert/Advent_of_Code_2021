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

increase_count = 0
current_data = sonar_data[0]
for measurement in sonar_data:
    if measurement > current_data:
        increase_count += 1
    current_data = measurement

# output result

print("Number of times the depth measurement increases:", increase_count)
