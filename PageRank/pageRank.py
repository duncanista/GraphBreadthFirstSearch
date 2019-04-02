#utf-8
#coded by Jordan Gonzalez

import sys
import networkx as nx
import matplotlib.pyplot as plot
from random import random
from collections import defaultdict

it = iter(sys.stdin.read().splitlines())
s = next(it).split(" ")
iterations = int(s.pop(0))
graph = defaultdict(list)
ranks = defaultdict(list)
coords = []

def drawGraph(coords, graph):
    graph = nx.DiGraph()
    graph.add_edges_from(coords)

    valuesMap = {}
    for node in graph:
        valuesMap[node] = random()

    values = [valuesMap.get(node, 0.25) for node in graph.nodes()]

    red_edges = coords
    black_edges = [edge for edge in graph.edges() if edge not in red_edges]

    position = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph, position, cmap=plot.get_cmap('jet'),
                           node_color=values, node_size=500)
    nx.draw_networkx_labels(graph, position)
    nx.draw_networkx_edges(graph, position, edgelist=red_edges, edge_color='r', arrows=True)
    nx.draw_networkx_edges(graph, position, edgelist=black_edges, arrows=False)
    plot.show()

def pageRank(graph, ranks):
    for node in graph:
        temporalRank = 0
        for pointing in graph:
            if(node in graph[pointing]):
                temporalRank += ranks[pointing] / float(len(graph[pointing]))
        ranks[node] = temporalRank
    return ranks

# reading file
for i in range(len(s)):
    pair = s[i].strip("()").split(",")
    node = pair[0]
    to = pair[1]
    tuple = (node, to)
    coords.append(tuple)
    graph[node].append(to)

# get length of graph
m = len(graph)

# round 01 for rank
for node in graph:
    ranks[node] = 1 / float(m)

for j in range(iterations):
    ranks = pageRank(graph, ranks)
print("==============================")
print("Resultado: ")
print("==============================")
for position in ranks:
    print("{} - {}".format(position, ranks[position]))
print("==============================")

drawGraph(coords, graph)




