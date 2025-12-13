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

    def _all_paths_dfs(self, start="svr", end="out"):
        paths = []
        path_count = [0]
        can_reach_fft = self._compute_reachable("fft")
        can_reach_dac = self._compute_reachable("dac")
        can_reach_end = self._compute_reachable(end)
        reachable_from_fft = self._compute_reachable_from("fft")
        reachable_from_dac = self._compute_reachable_from("dac")
        fft_then_dac_possible = (
            "dac" in reachable_from_fft and end in reachable_from_dac
        )
        dac_then_fft_possible = (
            "fft" in reachable_from_dac and end in reachable_from_fft
        )

        if not (fft_then_dac_possible or dac_then_fft_possible):
            print("No valid paths exist!")
            return 0
        print(f"Nodes that can reach fft: {len(can_reach_fft)}")
        print(f"Nodes that can reach dac: {len(can_reach_dac)}")
        print(f"Nodes that can reach end: {len(can_reach_end)}")

        def dfs(
            current_node: str,
            visited: set,
            seen_fft: bool,
            seen_dac: bool,
        ):
            if current_node not in can_reach_end:
                return
            if not seen_fft and current_node not in can_reach_fft:
                return
            if not seen_dac and current_node not in can_reach_dac:
                return

            if current_node == "fft" and not seen_fft:
                if "dac" not in reachable_from_fft:
                    return
            if current_node == "dac" and not seen_dac and not seen_fft:
                if "fft" not in reachable_from_dac:
                    return
            if seen_fft and not seen_dac:
                if "dac" not in reachable_from_fft:
                    return

            if seen_dac and not seen_fft:
                if "fft" not in reachable_from_dac:
                    return

            visited.add(current_node)
            seen_fft = seen_fft or (current_node == "fft")
            seen_dac = seen_dac or (current_node == "dac")
            if current_node == end:
                if seen_fft and seen_dac:
                    print(path_count[0])
                    path_count[0] += 1
            else:
                for neighbor in self.get_neighbors(current_node):
                    if neighbor not in visited:
                        dfs(
                            neighbor,
                            visited,
                            seen_dac=seen_dac,
                            seen_fft=seen_fft,
                        )
            visited.remove(current_node)

        dfs(start, set(), False, False)
        return path_count[0]


puzzle = """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out"""
with open("./inputs/day_11/puzzle.txt") as f:
    puzzle = f.read()
g = Graph(puzzle)
print(g._all_paths_bfs())
print(g._all_paths_dfs())
