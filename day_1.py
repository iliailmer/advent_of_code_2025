puzzle = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""


def part_1(puzzle: str) -> int:
    pw = 0
    dial = 50
    for line in puzzle.split("\n"):
        direction, num = line[0], int(line[1:])
        if direction == "L":
            dial -= num
        if direction == "R":
            dial += num
        dial = dial % 100
        if dial == 0:
            pw += 1
    return pw


def part_2(puzzle: str) -> int:
    pw = 0
    dial = 50
    for line in puzzle.split("\n"):
        direction, num = line[0], int(line[1:])
        if direction == "L":
            dial -= num
        if direction == "R":
            dial += num
        if dial < 0 or dial > 100:
            pw += 1
        dial = dial % 100
        if dial == 0:
            pw += 1
    return pw


if __name__ == "__main__":
    with open("inputs/day_1/puzzle_1.txt", encoding="utf8") as f:
        puzzle = f.read().strip()
    print(part_1(puzzle))
