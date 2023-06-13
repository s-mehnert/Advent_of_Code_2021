#***** ADVENT OF CODE 2021 *****
#************ DAY 6 ************
#****************** Part 1 *****


# input data

initial_lanternfish = [1,3,4,1,5,2,1,1,1,1,5,1,5,1,1,1,1,3,1,1,1,1,1,1,1,2,1,5,1,1,1,1,1,4,4,1,1,4,1,1,2,3,1,5,1,4,1,2,4,1,1,1,1,1,1,1,1,2,5,3,3,5,1,1,1,1,4,1,1,3,1,1,1,2,3,4,1,1,5,1,1,1,1,1,2,1,3,1,3,1,2,5,1,1,1,1,5,1,5,5,1,1,1,1,3,4,4,4,1,5,1,1,4,4,1,1,1,1,3,1,1,1,1,1,1,3,2,1,4,1,1,4,1,5,5,1,2,2,1,5,4,2,1,1,5,1,5,1,3,1,1,1,1,1,4,1,2,1,1,5,1,1,4,1,4,5,3,5,5,1,2,1,1,1,1,1,3,5,1,2,1,2,1,3,1,1,1,1,1,4,5,4,1,3,3,1,1,1,1,1,1,1,1,1,5,1,1,1,5,1,1,4,1,5,2,4,1,1,1,2,1,1,4,4,1,2,1,1,1,1,5,3,1,1,1,1,4,1,4,1,1,1,1,1,1,3,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,2,5,1,2,1,1,1,1,1,1,1,1,1]
test_list = [3,4,3,1,2]


# create fish

class Lanternfish:
    def __init__(self, internal_timer):
        self.internal_timer = internal_timer
        self.flock = 1
    
    def decrease_timer(self):
        self.internal_timer -= 1


#****************** Part 2 *****

    # fix this - count wrong
    def reproduce(self, duration):
        duration -= self.internal_timer
        self.flock += duration // 6
        print(f"Fish {self.internal_timer} reproduces {self.flock-1} times. New flock count: {self.flock} - Remaining duration {duration}")
        while duration > 6:
            duration -= 8
            self.flock += duration // 6
            print(f"The new fish reproduces as well. New flock count: {self.flock} - Remaining duration: {duration}")


test_fish_list = [Lanternfish(fish) for fish in test_list]
duration = 18
total_fish_count = 0
for fish in test_fish_list:
    print("Fish:", fish.internal_timer, " --> Flock:", fish.flock)
    fish.reproduce(duration)
    print("New flock count:", fish.flock)
    total_fish_count += fish.flock

print(total_fish_count)
    

# simulating 80 days

end_state_lanternfish = [Lanternfish(fish) for fish in initial_lanternfish]

duration = 80

for i in range(duration):
    num_of_new_fish = 0
    for fish in end_state_lanternfish:
        if fish.internal_timer == 0:
            num_of_new_fish += 1
            fish.internal_timer = 7
        fish.decrease_timer()
    for i in range(num_of_new_fish):
        end_state_lanternfish.append(Lanternfish(8))


#print(f"After {duration} days there are {len(end_state_lanternfish)} lanternfish.")



# optimizations

fish_count = len(test_list)
duration = 80
cycle_1 = 8
normal_cycle = 6

def get_additional_fish(fish, duration):
    additional_fish = 0
    if fish < duration:
        additional_fish += (duration-fish) // 6
        for i in range((duration-6)//6):
            additional_fish += get_additional_fish()
    return additional_fish

