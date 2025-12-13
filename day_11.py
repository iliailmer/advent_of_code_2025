from collections import deque

puzzle = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out"""


class Graph:
    """Graph from Day 10, modified"""

    def __init__(self, puzzle: str) -> None:
        lines = puzzle.strip().split("\n")
        self.vertices = [x.split(": ")[0] for x in lines]
        self.edges = {}
        for line in lines:
            src, tgts = line.split(": ")
            tgts = tgts.split(" ")
            self.edges[src] = tgts

    def __repr__(self) -> str:
        return "\n".join(f"{k}: {' '.join(v)}" for k, v in self.edges.items())

    def get_neighbors(self, state):
        """Get all states reachable by pressing one button"""
        return self.edges.get(state, [])

    def _all_paths_bfs(self, start: str = "you", end: str = "out"):
        queue = deque([start])
        if start == end:
            return 0
        path_counter = 0
        while queue:
            vertex = queue.popleft()
            for neighbor in self.get_neighbors(vertex):
                if neighbor == end:
                    path_counter += 1
                queue.append(neighbor)

        return path_counter

    def _compute_reachable(self, target):
        """BFS to find all nodes that can reach target"""
        print(f"computing reachability for {target}")
        reachable = {target}
        queue = deque([target])

        while queue:
            node = queue.popleft()
            for v in self.vertices:  # Or however you iterate your graph
                if node in self.get_neighbors(v) and v not in reachable:
                    reachable.add(v)
                    queue.append(v)

        return reachable

    def _compute_reachable_from(self, source):
        """Find all nodes REACHABLE FROM source (forward BFS)"""
        reachable = {source}
        queue = deque([source])

        while queue:
            node = queue.popleft()
            for neighbor in self.get_neighbors(node):
                if neighbor not in reachable:
                    reachable.add(neighbor)
                    queue.append(neighbor)

        return reachable

    def _count_paths_dp(self, start="svr", end="out"):
        memo = {}

        def dp(node, seen_fft, seen_dac, visited):
            # Base case
            if node == end:
                return 1 if (seen_fft and seen_dac) else 0

            cache_key = (node, seen_fft, seen_dac)
            if cache_key in memo:
                return memo[cache_key]

            # Update flags
            seen_fft = seen_fft or (node == "fft")
            seen_dac = seen_dac or (node == "dac")

            visited.add(node)

            total = 0
            for neighbor in self.get_neighbors(node):
                if neighbor not in visited:
                    total += dp(neighbor, seen_fft, seen_dac, visited)

            visited.remove(node)

            memo[cache_key] = total
            return total

        return dp(start, False, False, set())


with open("./inputs/day_11/puzzle.txt") as f:
    puzzle = f.read()
g = Graph(puzzle)
print(g._all_paths_bfs())
print(g._count_paths_dp())
