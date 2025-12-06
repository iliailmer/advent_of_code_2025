inputs = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""


def read_input(path: str):
    with open(path) as f:
        inputs = f.read().strip()
    return parse_input(inputs)


def parse_ranges(ranges: list[str]) -> list[tuple[int, int]]:
    return [(int(x.split("-")[0]), int(x.split("-")[1])) for x in ranges]


def parse_ids(ids: list[str]) -> list[int]:
    return list(map(int, ids))


def parse_input(inputs: str) -> tuple[list[tuple[int, int]], list[int]]:
    ranges, ids = inputs.split("\n\n")

    return parse_ranges(ranges.split("\n")), parse_ids(ids.split("\n"))


def merge_intervals(ranges: list[tuple[int, int]]):
    def overlap(int1, int2):
        if int1[1] < int1[0] or int1[0] > int2[1]:
            return False
        if (
            (int1[0] <= int2[0] <= int1[1])
            or (int1[0] <= int2[1] <= int1[1])
            or (int2[0] <= int1[0] <= int2[1])
            or (int2[0] <= int1[1] <= int2[1])
        ):
            return True

    def _merge(int1, int2):
        start = min(int1[0], int2[0])
        end = max(int1[1], int2[1])
        return (start, end)

    ranges = sorted(ranges)
    out = [ranges[0]]

    for interval in ranges[1:]:
        if out[-1][1] >= interval[0]:
            out[-1] = _merge(out[-1], interval)
        else:
            out.append(interval)
    return out


ranges, ids = read_input("inputs/day_5/puzzle.txt")
# ranges, ids = parse_input(inputs)
ranges = merge_intervals(ranges)

# part 1
counter = 0
for each_id in ids:
    for rng in ranges:
        if rng[0] <= each_id <= rng[1]:
            counter += 1
            break
print(counter)

# part 2
print(sum([end - start + 1 for (start, end) in ranges]))
