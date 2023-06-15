#***** ADVENT OF CODE 2021 *****
#************ DAY 10 ************
#****************** Part 1 *****


# get input data

import_input_data = list()

with open("10_syntax_input.txt") as input:
    for line in input.readlines():
        import_input_data.append(line.strip("\n"))

opening_chunk = ["(", "[", "{", "<"]
closing_chunk = [")", "]", "}", ">"]
pairs = ["()", "[]", "{}", "<>"]

# simulate stack

def check_for_corrupted_lines(chunk_list):
    check_stack = list()
    for char in chunk_list:
        if char in opening_chunk:
            check_stack.append(char)
        elif check_stack[-1] + char in pairs:
            check_stack.pop()
        else:
            return char
    
# find corrupted lines

errors_found = list()

for line in import_input_data:
    errors_found.append(check_for_corrupted_lines(line))

final_errors = [error for error in errors_found if error]
print("\nList of errors found:", final_errors)

# count syntax errors

count_dict = {")": 0, "]": 0, "}": 0, ">": 0}

for error in final_errors:
        count_dict[error] = final_errors.count(error)

print("\nCount of errors:", count_dict)

# find score

scores = {")": 3, "]": 57, "}": 1197, ">": 25137}

total_syntax_error_score = 0

for key, value in count_dict.items():
    if value > 0:
        total_syntax_error_score += value * scores[key]

print("\nTotal syntax error score:", total_syntax_error_score)

    
#****************** Part 2 *****


# filter out incomplete lines

def return_if_incomplete(chunk_list):
    check_stack = list()
    for char in chunk_list:
        if char in opening_chunk:
            check_stack.append(char)
        elif check_stack[-1] + char in pairs:
            check_stack.pop()
        else:
            return
    if check_stack:
        return check_stack
    
incomplete_lines = list()

for line in import_input_data:
    status = return_if_incomplete(line)
    if status:
        incomplete_lines.append(status)

print()
for line in incomplete_lines:
    print(line)

# autocomplete lines

counterparts = {"(": ")", "[": "]", "{": "}", "<": ">"}

def autocomplete_line(incomplete_line):
    repair_stack = incomplete_line[:]
    end_of_line = list()
    while repair_stack:
        left_half = repair_stack.pop()
        right_half = counterparts[left_half]
        end_of_line.append(right_half)
    return end_of_line

completion_lines = list()
for line in incomplete_lines:
    completion_line = autocomplete_line(line)
    completion_lines.append(completion_line)

print()
for line in completion_lines:
    print(line)

# create function to calculate autocomplete score

autocomplete_scores = {")": 1, "]": 2, "}": 3, ">": 4}

def calculate_autocomplete_score(completion_line):
    score = 0
    for char in completion_line:
        score *= 5
        score += autocomplete_scores[char]
    return score

score_list = list()

for line in completion_lines:
    score_list.append(calculate_autocomplete_score(line))

print()
for score in score_list:
    print(score)

# find the middle score

