import math
import random
import copy


class Graph:
    def __init__(self, size):
        self.size = size
        self.vertex = []

    def setVertex(self, id, x, y):
        self.vertex.append([id, x, y, False])
   


class Edges:
    def __init__(self, x, y, weight):
        self.x = x
        self.y = y
        self.weight = weight

    def setEdge(self, x, y, weight):
        self.x = x
        self.y = y
        self.weight = weight

    def getEdge(self):
        return self.x, self.y, self.weight


def weightEdge(v1, v2):
    return math.sqrt(((v1[1]-v2[1])**2) + ((v1[2]-v2[2])**2))


def readInput():
    description = []
    userInput = ''
    contLines = 0
    while userInput != 'EOF':
        userInput = input().strip()
    #     graph.vertex[lastVertex], graph.vertex[firstVertex])))
    # sumWeight = 0
    # for edge in edges:
    #     sumWeight += edge.weight
    #     print(edge.x, edge.y)

        description.append(userInput)
    i = description.index('NODE_COORD_SECTION')
    constructor = description[i + 1: len(description) - 1]
    graph = Graph(len(constructor))
    for line in constructor:
        graph.setVertex(contLines + 1, float(line.split()
                                             [1]), float(line.split()[-1]))
        contLines += 1

    return graph


def makeMatrix():
    contLines = 0
    file = open('D:\Sarah\Code\MOA-Trabalho1\pontos.txt', 'r')
    graph = Graph(48)
    for line in file:
        graph.setVertex(contLines + 1, float(line.split()
                                             [1]), float(line.split()[-1]))
        contLines += 1
    return graph


def nearestNeighbor(graph):
    randomVertex = random.randint(0, graph.size - 1)
    firstVertex = randomVertex
    listVisit = [False] * graph.size
    listVisit[randomVertex] = True
    edges = []
    cont = 0
    while cont < graph.size - 1:
        min = math.inf
        for j in range(graph.size):
            if not listVisit[j]:
                if weightEdge(graph.vertex[randomVertex], graph.vertex[j]) < min:
                    min = weightEdge(
                        graph.vertex[randomVertex], graph.vertex[j])
                    lastVertex = j
        listVisit[lastVertex] = True
        edges.append(Edges(randomVertex, lastVertex , min))
        randomVertex = lastVertex 
        cont+=1

    edges.append(Edges(lastVertex , firstVertex, weightEdge(
        graph.vertex[lastVertex ], graph.vertex[firstVertex])))
    sumWeight = 0
    for edge in edges:
        sumWeight += edge.weight

    # betterWeight = [item[1] for item in edges]
    return sumWeight, edges


    # randomVertex = random.randint(0, graph.size)
    # firstVertex = randomVertex
    # graph.setVisit(randomVertex)
    # # listVisit = []
    # # listVisit.append(randomVertex)
    # edges = []
    # lastVertex = 0
    # cont = 0
    # while cont < graph.size:
    #     min = math.inf
    #     # print(graph.isVisit(cont))
    #     for j in range(graph.size):
    #         # print(weightEdge(graph.vertex[randomVertex], graph.vertex[j]), graph.isVisit(graph.vertex[j]))
    #         if not graph.isVisit(j):
    #             if weightEdge(graph.vertex[randomVertex], graph.vertex[j]) < min:
    #                 min = weightEdge(
    #                     graph.vertex[randomVertex], graph.vertex[j])
    #                 lastVertex = j
            
    #     graph.setVisit(j)
    #     # listVisit.append(i)
    #     edges.append(Edges(randomVertex, lastVertex, min))
    #     randomVertex = lastVertex
    #     cont += 1
        
    # edges.append(Edges(lastVertex, firstVertex, weightEdge(
    # # betterWeight = [item[1] for item in edges]
    # return sumWeight, edges


