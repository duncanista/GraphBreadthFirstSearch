#encoding: utf-8
#coded by: duncanista / jordan gonzalez
import sys, subprocess, queue as qt, networkx as nx, matplotlib.pyplot as plot
from collections import defaultdict

it = iter(sys.stdin.read().splitlines())
s = next(it).split(" ")
graph = defaultdict(list)
coords = []
nodes = []

def checkLibraries():
    try:
        import networkx as nx
    except ImportError:
        install("networkx")
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        install("matplotlib")
def install(library):
    subprocess.call([sys.executable, "-m", "pip", "install", library])
def drawGraph(visited, current):
    graphBFS = nx.DiGraph()
    graphBFS.add_edges_from(coords)
    graphBFS.add_nodes_from(nodes)
    nodeColors = []
    for node in graphBFS:
        if node in visited:
            if node == current:
                nodeColors.append("green")
            else:
                nodeColors.append("red")
        else:
            nodeColors.append("yellow")
    nx.draw(graphBFS, node_color=nodeColors, with_labels=True)
    plot.show()
def breadthFirstSearch():
    queue = qt.Queue()
    nodesVisited = []
    root = nodes[0]
    queue.put(root)
    nodesVisited.append(root)
    drawGraph(nodesVisited, root)
    print(" --- Empezamos el recorrido de nuestro grafo --- ")
    iterations = 1
    while queue.qsize() > 0:
        nodeToCheck = queue.get()
        pointingNodes = graph[nodeToCheck]
        for node in pointingNodes:
            if node not in nodesVisited:
                nodesVisited.append(node)
                queue.put(node)

        print(" -------- Recorrido número {} -----------".format(iterations))
        print("| Popping node: {}".format(nodeToCheck))
        print("| Q =  {}".format(list(queue.queue)))
        print("| A = {} ".format(nodesVisited))
        print(" ----------------------------------------")
        drawGraph(nodesVisited, nodeToCheck)
        iterations += 1

# reading our input
for i in range(len(s)):
    pair = s[i].strip("()").split(",")
    node = pair[0]
    to = pair[1]
    # getting the coords
    tuple = (node, to)
    coords.append(tuple)
    # we append again the tuple but reversed, because it is an undirected graph
    coords.append(tuple[::-1])

    graph[node].append(to)
    nodes.append(node)
# we delete duplicates in our node list
nodes = list(set(nodes))
checkLibraries()
breadthFirstSearch()