from collections import Counter


test_input = [
    "start-A",
    "start-b",
    "A-c",
    "A-b",
    "b-d",
    "A-end",
    "b-end",
]

puzzle_input = [
    "pf-pk",
    "ZQ-iz",
    "iz-NY",
    "ZQ-end",
    "pf-gx",
    "pk-ZQ",
    "ZQ-dc",
    "NY-start",
    "NY-pf",
    "NY-gx",
    "ag-ZQ",
    "pf-start",
    "start-gx",
    "BN-ag",
    "iz-pf",
    "ag-FD",
    "pk-NY",
    "gx-pk",
    "end-BN",
    "ag-pf",
    "iz-pk",
    "pk-ag",
    "iz-end",
    "iz-BN",
]


class Graph:
    def __init__(self, edges) -> None:
        self.graph = {}
        for edge in edges:
            nodes = edge.split("-")
            self.addToGraph(nodes[0], nodes[1])
            self.addToGraph(nodes[1], nodes[0])
        self.number_of_nodes = len(self.graph)

    def __str__(self) -> str:
        return str(self.graph)

    def addToGraph(self, source_node: str, dest_node: str) -> None:
        if source_node in self.graph:
            self.graph[source_node].append(dest_node)
        else:
            self.graph[source_node] = [dest_node]


cave_map = Graph(puzzle_input)

paths = []


def has_small_cave_visited_twice(path: list) -> bool:
    counter = Counter(filter(lambda node: node.lower() == node, path))
    return 2 in counter.values()


def find_path(source: str, destination: str, path: list, visited_twice: bool):
    if (
        # condition for part 2
        (path and source == "start")
        or visited_twice
        # end condition for part 2
        and source.lower() in path
    ):
        return

    path.append(source)

    if not visited_twice:
        visited_twice = has_small_cave_visited_twice(path)

    if source == destination:
        paths.append(",".join(path))
    else:
        for node in cave_map.graph[source]:
            find_path(
                node,
                destination,
                path,
                visited_twice,
            )

    path.pop()
    if visited_twice:
        visited_twice = has_small_cave_visited_twice(path)


find_path("start", "end", [], False)

print(f"Number of paths found: {len(paths)}")
