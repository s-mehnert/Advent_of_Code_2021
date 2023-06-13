#***** ADVENT OF CODE 2021 *****
#************ DAY 4 ************
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
    

# play game

def mark_drawn_number(drawn_num, board):
    for row in range(len(board)):
        for num in range(len(board[0])):
            if board[row][num] == drawn_num:
                board[row][num] = -1
    return board


def check_bingo(board):
    cols = [[] for i in range(len(board))]
    for row in board:
        if sum(row) == -5:
            print("\n***** B I N G O *****")
            return True
        for i in range(len(board)):
            cols[i].append(row[i])
    for col in cols:
        if sum(col) == -5:
            print("\n***** B I N G O *****")
            return True
    return cols

def print_board(board):
    print()
    for row in board:
        print(row)

def get_score(board, last_num):
    points = 0
    for row in board:
        for num in row:
            if num > 0:
                points += num
    return points * last_num


#****************** Part 2 *****

last_number_drawn = None
winning_board = None
winning_score = None
copy_of_bingo_boards = bingo_boards.copy()

for num in bingo_numbers:
    print("\nNumber drawn:", num, "\n")
    boards_to_be_removed = list()
    for board in copy_of_bingo_boards:
        mark_drawn_number(num, board)
        last_number_drawn = num
        winning_board = board
        winning_score = get_score(winning_board, last_number_drawn)
        if check_bingo(board) is True:
            boards_to_be_removed.append(board)
    for board in boards_to_be_removed:
        copy_of_bingo_boards.remove(board)
    if not copy_of_bingo_boards:
        print("No more boards to check.")
        break
            
   
print("\nWinning board:\n")
print_board(winning_board)
print("\nLast number drawn:", last_number_drawn)
print("\nThe winning score is:", winning_score)
print()



# Testing

#print(bingo_boards)
#for board in bingo_boards:
#    print()
#    for line in board:
#        print(line)