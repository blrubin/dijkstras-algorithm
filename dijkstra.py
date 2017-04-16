'''
Brianna Rubin
'''

from collections import defaultdict

class Graph:
  def __init__(self):
    self.Queue = set()
    self.edges = defaultdict(list)
    self.distances = {}

  def addNode(self, value):
    self.Queue.add(value)

  def addEdge(self, fromNode, toNode, distance):
    self.edges[fromNode].append(toNode)
    self.edges[toNode].append(fromNode)
    self.distances[(fromNode, toNode)] = distance
    self.distances[(toNode, fromNode)] = distance


def dijsktra(graph, initial):
  marked = {initial: 0}
  previous = {}

  Queue = set(graph.Queue)

  while Queue != None:
    minNode = None
    for node in Queue:
      if node in marked:
        if minNode is None:
          minNode = node
        elif marked[node] < marked[minNode]:
          minNode = node

    if minNode is None:
      break

    Queue.remove(minNode)
    currentWeight = marked[minNode]

    for edge in graph.edges[minNode]:
      weight = currentWeight + graph.distances[(minNode, edge)]
      if edge not in marked or weight < marked[edge]:
        marked[edge] = weight
        previous[edge] = minNode

  print "Marked: ", marked
  print "Previous", previous

def main():
  graph = Graph()
  graph.addNode("A")
  graph.addNode("B")
  graph.addNode("C")
  graph.addNode("D")

  graph.addEdge("A","C",3)
  graph.addEdge("A","D",5)
  graph.addEdge("C","D",1)
  graph.addEdge("C","B",6)
  graph.addEdge("D","B",2)

  dijsktra(graph,"A")
main()
