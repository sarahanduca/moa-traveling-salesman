import math
import random
import copy


class Graph:
    def __init__(self, size):
        self.size = size
        self.vertex = []

    def setVertex(self, id, x, y):
        self.vertex.append([id, x, y])


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
        description.append(userInput)
    i = description.index('a')
    constructor = description[i + 1: len(description) - 1]
    graph = Graph(len(constructor))
    for line in constructor:
        graph.setVertex(contLines + 1, float(line.split()
                                             [1]), float(line.split()[-1]))
        contLines += 1

    return graph


def makeMatrix():
    contLines = 0
    file = open('pontos.txt', 'r')
    graph = Graph(48)
    for line in file:
        graph.setVertex(contLines + 1, float(line.split()
                                             [1]), float(line.split()[-1]))
        contLines += 1
    return graph


def nearestNeighbor(graph):
    randomVertex = random.randint(0, graph.size)
    firstVertex = randomVertex
    listVisit = []
    listVisit.append(randomVertex)
    edges = []
    while len(listVisit) < graph.size:
        min = math.inf
        for j in range(graph.size):
            if j not in listVisit:
                if weightEdge(graph.vertex[randomVertex], graph.vertex[j]) < min:
                    min = weightEdge(
                        graph.vertex[randomVertex], graph.vertex[j])
                    i = j
        listVisit.append(i)
        edges.append(Edges(randomVertex, i, min))
        randomVertex = i

    edges.append(Edges(i, firstVertex, weightEdge(
        graph.vertex[i], graph.vertex[firstVertex])))
    sumWeight = 0
    for edge in edges:
        sumWeight += edge.weight

    # betterWeight = [item[1] for item in edges]
    return sumWeight, edges


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


def isAdjacent(currEdge, randomEdge):
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
            if not isAdjacent(edge, randomEdge):
                if(compareWeight(graph, edge, randomEdge)):
                    swap(edge, randomEdge, graph, index, randomIndex, edges)

    sumWeight = 0
    for edge in edges:
        sumWeight += edge.weight

    # print('oi')
    # for edge in edges:
        # print(edge.x, edge.y)
    return sumWeight


def swap(edge1, edge2, graph, index, randomIndex, edges):
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


def threeOpt(edges, graph):
    fazer = 1


if __name__ == '__main__':
    graph = makeMatrix()
    result, edges = nearestNeighbor(graph)
    result2 = twoOpt(edges, graph)
    # result3 = threeOpt(edges, graph)

    print(result, result2)
