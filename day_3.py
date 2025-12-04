def find_max_pair(line: list[int]):
    max_pair = 0
    for i in range(len(line) - 1):
        for j in range(i + 1, len(line)):
            pair = line[i] * 10 + line[j]
            if pair > max_pair:
                max_pair = pair
    return max_pair


def largest_subsequence(line, size=12):
    result = []
    allowed = len(line) - size
    for char in line:
        while result and str(char) > result[-1] and allowed > 0:
            result.pop()
            allowed -= 1
        result.append(str(char))

    return int("".join(result[:size]))


with open("inputs/day_3/puzzle.txt", "r") as f:
    puzzle = f.read().strip()
# puzzle = """987654321111111
# 811111111111119
# 234234234234278
# 818181911112111"""

# part 1
lines = list(map(lambda x: [int(y) for y in list(x)], puzzle.split("\n")))
print(sum([find_max_pair(each) for each in lines]))
print(sum([largest_subsequence(each, 2) for each in lines]))

# part 2

print(sum([largest_subsequence(each) for each in lines]))
