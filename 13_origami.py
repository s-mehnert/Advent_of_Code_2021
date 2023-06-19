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
        print(self.dots)
        copied_dots = list()
        dots_to_remove = list()
        for dot in self.dots:
            if dot[1] > y:
                print(dot)
                copied_dot = (dot[0], y - (dot[1]-y))
                print("Copying dot:", copied_dot)
                copied_dots.append(copied_dot)
                dots_to_remove.append(dot)
        for new_dot in copied_dots:
            if new_dot not in self.dots:
                self.dots.append(new_dot)
        for old_dot in dots_to_remove:
            self.dots.remove(old_dot)

# create class method fold left


# populate grid with dots from imported data

test_grid = Grid(15, 30)

for row in test_grid.matrix:
    print(row)

for position in dot_distribution:
    test_grid.add_dot(*position)
test_grid.print_grid()

test_grid.fold_up(7)
test_grid.print_grid()

# create new grid half the size with merged dots
