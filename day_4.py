inputs = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""
"""
..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.
"""
with open("inputs/day_4/puzzle.txt") as f:
    inputs = f.read().strip()
puzzle = [list(line) for line in inputs.split("\n")]
# output = [list(line) for line in inputs.split("\n")]
rows = len(puzzle)
cols = len(puzzle[0])
total_removed = 0
while True:
    accessible = 0
    to_remove = []
    for r in range(rows):
        for c in range(cols):
            if puzzle[r][c] == "@":
                above_left = (
                    puzzle[r - 1][c - 1] == "@" if (r >= 1) and (c >= 1) else False
                )
                above = puzzle[r - 1][c] == "@" if (r >= 1) else False
                above_right = (
                    puzzle[r - 1][c + 1] == "@" if r >= 1 and c < cols - 1 else False
                )
                right = puzzle[r][c + 1] == "@" if c < cols - 1 else False
                below_right = (
                    puzzle[r + 1][c + 1] == "@"
                    if r < rows - 1 and c < cols - 1
                    else False
                )
                below = puzzle[r + 1][c] == "@" if r < rows - 1 else False
                below_left = (
                    puzzle[r + 1][c - 1] == "@" if r < rows - 1 and c >= 1 else False
                )
                left = puzzle[r][c - 1] == "@" if c >= 1 else False
                if (
                    above_left
                    + above
                    + above_right
                    + right
                    + below_right
                    + below
                    + below_left
                    + left
                ) < 4:
                    accessible += 1
                    to_remove.append([r, c])
    for r_rem, c_rem in to_remove:
        puzzle[r_rem][c_rem] = "."

    total_removed += accessible
    if accessible == 0:
        break
print(total_removed)
# print("\n".join(["".join(line) for line in output]))
