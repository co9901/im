from edge import Edge

class Node:

  #id
  #name
  #inEdges
  #outEdges
  #extraInfluence

  def __init__(self, id, name):
    self.id = id
    self.name = name
    self.inEdges = []
    self.outEdges = []

  def __repr__(self):
    return self.name

  def getId(self):
    return self.id

  def getName(self):
    return self.name

  def getInEdges(self):
    return self.inEdges
  
  def getOutEdges(self):
    return self.outEdges

  def addInEdge(self, edge):
    self.inEdges.append(edge)

  def addOutEdge(self, edge):
    self.outEdges.append(edge)
  
  def getInDegree(self):
    return len(self.inEdges)

  def getOutDegree(self):
    return len(self.outEdges)

  def setExtraInfluence(self, extraInfluence):
    self.extraInfluence = extraInfluence

  def getExtraInfluence(self):
    return self.extraInfluence

