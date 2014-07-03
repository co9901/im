import sys
from node import Node
from edge import Edge
from graph import Graph

#G graph
#seedCount
#inputFileName
#outputFileName

G = Graph()
seedCount = 0

def main():

  validatePath()
  generalGreedy()
  printResults()

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

def printResults():
  global G
  global outputFileName

  G.draw()
  outputFile = open(outputFileName,'w')
  outputFile.write("Seed :\n")
  for s in G.getSeeds():
    outputFile.write(s.getId() + " " + s.getName() + "\n")

  outputFile.write("========\n")
  outputFile.write("propagated :\n")

  validNodeSet = G.getValidNodeSet()
  for k in validNodeSet.keys():
    outputFile.write(k)
    for n in validNodeSet[k]:
      outputFile.write(" " + str(n.getTime()))
    outputFile.write("\n")

  outputFile.write("========\n")

  outputFile.close()


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



