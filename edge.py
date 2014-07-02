class Edge:

  #id 
  #src 
  #dest 
  #prob 
  #activation

  def __init__(self, id):
    from node import Node
    self.id = id
    self.prob = 1
  
  def setSrc(self, src):
    self.src = src

  def setDest(self, dest):
    self.dest = dest

  def setProb(self, prob):
    self.prob = prob

  def getId(self):
    return self.id

  def getSrc(self):
    return self.src

  def getDest(self):
    return self.dest

  def getProb(self):
    return self.prob

  def isActivation(self):
    return self.activation

