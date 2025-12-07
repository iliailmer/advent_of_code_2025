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

# puzzle = read_puzzle("inputs/day_6/puzzle.txt")
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


def process_columns(problem: list):
    rows = len(problem) - 1  # ignore last row
    cols = len(problem[0])
    columns = []
    for c in range(cols):
        column = [deque(str(problem[i][c])) for i in range(rows)]
        max_string_len = len(max(column, key=lambda x: len(x)))
        for i in range(len(column)):
            column[i].extendleft(["" for _ in range(max_string_len - len(column[i]))])
        # column is len(column) x max_string_len array
        number = ""

        for col_idx in range(max_string_len):
            for row_idx in range(len(column)):
                number = number + column[row_idx][col_idx]
            print(number)
            number = ""
        columns.append(column)
    return columns


print(process_columns(problem)[0])
