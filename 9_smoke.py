#***** ADVENT OF CODE 2021 *****
#************ DAY 9 ************
#****************** Part 1 *****


# get input data

import_input_data = list()

with open("9_smoke_input.txt") as input:
    for line in input.readlines():
        import_input_data.append(line.strip("\n"))

matrix = [[int(char) for char in line] for line in import_input_data]

print()
for row in matrix:
    print(row)
print()

positions_in_matrix = [[(row, col) for col in range(len(matrix[0]))] for row in range(len(matrix))]

print()
for row in positions_in_matrix:
    print(row)
print()

# find low points

potential_low_points = list()
higher_points = list()
low_points = list()

# checking rows

for i in range(len(matrix)):
    potential_low_points_row = list()
    higher_points_row = list()
    for j in range(1, len(matrix[0]), 2):
        if j == len(matrix[0])-1:
            if matrix[i][j] < matrix[i][j-1] and (i, j) not in higher_points_row:
                potential_low_points_row.append((i, j))
            break
        if matrix[i][j] > matrix[i][j-1]:
            if j < 2 and (i, j-1) not in higher_points_row:
                potential_low_points_row.append((i, j-1))
            elif matrix[i][j-1] < matrix[i][j-2]:
                potential_low_points_row.append((i, j-1))
            higher_points_row.append((i, j))
        else:
            if (i, j) not in higher_points_row and matrix[i][j] < matrix[i][j+1]:
                potential_low_points_row.append((i, j))
                higher_points_row.append((i, j+1))
            higher_points_row.append((i, j-1))
    potential_low_points_row = list(set(potential_low_points_row))
    potential_low_points += potential_low_points_row
    higher_points_row = list(set(higher_points_row))
    higher_points += higher_points_row

# checking potential low points against columns

for plp in potential_low_points:
    i, j = plp
    if i < len(matrix)-1:
        if matrix[i][j] < matrix[i+1][j]:
            if i > 0:
                if matrix[i][j] < matrix[i-1][j]:
                    low_points.append(plp)
            else:
                low_points.append(plp)
    else:
        if matrix[i][j] < matrix[i-1][j]:
            low_points.append(plp)

print()
print(low_points)

# calculate risk level


risk_level_points = [matrix[i][j] for (i, j) in low_points]
risk_level = sum(risk_level_points) + len(risk_level_points)
print(risk_level_points)
print(len(risk_level_points))
print(len(low_points))

check_sum = 0
for point in risk_level_points:
    check_sum += point+1

print("Check sum:", check_sum, "plus 1 higher:", check_sum + len(low_points))



print()
print("The cumulated risk level of all low points is", risk_level)

            
print("".join(import_input_data).count("0"))
print(risk_level_points.count(0))
    



