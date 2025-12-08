import re
from collections import deque
from functools import reduce

puzzle = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""


def read_puzzle(path: str):
    with open(path) as f:
        return f.read()


def parse_puzzle(puzzle: str):
    rows = puzzle.strip().split("\n")
    output = []
    for row in rows:
        row = list(
            map(
                lambda x: int(x) if x.isnumeric() else x,
                re.sub(r"\s+", " ", row.strip()).split(),
            )
        )
        output.append(row)
    return output


def mult(a: int, b: int):
    return a * b


def add(a: int, b: int):
    return a + b


op_map = {"*": mult, "+": add}

puzzle = read_puzzle("inputs/day_6/puzzle.txt")
problem = parse_puzzle(puzzle)
rows = len(problem)
cols = len(problem[0])
solution = [0 for _ in range(cols)]
for j in range(cols):
    op = problem[rows - 1][j]
    out = problem[0][j]
    for i in range(1, rows - 1):
        out = op_map[op](out, problem[i][j])
    solution[j] = out

# part 1
print(sum(solution))

# part 2


def solve_puzzle_pt2(puzzle: str):
    lines = puzzle.strip().split("\n")
    columns = []
    last_line = lines[-1]
    start_col = [i for i, _ in enumerate(last_line) if last_line[i] != " "]
    for each_slice in zip(start_col, start_col[1:]):
        columns.append(
            [list(l[each_slice[0] : each_slice[-1] - 1]) for l in lines[:-1]]
        )
    columns.append([list(l[start_col[-1] :]) for l in lines[:-1]])
    numbers = []
    for col in columns:
        nums = []
        rows = len(col)
        cols = len(col[0])
        for c in range(cols):
            num = ""
            for r in range(rows):
                num += col[r][c]
            nums.append(int(num))
        numbers.append(nums)
    ops = [last_line[i] for i in start_col]
    total = 0
    for idx, each in enumerate(numbers):
        res = 0 if ops[idx] == "+" else 1
        for other in each:
            res = op_map[ops[idx]](res, other)
        total += res

    return total


# print(process_columns(problem)[0])
print(solve_puzzle_pt2(puzzle))
