#***** ADVENT OF CODE 2021 *****
#************ DAY 7 ************
#****************** Part 1 *****


# input data

crab_subs_positions = [16,1,2,0,4,2,7,1,2,14]
crab_subs_positions.sort()


# calculate fuel efficiency

middle_idx = len(crab_subs_positions) // 2
front_idx = 1
back_idx = len(crab_subs_positions)-2

front_comp_value = crab_subs_positions[0]
back_comp_value = crab_subs_positions[-1]

while front_idx <= middle_idx:
    print(front_comp_value)
    front_comp_value = (front_comp_value + crab_subs_positions[front_idx]) // 2
    front_idx += 1

while back_idx >= middle_idx:
    print(back_comp_value)
    back_comp_value = (back_comp_value + crab_subs_positions[back_idx]) // 2
    back_idx -= 1

print()
print(front_comp_value)
print(back_comp_value)

median = (front_comp_value + back_comp_value) // 2

print("All crab submarines need to move to position:", median)

fuel_needed = sum([abs(position - median) for position in crab_subs_positions])

print("The total fuel cost amounts to:", fuel_needed)