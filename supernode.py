from node import Node
from edge import Edge

class Supernode:

  #id
  #nodes
  #inEdges
  #OutEdges

  def __init__(self, id):
    self.id = id
    self.nodes = []
    self.inEdges = []
    self.outEdges = []

  def setNodes(self, nodes):
    self.nodes = nodes
    for v in nodes:
      self.inEdges += v.getInEdges()
      self.outEdges += v.getOutEdges()

