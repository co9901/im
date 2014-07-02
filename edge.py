class Edge:

  #id 
  #src 
  #dest 
  #prob 
  #valid
  #status

  STATUS_ACTIVATION = "activation"
  STATUS_INHIBITION = "inhibition"

  def __init__(self, id, status):
    from node import Node
    self.id = id
    self.prob = 1
    self.valid = False
    self.status = status
  
  def setSrc(self, src):
    self.src = src

  def setDest(self, dest):
    self.dest = dest

  def setProb(self, prob):
    self.prob = prob

  def validate(self):
    self.valid = True

  def invalidate(self):
    self.valid = False

  def getId(self):
    return self.id

  def getSrc(self):
    return self.src

  def getDest(self):
    return self.dest

  def getProb(self):
    return self.prob

  def isActivation(self):
    return self.status == Edge.STATUS_ACTIVATION

  def isInhibition(self):
    return self.status == Edge.STATUS_INHIBITION

  def isValid(self):
    return self.valid

