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
        return True
    return False


def compareWeight3(graph, edge, randomEdge1, randomEdge2):
    newEdge1 = weightEdge(graph.vertex[edge.x], graph.vertex[randomEdge1.x])
    newEdge2 = weightEdge(graph.vertex[edge.y], graph.vertex[randomEdge2.x])
    newEdge3 = weightEdge(
        graph.vertex[randomEdge1.y], graph.vertex[randomEdge2.y])
    if (newEdge1 + newEdge2 + newEdge3) < (edge.weight + randomEdge1.weight + randomEdge2.weight):
        return True
    return False


def compareWeight3Value(graph, edge, randomEdge1, randomEdge2):
    newEdge1 = weightEdge(graph.vertex[edge.x], graph.vertex[randomEdge1.x])
    newEdge2 = weightEdge(graph.vertex[edge.y], graph.vertex[randomEdge2.x])
    newEdge3 = weightEdge(
        graph.vertex[randomEdge1.y], graph.vertex[randomEdge2.y])
    return newEdge1 + newEdge2 + newEdge3


def twoOpt(edges, graph):
    for index, edge in enumerate(edges):
        randomList = random.sample(range(0, graph.n), graph.n)
        while len(randomList) > 0:
            randomIndex = randomList.pop()
            randomEdge = edges[randomIndex]
            if not isAdjacent(edge, randomEdge):
                if(compareWeight(graph, edge, randomEdge)):
                    swap(edge, randomEdge, graph)

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
        randomList = random.sample(range(0, graph.n), graph.n)
        while len(randomList) > 1:
            optResults = [math.inf]*7
            randomIndex1 = randomList.pop()
            randomIndex2 = randomList.pop()
            randomEdge1 = edges[randomIndex1]
            randomEdge2 = edges[randomIndex2]
            if not isAdjacent(edge, randomEdge1) and not isAdjacent(edge, randomEdge2) and not isAdjacent(randomEdge1, randomEdge2):
                if compareWeight(graph, edge, randomEdge2):
                    optResults[0] = weightEdge(graph.vertex[edge.x], graph.vertex[randomEdge2.x]) + weightEdge(
                        graph.vertex[edge.y], graph.vertex[randomEdge2.y])
                elif compareWeight(graph, randomEdge1, randomEdge2):
                    optResults[1] = weightEdge(graph.vertex[randomEdge1.x], graph.vertex[randomEdge2.x]) + weightEdge(
                        graph.vertex[randomEdge1.y], graph.vertex[randomEdge2.y])
                elif compareWeight(graph, edge, randomEdge1):
                    optResults[2] = weightEdge(graph.vertex[edge.x], graph.vertex[randomEdge1.x]) + weightEdge(
                        graph.vertex[edge.y], graph.vertex[randomEdge1.y])
                elif compareWeight3(graph, edge, randomEdge1, randomEdge2):
                    optResults[3] = compareWeight3Value(
                        graph, edge, randomEdge1, randomEdge2)
                elif compareWeight3(graph, randomEdge1, randomEdge2, edge):
                    optResults[5] = compareWeight3Value(
                        graph, randomEdge1, randomEdge2, edge)

                minList = min(optResults)
                minListIndex = optResults.index(minList)
                if minListIndex == 0:
                    swap(edge, randomEdge2, graph)
                elif minListIndex == 1:
                    swap(randomEdge1, randomEdge2, graph)
                elif minListIndex == 2:
                    swap(edge, randomEdge1, graph)

            randomList.append(randomIndex2)

    sumWeight = 0
    for edge in edges:
        sumWeight += edge.weight

    return sumWeight


if __name__ == '__main__':
    graph = makeMatrix()
    result, edges = nearestNeighbor(graph)
    # result2 = twoOpt(edges, graph)
    result3 = threeOpt(edges, graph)

    print(result, result3)
