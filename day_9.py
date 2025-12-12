from collections import deque
from typing import NamedTuple

puzzle = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""


class Point(NamedTuple):
    x: int
    y: int


def area(point_1: Point, point_2: Point):
    return abs(point_1.x - point_2.x + 1) * abs(point_1.y - point_2.y + 1)


def part_1(puzzle):
    points = [
        Point(int(x), int(y))
        for (x, y) in map(lambda z: z.split(","), puzzle.split("\n"))
    ]
    n = len(points)
    answer = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            a = area(points[i], points[j])
            answer = max(answer, a)
    return answer


def part_2(puzzle: str):
    points = [
        Point(int(x), int(y))
        for x, y in map(lambda z: z.split(","), puzzle.split("\n"))
    ]

    answer = 0
    n = len(points)

    return answer


with open("inputs/day_9/puzzle.txt") as f:
    puzzle = f.read().strip()

print(part_1(puzzle))