def farestNeighbor(graph):
    randomVertex = random.randint(0, graph.size)
    listVisit = []
    listVisit.append(randomVertex)
    edges = []
    while len(listVisit) < graph.size:
        max = 0
        for j in range(graph.size):
            if j not in listVisit:
                if weightEdge(randomVertex, j) > max:
                    max = weightEdge(randomVertex, j)
                    i = j
        listVisit.append(i)
        edges.append([(randomVertex, i), max])
        randomVertex = i
    betterWeight = [item[1] for item in edges]
    return sum(betterWeight)


def isAdjacent2(currEdge, randomEdge):
    return currEdge.x == randomEdge.x or currEdge.y == randomEdge.x or randomEdge.y == currEdge.x or currEdge.y == randomEdge.y


def compareWeight(graph, edge, randomEdge):
    newEdge1 = weightEdge(graph.vertex[edge.x], graph.vertex[randomEdge.x])
    newEdge2 = weightEdge(graph.vertex[edge.y], graph.vertex[randomEdge.y])
    if (newEdge1 + newEdge2) < (edge.weight + randomEdge.weight):
        return True
    return False


def twoOpt(edges, graph):
    # for edge in edges:
    # print(edge.x, edge.y)
    for index, edge in enumerate(edges):
        randomList = random.sample(
            range(index, graph.size), graph.size - index)
        while len(randomList) > 0:
            randomIndex = randomList.pop()
            randomEdge = edges[randomIndex]
            if not isAdjacent2(edge, randomEdge):
                if(compareWeight(graph, edge, randomEdge)):
                    swap2(edge, randomEdge, graph, index, randomIndex, edges)

    sumWeight = 0
    for edge in edges:
        sumWeight += edge.weight

    # print('oi')
    # for edge in edges:
        # print(edge.x, edge.y)
    return sumWeight


def swap2(edge1, edge2, graph, index, randomIndex, edges):
    y = edge1.y
    edge1.setEdge(edge1.x, edge2.x, weightEdge(
        graph.vertex[edge1.x], graph.vertex[edge2.x]))
    edge2.setEdge(y, edge2.y, weightEdge(
        graph.vertex[y], graph.vertex[edge2.y]))

    if not randomIndex == index + 1:
        if randomIndex == index + 2:
            edge = edges[index + 1]
            x, y = edge.x, edge.y
            edge.setEdge(y, x, edge.weight)
        else:
            aux = int(randomIndex/2)
            for i in range(int(index), int(randomIndex/2)):
                edgeLeft = edges[i + 1]
                edgeRight = edges[aux - 1]
                x, y, w = edgeLeft.x, edgeLeft.y, edgeLeft.weight
                edgeLeft.setEdge(edgeRight.y, edgeRight.x, edgeRight.weight)
                edgeRight.setEdge(y, x, w)
                aux -= 1
            if not randomIndex % 2 == 0:
                edge = edges[math.ceil(randomIndex/2)]
                x, y = edge.x, edge.y
                edge.setEdge(y, x, edge.weight)
                aux = (randomIndex/2)

def weightValue(edge1x, edge1y, edge2x, edge2y, edge3x, edge3y):
    return weightEdge(edge1x, edge2x) + weightEdge(edge1y, edge3x) + weightEdge(edge2y, edge3y)

def swap3(indexStart, indexEnd, edges):
    interval = indexEnd - indexStart
    # print(interval, indexEnd, indexStart)
    while interval > 2:
        edgeStart = edges[indexStart + 1]
        edgeEnd = edges[indexEnd - 1]
        x, y, w = edgeStart.x, edgeStart.y, edgeStart.weight
        edgeStart.setEdge(edgeEnd.y, edgeEnd.x, edgeEnd.weight)
        edgeEnd.setEdge(y, x, w)
        indexStart += 1
        indexEnd -= 1
        interval -= 2
    if interval == 2:
        edgeMiddle = edges[indexStart + 1]
        x, y = edgeMiddle.x, edgeMiddle.y
        edgeMiddle.setEdge(y, x, edgeMiddle.weight)

