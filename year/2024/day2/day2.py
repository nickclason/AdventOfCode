# Puzzle: https://adventofcode.com/2024/day/1

# Read input
def read_input(file_path):
    with open(file_path, 'r') as file:
        return [[int(num) for num in line.strip().split()] for line in file]


def calculate_valid_diff(level1, level2):
    min_diff = 1
    max_diff = 3
    level_diff = level2 - level1
    return level_diff, (abs(level_diff) >= min_diff) and (abs(level_diff) <= max_diff)


def is_level_order_valid(is_first, is_increasing, level1, level2):
    return ((is_first and level1 != level2) or 
            (is_increasing and level2 > level1) or 
            (not is_increasing and level2 < level1))


# Level is valid/"Safe" if:
#   - The levels are either all increasing or all decreasing.
#   - Any two adjacent levels differ by at least one and at most three.
def is_report_safe(report, problem_dampener=False):
    # [7, 6, 4, 3, 2]
    is_valid = False
    is_increasing = False

    report_len = len(report)
    num_problems = 0
    
    for level in range(report_len-1):
        current_level = report[level]
        next_level_index = level+1
        next_level = report[next_level_index]
        
        if (level < report_len-2):
            next_next_level_index = next_level_index+1

        is_order_valid = is_level_order_valid(level==0, is_increasing, current_level, next_level)
        if not is_order_valid and problem_dampener and (num_problems <= 1):
            if len(report[next_next_level_index]) != 0:
                is_order_valid = is_level_order_valid(level==0, is_increasing, current_level, report[next_next_level_index])
                next_level = report[next_next_level_index]
                num_problems += 1

        if ((num_problems <= 1) and is_order_valid):
            
            level_diff, is_valid_diff = calculate_valid_diff(current_level, next_level)
            if problem_dampener and (num_problems <= 1):
                if not is_valid_diff:
                    level_diff, is_valid_diff = calculate_valid_diff(current_level, report[next_next_level_index])
                    next_level = report[next_next_level_index]
                    num_problems += 1

            if is_valid_diff:
                is_increasing = level_diff > 0
                is_valid = True
            else:
                return False
        else:
            return False

    return is_valid

# Part 1
reports_list = read_input("input.txt")
# report_safeties = [is_report_safe(report, True) for report in reports_list]
# num_safe_reports = sum(1 for is_safe in report_safeties if is_safe)
# print("Number of Safe Reports: ", num_safe_reports )

# test_reports = [
#     [7, 6, 4, 2, 1],  # Safe without removing any level
#     [1, 2, 7, 8, 9],  # Unsafe regardless of which level is removed
#     [9, 7, 6, 2, 1],  # Unsafe regardless of which level is removed
#     [1, 3, 2, 4, 5],  # Safe by removing the second level, 3
#     [8, 6, 4, 4, 1],  # Safe by removing the third level, 4
#     [1, 3, 6, 7, 9]   # Safe without removing any level
# ]

# for report in test_reports:
#     is_safe = is_report_safe(report, True)
#     print("Is Report Safe: ", is_safe)

# Part 2
def check_safety(a):
  diffs = [a[i + 1] - a[i] for i in range(len(a) - 1)]    # build list of differences between consecutive pairs
  if (all(x < 0 and x in range(-3, 0) for x in diffs) or  # all differences are negative and between -3 and -1
      all(x > 0 and x in range(1, 4) for x in diffs)):    # all differences are positive and between 1 and 3
    return True
  else:
    return False

# read input_data from file
with open("input.txt", "r") as file:
  input_data = file.readlines()

total = 0
for line in input_data:
  nums = [int(num.strip()) for num in line.split()]
  if check_safety(nums):
    total += 1  # report is safe
  else:
    for i in range(len(nums)):
      temp_nums = nums.copy()
      temp_nums.pop(i)
      if check_safety(temp_nums):
        total += 1  # report is safe by removing a single level
        break

print(total)