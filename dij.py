from collections import defaultdict

class Edge(object):
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight


class Graph(object):
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges


def dijkstra(graph, origin):
    seen = set()
    seen.add(origin)

    distances = defaultdict(lambda: 1000000)
    distances[origin] = 0

    while len(seen) < len(graph.nodes):
        next_min_weight = None
        next_edge = None

        for edge in graph.edges:
            if edge.v in seen and edge.w not in seen:
                if next_min_weight is None or distances[edge.v] + edge.weight < next_min_weight:
                    next_min_weight = distances[edge.v] + edge.weight
                    next_edge = edge

        seen.add(next_edge.w)
        distances[next_edge.w] = next_min_weight

    return distances


def parse_line(line):
    parts = [x for x in line.strip().split('\t') if x.strip()]

    if len(parts) < 2:
        return None, None

    v = int(parts[0])
    edges = []

    for part in parts[1:]:
        w, weight = [int(x) for x in part.split(',')]
        edges.append(Edge(v, w, weight))

    return v, edges


def main():
    with open("dij.txt") as f:
        lines = f.readlines()

    nodes = []
    edges = []

    for line in lines:
        try:
            node, more = parse_line(line)
        except Exception:
            continue
        if node is not None:
            nodes.append(node)
            edges += more

    print dijkstra(Graph(nodes, edges), 1)


if __name__ == '__main__':
    main()

