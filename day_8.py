from functools import reduce


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
            self.size[root_x] += self.size[root_y]

        return True  # Successfully merged

    def get_size(self, x):
        return self.size[self.find(x)]

    def num_clusters(self):
        return len(set(self.find(i) for i in range(len(self.parent))))


puzzle = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""


def dist(x: list[int], y: list[int]) -> float:
    return (sum((x[i] - y[i]) ** 2 for i in range(len(x)))) ** (1 / 2)


def part_1(puzzle: str):
    points = [[int(y) for y in x.split(",")] for x in puzzle.strip().split("\n")]

    n = len(points)
    distances = []

    for i in range(n):
        for j in range(n):
            if i > j:
                distances.append([i, j, dist(points[i], points[j])])

    distances = sorted(distances, key=lambda x: x[-1])
    union = UnionFind(n)
    count = 0
    for d in distances:
        union.union(d[0], d[1])
        count += 1
        if count == 1000:
            break

    cluster_sizes = []
    for i in range(n):
        if union.find(i) == i:  # i is a root
            cluster_sizes.append(union.get_size(i))
    return reduce(lambda x, y: x * y, sorted(cluster_sizes, reverse=True)[:3])


def part_2(puzzle: str):
    points = [[int(y) for y in x.split(",")] for x in puzzle.strip().split("\n")]

    n = len(points)
    distances = []

    for i in range(n):
        for j in range(n):
            if i > j:
                distances.append([i, j, dist(points[i], points[j])])

    distances = sorted(distances, key=lambda x: x[-1])
    union = UnionFind(n)
    for d in distances:
        union.union(d[0], d[1])
        if union.num_clusters() == 1:
            return points[d[0]][0] * points[d[1]][0]


def read_puzzle(path: str):
    with open(path) as f:
        return f.read()


puzzle = read_puzzle("./inputs/day_8/puzzle.txt")
# print(part_1(puzzle))
print(part_2(puzzle))
