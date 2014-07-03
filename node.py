from edge import Edge

class Node:

  #id
  #name
  #inEdges
  #outEdges
  #extraInfluence
  #geneName
  #time
  #status
  #valid

  STATUS_UP = "up"
  STATUS_DOWN = "down"
  STATUS_CONST = "constant"
  

  def __init__(self, id, name, status):
    self.id = id
    self.name = name
    self.status = status
    self.inEdges = []
    self.outEdges = []
    self.valid = False

    names = name.split('_')
    self.geneName = names[0]
    self.time = int(names[len(names)-1])

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
    return self.status == Node.STATUS_UP

  def isDownRegulated(self):
    return self.status == Node.STATUS_DOWN

  def isConstant(self):
    return self.status == Node.STATUS_CONST

  def getStatus(self):
    return self.status

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

  def isValid(self):
    return self.valid

  def validate(self):
    self.valid = True

  def invalidate(self):
    self.valid = False

