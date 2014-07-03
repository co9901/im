from node import Node
from edge import Edge
import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

class Graph:

  #graph Digraph
  #seeds
  #nodeGroups

  def __init__(self):
    self.graph = nx.DiGraph()
    self.seeds = []
    self.nodeGroups = {}

  def addNode(self, node):
    self.graph.add_node(node)

    if self.nodeGroups.has_key(node.getGeneName()):
      self.nodeGroups[node.getGeneName()].append(node)
    else:
      self.nodeGroups[node.getGeneName()] = [node]
    sorted(self.nodeGroups[node.getGeneName()], key=lambda n: n.getTime())

  def addEdge(self, edge, srcId, destId):
    src = self.getNode(srcId)
    dest = self.getNode(destId)
    if (src is not None and dest is not None):
      edge.setSrc(src)
      edge.setDest(dest)
      src.addOutEdge(edge)
      dest.addInEdge(edge)
      self.graph.add_edge(edge.getSrc(), edge.getDest(), {'instance':edge})

  def getNodes(self):
    return self.graph.node

  def getNode(self, id):
    for v in self.getNodes():
      if v.id == id:
        return v
    return None

  def getEdges(self):
    return [e[2]['instance'] for e in self.graph.edges(data=True)]

  def draw(self):
    nodeColor = ['r' if v.isUpRegulated() else 'b' for v in self.getNodes()]
    edgeColor = ['r' if e.isValid() else 'black' for e in self.getEdges()]

    pos = nx.graphviz_layout(self.graph, prog='dot')
    nx.draw(self.graph, pos, node_color=nodeColor, edge_color=edgeColor)
    plt.savefig("path.png")

  def getSeeds(self):
    return self.seeds

  def addSeed(self, seed):
    self.seeds.append(seed)

  def clearSeed(self):
    self.seeds = []

  def getSameNameNodes(self, geneName):
    return self.nodeGroups[geneName]

  def getValidNodeSet(self):
    validNodeGroups = {}
    for k in self.nodeGroups.keys():
      validSet = [n for n in self.nodeGroups[k] if n.isValid()]
      if len(validSet) > 0:
        validNodeGroups[k] = validSet
    return validNodeGroups



