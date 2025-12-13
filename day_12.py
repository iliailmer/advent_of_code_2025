puzzle = """0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2"""


def get_all_orientations(shape):
    """Get all rotations and flips of shape"""
    orientations = set()
    current = shape

    for _ in range(4):  # 4 rotations
        orientations.add(tuple(map(tuple, current)))
        orientations.add(tuple(map(tuple, flip_horizontal(current))))
        current = rotate_90(current)

    return [list(map(list, o)) for o in orientations]


def rotate_90(shape):
    """Rotate shape 90 degrees clockwise"""
    return [list(row) for row in zip(*shape[::-1])]


def flip_horizontal(shape):
    """Flip shape horizontally"""
    return [row[::-1] for row in shape]


def can_place(grid, shape, row, col):
    """Check if shape fits at position without overlapping"""
    for r, line in enumerate(shape):
        for c, char in enumerate(line):
            if char == "#":
                gr, gc = row + r, col + c
                # Check bounds and if cell is empty
                if gr >= len(grid) or gc >= len(grid[0]) or grid[gr][gc] != ".":
                    return False
    return True


def place(grid, shape, row, col, marker):
    """Place shape on grid with given marker"""
    for r, line in enumerate(shape):
        for c, char in enumerate(line):
            if char == "#":
                grid[row + r][col + c] = marker


def remove(grid, shape, row, col):
    """Remove shape from grid"""
    for r, line in enumerate(shape):
        for c, char in enumerate(line):
            if char == "#":
                grid[row + r][col + c] = "."


def can_fit_all_presents(width, height, shapes, required_counts):
    grid = [["." for _ in range(width)] for _ in range(height)]

    def backtrack(shape_idx):
        # Base case: all shapes placed
        if shape_idx >= len(required_counts):
            return True

        # Skip if we don't need any of this shape
        if required_counts[shape_idx] == 0:
            return backtrack(shape_idx + 1)

        # Get all rotations/flips of this shape
        shape = shapes[shape_idx]
        for rotated_shape in get_all_orientations(shape):
            # Try placing at every position
            for row in range(height):
                for col in range(width):
                    if can_place(grid, rotated_shape, row, col):
                        # Place it
                        place(grid, rotated_shape, row, col, str(shape_idx))
                        required_counts[shape_idx] -= 1

                        # Recurse - try placing remaining shapes
                        if backtrack(shape_idx):
                            return True

                        # Backtrack - didn't work, try another placement
                        remove(grid, rotated_shape, row, col)
                        required_counts[shape_idx] += 1

        # Couldn't place this shape anywhere
        return False

    return backtrack(0)


with open("./inputs/day_12/puzzle.txt") as f:
    puzzle = f.read()

lines = puzzle.strip().split("\n\n")
shapes = lines[:-1]
shape_list = []
regions = lines[-1].split("\n")
regions_parsed = []
counter = 0

for shape in shapes:
    shape = shape.split(":\n")[1]
    shape_list.append(shape.count("#"))

for r in regions:
    _area, _quantities = r.split(": ")
    _area = _area.split("x")
    width, height = int(_area[0]), int(_area[1])
    quantities = list(map(int, _quantities.split(" ")))
    if ((width // 3) * (height // 3)) >= sum(quantities):
        counter += 1
        continue
    region_area = width * height
    if region_area < sum(size * quant for (size, quant) in zip(shape_list, quantities)):
        continue


print(counter)
