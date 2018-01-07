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

    distances = {origin: 0}
    for n in graph.nodes:
        if n != origin:
            distances[n] = 1000000

    
    while len(seen) < len(graph.nodes):
        min_from_seen = None
        next_edge = None

        for edge in graph.edges:
            if edge.v in seen and edge.w not in seen:
                if min_from_seen is None or distances[edge.v] + edge.weight < min_from_seen:
                    min_from_seen = distances[edge.v] + edge.weight
                    next_edge = edge

        seen.add(next_edge.w)
        distances[next_edge.w] = min_from_seen

    return distances


def parse_line(line):
    parts = [x for x in line.strip().split('\t') if x.strip()]
    if len(parts) < 2:
        return None, None
    v = int(parts.pop(0))
    edges = []
    for part in parts:
        p = [int(x) for x in part.split(',')]
        edges.append(Edge(v, p[0], p[1]))
    return v, edges


def main():
    with open("dij.txt") as f:
        lines = f.readlines()

        nodes = []
        edges = []
        for line in lines:
            node, more = parse_line(line)
            if node is not None:
                nodes.append(node)
                edges += more

    graph = Graph(nodes, edges)

    print dijkstra(graph, 1)

if __name__ == '__main__': main()
