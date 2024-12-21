import re

# Part 1
mul_pattern = r"(mul\(\d+,\d+\))"
num_pattern = r"(\d+)"
file = "/Users/nick/repos/AdventOfCode/year/2024/day3/input.txt"

with open(file) as f:
    data = f.read()


def do_mult_op(mul_op):
    pattern=r"(\d+)"
    nums = re.findall(pattern, mul_op)
    assert(len(nums) == 2)

    multiplicand = int(nums[0])
    multiplier = int(nums[1])

    return multiplicand * multiplier

sum = 0
mul_op = re.finditer(mul_pattern, data)
for mul in mul_op:
    match = mul.group()
    sum += do_mult_op(match)

print("Part1: ", sum)

# Part 2
# part2_reg_exp = r"(do|don't)\(\)|mul\(\d+,\d+\)"
part2_reg_exp = r"(do|don't)\(\)|mul\(\d+,\d+\)"
do_mult = True # default is do_mult

do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"

part2_sum = 0
for idx, match in enumerate(re.finditer(part2_reg_exp, data), start=1):
    group = match.group()
    # print(f"Match {idx}: {group}")

    if re.fullmatch(mul_pattern, group):
        # print("mul() op")
        if do_mult:
            part2_sum += do_mult_op(group)
    elif re.fullmatch(do_pattern, group):
        # print("do() op")
        do_mult = True
    elif re.fullmatch(dont_pattern, group):
        # print("don't() op")
        do_mult = False

print(f"Part 2: {part2_sum}")