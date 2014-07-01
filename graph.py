from node import Node
from edge import Edge
import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

class Graph:

  #graph Digraph
  #seeds

  def __init__(self):
    self.graph = nx.DiGraph()
    self.seeds = []

  def addNode(self, node):
    self.graph.add_node(node)

  def addEdge(self, edge, srcId, destId):
    src = self.getNode(srcId)
    dest = self.getNode(destId)
    if (src is not None and dest is not None):
      edge.setSrc(src)
      edge.setDest(dest)
      src.addOutEdge(edge)
      dest.addInEdge(edge)
      self.graph.add_edge(edge.getSrc(), edge.getDest(), weight = edge.getProb())

  def getNodes(self):
    return self.graph.node

  def getNode(self, id):
    for v in self.getNodes():
      if v.id == id:
        return v
    return None

  def draw(self):
    nodeColor = []
    for v in self.graph.node:
      color = 'r' if v in self.seeds else 'b'
      nodeColor.append(color)
    nx.draw(self.graph, node_color=nodeColor)
    plt.savefig("path.png")

  def getSeeds(self):
    return self.seeds

  def addSeed(self, seed):
    self.seeds.append(seed)


