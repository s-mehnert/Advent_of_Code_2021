#***** ADVENT OF CODE 2021 *****
#************ DAY 13 ***********
#****************** Part 1 *****


# get input data

import_input_data = list()

with open("13_origami_input.txt") as input:
    for line in input.readlines():
        import_input_data.append(line.strip("\n").split(","))

dot_distribution = [(int(line[0]), int(line[1])) for line in import_input_data]

print("\nDot distribution:")
for line in dot_distribution:
    print(line)

# get instructions

import_instructions = list()

with open("13_origami_instructions.txt") as instrs:
    for instr in instrs.readlines():
        import_instructions.append(instr.strip("\n").split())

decoded_instructions = list()

for instr in import_instructions:
    for part in instr:
        if "=" in part:
            decoded_instructions.append(part.split("="))

print("\nInstructions:")
for line in decoded_instructions:
    print(line)


# create class Grid with positions

class Grid:
    def __init__(self, num_cols, num_rows):
        self.num_cols = num_cols
        self.num_rows = num_rows
        self.matrix = [[(col, row) for col in range(num_cols)] for row in range(num_rows)]
        self.dots = list()
    
    def add_dot(self, x, y):
        print("Adding dot in position:", (x, y))
        self.dots.append((x, y))
    
    def print_grid(self):
        for row in range(self.num_rows):
            print()
            for col in range(self.num_cols):
                if self.matrix[row][col] in self.dots:
                    print(" # ", end="")
                else:
                    print(" . ", end="")

# create class method fold up
    def fold_up(self, y):
        print("Folding up at row:", y)
        copied_dots = list()
        dots_to_remove = list()
        for dot in self.dots:
            if dot[1] > y:
                copied_dot = (dot[0], y - (dot[1]-y))
                copied_dots.append(copied_dot)
                dots_to_remove.append(dot)
        for new_dot in copied_dots:
            if new_dot not in self.dots:
                self.dots.append(new_dot)
        for old_dot in dots_to_remove:
            self.dots.remove(old_dot)

# create class method fold left

    def fold_left(self, x):
        print("Folding left at column:", x)
        copied_dots = list()
        dots_to_remove = list()
        for dot in self.dots:
            if dot[0] > x:
                copied_dot = (x -(dot[0]-x), dot[1])
                copied_dots.append(copied_dot)
                dots_to_remove.append(dot)
        for new_dot in copied_dots:
            if new_dot not in self.dots:
                self.dots.append(new_dot)
        for old_dot in dots_to_remove:
            self.dots.remove(old_dot)

# populate grid with dots from imported data

test_grid = Grid(100, 100)

for position in dot_distribution:
    test_grid.add_dot(*position)
print("\nBefore first fold:", len(test_grid.dots))

# pass instructions to grid

for instr in decoded_instructions:
    if instr[0] == "y":
        test_grid.fold_up(int(instr[1]))
    elif instr[0] == "x":
        test_grid.fold_left(int(instr[1]))
    else:
        print("Sorry, unknown instruction")

test_grid.print_grid()

print("\nNumber of dots left:", len(test_grid.dots))
