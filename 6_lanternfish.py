#***** ADVENT OF CODE 2021 *****
#************ DAY 6 ************
#****************** Part 1 *****


# input data

initial_lanternfish = [3,4,3,1,2]


# create fish

class Lanternfish:
    def __init__(self, internal_timer):
        self.internal_timer = internal_timer
    
    def decrease_timer(self):
        self.internal_timer -= 1
    

# simulating 80 days

end_state_lanternfish = [Lanternfish(fish) for fish in initial_lanternfish]

print()
for fish in end_state_lanternfish:
    print(fish.internal_timer, end= ", ")

for i in range(80):
    num_of_new_fish = 0
    for fish in end_state_lanternfish:
        if fish.internal_timer == 0:
            num_of_new_fish += 1
            fish.internal_timer = 7
        fish.decrease_timer()
    for i in range(num_of_new_fish):
        end_state_lanternfish.append(Lanternfish(8))
    print("\nNumber of new fish:", num_of_new_fish)
    print([fish.internal_timer for fish in end_state_lanternfish])


print(f"After 80 days there are {len(end_state_lanternfish)} lanternfish.")
    