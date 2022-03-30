import math
import random
import copy


class Graph:
    def __init__(self, n):
        self.n = n
        self.vertex = []

    def setVertex(self, n, x, y):
        self.vertex.append([n, x, y])


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


class Vertex:
    def __init__(self, id, x, y):
        self.id = int(id)
        self.x = float(x)
        self.y = float(y)


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
    graph = Graph(33810)
    for line in file:
        graph.setVertex(contLines + 1, float(line.split()
                                             [1]), float(line.split()[-1]))
        contLines += 1
    return graph


def nearestNeighbor(graph):
    randomVertex = random.randint(0, graph.n)
    firstVertex = randomVertex
    listVisit = []
    listVisit.append(randomVertex)
    edges = []
    while len(listVisit) < graph.n:
        min = math.inf
        for j in range(graph.n):
            if j not in listVisit:
                # print(graph.vertex[100], graph.vertex[2])
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
    randomVertex = random.randint(0, graph.n)
    listVisit = []
    listVisit.append(randomVertex)
    edges = []
    while len(listVisit) < graph.n:
        max = 0
        for j in range(graph.n):
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
        swap(edge, randomEdge, graph)


def twoOpt(edges, graph):
    for index, edge in enumerate(edges):
        randomList = random.sample(range(0, graph.n), graph.n)
        while len(randomList) > 0:
            randomIndex = randomList.pop()
            randomEdge = edges[randomIndex]
            if not isAdjacent(edge, randomEdge):
                compareWeight(graph, edge, randomEdge)

    sumWeight = 0
    for edge in edges:
        sumWeight += edge.weight

    return sumWeight


def swap(edge1, edge2, graph):
    y = edge1.y
    edge1.setEdge(edge1.x, edge2.x, weightEdge(
        graph.vertex[edge1.x], graph.vertex[edge2.x]))
    edge2.setEdge(y, edge2.y, weightEdge(
        graph.vertex[y], graph.vertex[edge2.y]))


def threeOpt(edges, graph):
    for index, edge in enumerate(edges):
        randomList1 = random.sample(range(0, graph.n), graph.n)
        while len(randomList1) > 0:
            randomIndex1 = randomList1.pop()
            randomEdge1 = edges[randomIndex1]
            randomList2 = random.sample(range(0, graph.n), graph.n)
            if not isAdjacent(edge, randomEdge1):
                while len(randomList2) > 0:
                    randomIndex2 = randomList2.pop()
                    randomEdge2 = edges[randomIndex2]
                    if not isAdjacent(edge, randomEdge2) and not isAdjacent(randomEdge1, randomEdge2):
                        a = 2


if __name__ == '__main__':
    graph = makeMatrix()
    result, edges = nearestNeighbor(graph)
    # threeOpt(edges, graph)
    result2 = twoOpt(edges, graph)

    print(result2)
