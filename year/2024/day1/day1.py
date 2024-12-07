# Puzzle: https://adventofcode.com/2024/day/1


def convert_to_int(input_list):
    return [int(num) for num in input_list]


# Read the file and store columns in separate lists
def read_input(file_path):
    column1, column2 = [], []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            assert(len(parts) == 2)
            column1.append(parts[0])
            column2.append(parts[1])

    return convert_to_int(column1), convert_to_int(column2)

##########
# Part 1 #
##########
# col1, col2 = read_input("input.txt")
col1, col2 = read_input("/Users/nick/repos/AdventOfCode/year/2024/day1/input.txt")
assert(len(col1) == len(col2))

# Sort the lists
col1.sort()
col2.sort()

# Get the total distance
total_distance = sum([abs(x - y) for x, y in zip(col1, col2)])
print("Total Distance: ", total_distance)

##########
# Part 2 #
##########
def calc_similarity_score(list1, frequency):
    scores = []
    for val in list1:
        value = 0
        if frequency.get(val):
            value = val * frequency[val]
        scores.append(value)

    return scores

frequency = {num: col2.count(num) for num in set(col2)}
similarity_score = sum(calc_similarity_score(col1, frequency))
print("Similarity Score: ", similarity_score)
