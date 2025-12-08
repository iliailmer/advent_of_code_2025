from collections import Counter

puzzle = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""


def read_puzzle(path: str):
    with open(path) as f:
        return f.read()


puzzle = read_puzzle("inputs/day_7/puzzle.txt")
# part 1


def part_1(puzzle: str):
    beams = [0 for _ in (puzzle.split("\n")[0])]
    beams[puzzle.split("\n")[0].index("S")] = 1
    total = 0
    for idx, line in enumerate(puzzle.split("\n")[1:]):
        for c_idx, c in enumerate(line):
            if c == "^":
                if beams[c_idx] == 1:
                    total += 1
                    beams[c_idx] = 0
                    beams[c_idx - 1] = 1
                    beams[c_idx + 1] = 1

    return total


def part_2(puzzle: str):
    beams = [0 for _ in (puzzle.split("\n")[0])]
    beams[puzzle.split("\n")[0].index("S")] = 1
    total = 0
    for idx, line in enumerate(puzzle.split("\n")[1:]):
        for c_idx, c in enumerate(line):
            if c == "^":
                beams[c_idx - 1] += beams[c_idx]  # however many rays went in
                beams[c_idx + 1] += beams[
                    c_idx
                ]  # same amount comes out through adjacent paths
                beams[c_idx] = 0

    return sum(beams)


print(part_1(puzzle))
print(part_2(puzzle))
