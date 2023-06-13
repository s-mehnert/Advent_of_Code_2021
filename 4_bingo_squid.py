#***** ADVENT OF CODE 2021 *****
#************ DAY 3 ************
#****************** Part 1 *****


# get input data

import_input_data = list()

with open("4_bingo_squid_numbers.txt") as input:
    for line in input.readlines():
        import_input_data = line.strip("\n").split(",")

bingo_numbers = [int(num) for num in import_input_data]


import_board_data = list()

with open("4_bingo_squid_boards.txt") as boards:
    for line in boards.readlines():
        import_board_data.append(line.strip("\n"))

bingo_boards = list()

temp_board = list()

for i in range(len(import_board_data)):
    if import_board_data[i] == "":
        bingo_boards.append(temp_board)
        temp_board = list()
        continue
    board_line = [int(num) for num in import_board_data[i].split()]
    temp_board.append(board_line)
    if i == len(import_board_data)-1:
        bingo_boards.append(temp_board)
        temp_board = list()
    

# Testing

print(bingo_boards)
for board in bingo_boards:
    print()
    for line in board:
        print(line)