def threeOpt(edges, graph):
    for indexi, i in enumerate(edges):
        for indexj, j in enumerate(edges):
            for indexk, k in enumerate(edges):
                if indexk > indexj and indexj > indexi:
                    if not isAdjacent2(i, j):
                        if not isAdjacent2(i, k):
                            if not isAdjacent2(j, k):
                                d1 = weightValue(graph.vertex[i.x], graph.vertex[i.y], graph.vertex[j.x], graph.vertex[j.y], graph.vertex[k.x], graph.vertex[k.y])
                                d2 = weightValue(graph.vertex[i.x], graph.vertex[k.y], graph.vertex[k.x], graph.vertex[i.y], graph.vertex[j.x], graph.vertex[j.y])
                                d3 = weightValue(graph.vertex[j.x], graph.vertex[i.x], graph.vertex[k.x], graph.vertex[i.y], graph.vertex[j.y], graph.vertex[k.y])
                                d4 = weightValue(graph.vertex[i.x], graph.vertex[j.x], graph.vertex[j.y], graph.vertex[k.x], graph.vertex[k.y], graph.vertex[i.y])
                                distanceList =[d1, d2, d3, d4]
                                minDistance = min(distanceList)
                                indexDistance = distanceList.index(minDistance)
                                if minDistance < (i.weight + j.weight + k.weight):
                                    if indexDistance == 0:
                                        ix, iy = i.x, i.y
                                        jx, jy = j.x, j.y
                                        kx, ky = k.x, k.y
                                        i.setEdge(ix, jx, weightEdge(graph.vertex[ix], graph.vertex[jx]))
                                        j.setEdge(iy, kx, weightEdge(graph.vertex[iy], graph.vertex[kx]))
                                        k.setEdge(jy, ky, weightEdge(graph.vertex[jy], graph.vertex[ky]))
                                        swap3(indexi, indexj, edges)
                                        swap3(indexj, indexk, edges)
                                    elif indexDistance == 1:
                                        ix, iy = i.x, i.y
                                        jx, jy = j.x, j.y
                                        kx, ky = k.x, k.y
                                        i.setEdge(ix, kx, weightEdge(graph.vertex[ix], graph.vertex[kx]))
                                        j.setEdge(jy, iy, weightEdge(graph.vertex[jy], graph.vertex[iy]))
                                        k.setEdge(jx, ky, weightEdge(graph.vertex[jx], graph.vertex[ky]))
                                        swap3(indexj, indexk, edges)
                                    elif indexDistance == 2:
                                        ix, iy = i.x, i.y
                                        jx, jy = j.x, j.y
                                        kx, ky = k.x, k.y
                                        i.setEdge(ix, jy, weightEdge(graph.vertex[ix], graph.vertex[jy]))
                                        j.setEdge(kx, jx, weightEdge(graph.vertex[kx], graph.vertex[jx]))
                                        k.setEdge(iy, ky, weightEdge(graph.vertex[iy], graph.vertex[ky]))
                                        swap3(indexi, indexj, edges)
                                    else:
                                        ix, iy = i.x, i.y
                                        jx, jy = j.x, j.y
                                        kx, ky = k.x, k.y
                                        i.setEdge(ix, jy, weightEdge(graph.vertex[ix], graph.vertex[jy]))
                                        j.setEdge(kx, iy, weightEdge(graph.vertex[kx], graph.vertex[iy]))
                                        k.setEdge(jx, ky, weightEdge(graph.vertex[jx], graph.vertex[ky]))
    sumWeight = 0
    for edge in edges:
        sumWeight += edge.weight

    return sumWeight


if __name__ == '__main__':
    graph = makeMatrix()
    result, edges = nearestNeighbor(graph)
    result2 = twoOpt(edges, graph)
    result3 = threeOpt(edges, graph)

    print(result, result2, result3)
