from collections import defaultdict
from functools import reduce
import re
import random

class Graph:
    """Undirected graph representation."""
    def __init__(self):
        """Creation of a graph object."""
        self.connections = defaultdict(set)

    def build_graph(self, pipes):
        """Out of a set of lines, create all edges."""
        for pipe in pipes:
            match = re.match(r"(.+) <-> (.+)", pipe)
            node, connections = match.group(1), match.group(2)
            for connection in connections.split(', '):
                self.add_edge(node, connection)

    def add_edge(self, a, b):
        """Add an undirected edge between a and b."""
        self.connections[a].add(b)
        self.connections[b].add(a)

    def get_cluster(self, root):
        """Return the cluster formed by all connected nodes to a root."""
        open_list = [root]
        cluster = set()
        while open_list:
            for node in open_list:
                cluster.add(node)
                open_list.remove(node)
                open_list += list(self.connections[node] - cluster)
        return cluster

    def n_clusters(self):
        """Return the number of different clusters in a graph."""
        all_nodes = set(self.connections.keys())
        clusters = []
        clusters_union = set()

        while clusters_union != all_nodes:
            new_root = random.sample(all_nodes - clusters_union, 1)[0]
            clusters.append(self.get_cluster(new_root))
            clusters_union = reduce(lambda x, acc: acc.union(x), clusters)

        return len(clusters)

def main():
    with open('src/day-12.txt', 'r') as f:
        pipes = f.readlines()

    graph = Graph()
    graph.build_graph(pipes)
    print('Solution to problem 1 is', len(graph.get_cluster('0')))
    print('Solution to problem 1 is', graph.n_clusters())


if __name__ == '__main__':
   main()
