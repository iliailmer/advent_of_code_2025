from collections import deque
from itertools import product

puzzle = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""


def parse_puzzle(puzzle: str):
    lines = [x.split(" ") for x in puzzle.strip().split("\n")]
    indicators = []
    buttons = []
    joltages = []
    for x in lines:
        indicators.append(x[0])
        buttons.append(x[1:-1])
        joltages.append(x[-1])
    return indicators, buttons, joltages


class Graph:
    def __init__(self, indicators: str, buttons: list[str]) -> None:
        self.end_state = self.state_from_string(indicators.strip("[]"))
        self.vertices = []
        self.edges = {}
        self._build(indicators, buttons)

    def state_from_string(self, state_str):
        """Convert string like '.##.' to state tuple"""
        return tuple(c == "#" for c in state_str)

    def state_to_string(self, state):
        """Convert state tuple to string like '.##.'"""
        return "".join("#" if b else "." for b in state)

    def _build(self, indicators: str, buttons: list[str]):
        indicators = indicators.strip("[]")
        n = len(indicators)
        self.start_state = tuple(False for _ in range(n))
        for vertex in product([False, True], repeat=n):
            self.vertices.append(tuple(vertex))
        for v in self.vertices:
            neighbors = []
            for button in buttons:
                new_vertex = self._push_button(list(v), button)
                neighbors.append(new_vertex)
            self.edges[v] = neighbors

    def _push_button(self, indicator: list[bool], button: str):
        light_ids = [int(x) for x in button.strip("()").split(",")]
        for idx in light_ids:
            if idx < len(indicator):
                indicator[idx] = not indicator[idx]
        return tuple(indicator)

    def get_neighbors(self, state):
        """Get all states reachable by pressing one button"""
        return self.edges.get(state, [])

    def _shortest_path(self):
        start = self.start_state
        queue = deque([(start, 0)])
        if start == self.end_state:
            return 0
        visited = {start}
        while queue:
            current_state, distance = queue.popleft()

            for neighbor_state in self.get_neighbors(current_state):
                if neighbor_state == self.end_state:
                    return distance + 1

                if neighbor_state not in visited:
                    visited.add(neighbor_state)
                    queue.append((neighbor_state, distance + 1))

        return -1  # unreachable


with open("./inputs/day_10/puzzle.txt") as f:
    puzzle = f.read()

indicators, buttons, joltages = parse_puzzle(puzzle)


def part_1(indicators, buttons):
    graphs = [Graph(i, b) for i, b in zip(indicators, buttons)]
    answer = sum([g._shortest_path() for g in graphs])
    return answer


print(part_1(indicators, buttons))
