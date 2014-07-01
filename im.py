import sys
from node import Node
from edge import Edge
from graph import Graph

#G graph
#seedCount

G = Graph()
seedCount = 0

def main(k):
  global seedCount
  global G
  seedCount = k

  generalGreedy()
  G.draw()

def initialize(filename):
  global G

  file = open(filename,'r')
  for line in file:
    elements = line.split()
    if elements[0] == "node":
      n = Node(elements[1], elements[2])
      G.addNode(n)
    elif elements[0] == "edge":
      e = Edge(elements[1])
      G.addEdge(e, elements[2], elements[3])


def generalGreedy():
  global G
  global seedCount

  for i in range(0,seedCount):
    candidates = list(set(G.getNodes())-set(G.getSeeds()))
    for v in candidates:
      v.setExtraInfluence(0)
      results = []
      for s in G.getSeeds():
        cascade(s, results)
      cascade(v, results)
      v.setExtraInfluence(len(results))
    G.addSeed(getMaximumNode(candidates))

def cascade(seed, results): ##DFS
  if seed not in results:
    results.append(seed)
    for e in seed.getOutEdges():
      dest = e.getDest()
      if dest not in results:
        results.append(dest)
        cascade(dest, results)


def getMaximumNode(nodes):
  max = nodes[0]
  for v in nodes:
    if v.getExtraInfluence() > max.getExtraInfluence():
      max = v
  return max


if __name__ == "__main__":
  initialize(sys.argv[2])
  main(int(sys.argv[1]))



