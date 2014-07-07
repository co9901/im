import sys
import time
from node import Node
from edge import Edge
from graph import Graph

#G graph
#seedCount
#inputFileName
#outputFileName

G = Graph()
seedCount = 0
runningTimes = {}

def main():

  global G

  validatePath()
  weightedCascade('weightedCascade')
  #printPropagationPath('w')
  #generalGreedy('generalGreedy')
  #printResults('a', 'generalGreedy')
  #degreeDiscountRough('degreeDiscountRough')
  #printResults('a', 'degreeDiscountRough')

def initialize(k,inputName,outputName):
  global G
  global seedCount
  global inputFileName
  global outputFileName

  seedCount = k
  inputFileName = inputName
  outputFileName = outputName


  inputFile = open(inputFileName,'r')
  for line in inputFile:
    elements = line.split()
    if elements[0] == "node":
      n = Node(elements[1], elements[2], elements[3])
      G.addNode(n)
    elif elements[0] == "edge":
      e = Edge(elements[1], elements[4])
      G.addEdge(e, elements[2], elements[3])
  inputFile.close()

def printPropagationPath(mode):
  global outputFileName
  outputFile = open(outputFileName, mode)
  outputFile.write("propagated :\n")

  validNodeSet = G.getValidNodeSet()
  for k in validNodeSet.keys():
    outputFile.write(k)
    for n in validNodeSet[k]:
      outputFile.write(" " + str(n.getTime()))
    outputFile.write("\n")

  outputFile.write("========\n")
  outputFile.close()

def printResults(mode, method):
  global G
  global outputFileName
  global runningTimes

  G.draw()
  outputFile = open(outputFileName, mode)
  outputFile.write(method + " : " + str(runningTimes[method]) + "s\n")
  outputFile.write("Seed :\n")
  for s in G.getSeeds():
    outputFile.write(s.getId() + " " + s.getName() + "\n")

  outputFile.write("========\n")
  outputFile.close()

def weightedCascade(method):
  global G
  global seedCount
  global runningTimes

  G.clearSeed()

  startTime = time.time()


  for i in range(0,seedCount):
    for v in G.getNodes():
      v.setExtraInfluence(0)
      v.setIndex(-1)
      v.setLowlink(-1)
    result = collapse(G) 


  runningTimes[method] = round(time.time() - startTime,2)

def collapse(G):
  index = [0]
  result = []
  stack = [] 

  def strongConnect(v):
    v.setIndex(index[0])
    v.setLowlink(index[0])
    index[0] += 1
    stack.append(v)

    for e in v.getOutEdges():
      w = e.getDest()
      if w.getIndex() < 0:
        strongConnect(w)
        v.setLowlink(min(v.getLowlink(), w.getLowlink()))
      elif w in stack:
        v.setLowlink(min(v.getLowlink(), w.getLowlink()))

    if v.getLowlink() == v.getIndex():
      ## start a new strongly connected component ??
      temp = []
      while True:
        w = stack.pop()
        temp.append(w) 
        if w == v:
          break
      result.append(temp)

  for v in G.getNodes():
    if v.getIndex() < 0:
      strongConnect(v)

  return result

def degreeDiscountRough(method):
  global G
  global seedCount
  global runningTimes

  G.clearSeed()

  startTime = time.time()
  for v in G.getNodes():
    v.setSeedNeighborCount(0)
    v.setExtraInfluence(v.getValidOutDegree())

  candidates = list(set(G.getNodes())-set(G.getSeeds()))
  for i in range(0,seedCount):
    u = getMaximumNode(candidates)
    G.addSeed(u)
    candidates.remove(u)
    for e in u.getInEdges():
      neighbor = e.getSrc()
      neighbor.setSeedNeighborCount(neighbor.getSeedNeighborCount()+1)
      neighbor.setExtraInfluence(neighbor.getValidOutDegree()-neighbor.getSeedNeighborCount() if neighbor.getExtraInfluence() > 0 else -1)
    for e in u.getOutEdges():
      dest = e.getDest()
      dest.setExtraInfluence(-1)

  runningTimes[method] = round(time.time() - startTime,2)


def generalGreedy(method):
  global G
  global seedCount
  global runningTimes

  G.clearSeed()

  startTime = time.time()
  candidates = list(set(G.getNodes())-set(G.getSeeds()))
  for i in range(0,seedCount):
    for v in candidates:
      v.setExtraInfluence(0)
      results = []
      for s in G.getSeeds():
        cascade(s, results)
      cascade(v, results)
      v.setExtraInfluence(len(results))
    selected = getMaximumNode(candidates)
    G.addSeed(selected)
    candidates.remove(selected)

  runningTimes[method] = round(time.time() - startTime,2)

def cascade(seed, results): ##DFS
  if seed not in results:
    results.append(seed)
  for e in seed.getOutEdges():
    if e.isValid():
      dest = e.getDest()
      if dest not in results:
        results.append(dest)
        cascade(dest, results)

def validatePath():
  global G

  for e in G.getEdges():
    if isValidPath(e):
      e.validate()
      e.getSrc().validate()
      e.getSrc().setValidOutDegree(e.getSrc().getValidOutDegree()+1)
      e.getDest().validate()
    else:
      e.invalidate()

def isValidPath(edge):

  src = edge.getSrc()
  dest = edge.getDest()

  if edge.isActivation():
    if src.getStatus() == dest.getStatus():
      return checkTimeSeries(src, dest)
    else:
      return False
  elif edge.isInhibition():
    if src.getStatus() != dest.getStatus():
      return checkTimeSeries(src, dest)
    else:
      return False
  else:
    print "error"
    return False

def checkTimeSeries(src, dest):
  global G

  if src.isConstant() or dest.isConstant():
    return False

  if dest.getTime() - src.getTime() < 2:
    return True

  srcGroup = G.getSameNameNodes(src.getGeneName())
  destGroup = G.getSameNameNodes(dest.getGeneName())

  if len(srcGroup) != len(destGroup):
    print "error"
    return False

  for i in range(srcGroup.index(src), destGroup.index(dest)+1):
    tail = srcGroup[i]
    if tail.getStatus() != src.getStatus():
      break
  for j in range(i+1, destGroup.index(dest)+1):
    head = destGroup[j]
    if head.getStatus() != dest.getStatus():
      return False

  return True

def getMaximumNode(nodes):
  max = nodes[0]
  for v in nodes:
    if v.getExtraInfluence() > max.getExtraInfluence():
      max = v
  return max


if __name__ == "__main__":
  k = int(sys.argv[1]) if len(sys.argv) > 1 else 2
  input = sys.argv[2] if len(sys.argv) > 2 else "input.txt"
  output = sys.argv[3] if len(sys.argv) > 3 else "output.txt"
  initialize(k,input,output)
  main()



