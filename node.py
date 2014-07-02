from edge import Edge

class Node:

  #id
  #name
  #inEdges
  #outEdges
  #propagationEdges
  #extraInfluence
  #geneName
  #time
  #isUpRegulated
  #isDownRegulated
  #isConstant

  def __init__(self, id, name):
    self.id = id
    self.name = name
    self.inEdges = []
    self.outEdges = []
    self.propagationEdges = []
    self.isUpRegulated = False
    self.isDownRegulated = False 
    self.isConstant = False 

  def __repr__(self):
    return self.name

  def getId(self):
    return self.id

  def getName(self):
    return self.name

  def getGeneName(self):
    return self.geneName

  def getTime(self):
    return self.time

  def isUpRegulated(self):
    return self.isUpRegulated

  def isDownRegulated(self):
    return self.isDownRegulated

  def isConstant(self):
    return self.isConstant

  def getInEdges(self):
    return self.inEdges
  
  def getOutEdges(self):
    return self.outEdges

  def getPropagationEdges(self):
    return self.propagationEdges

  def addInEdge(self, edge):
    self.inEdges.append(edge)

  def addOutEdge(self, edge):
    self.outEdges.append(edge)

  def addPropagationEdges(self, edge):
    self.propagationEdges.append(edge)
  
  def getInDegree(self):
    return len(self.inEdges)

  def getOutDegree(self):
    return len(self.outEdges)

  def setExtraInfluence(self, extraInfluence):
    self.extraInfluence = extraInfluence

  def getExtraInfluence(self):
    return self.extraInfluence

