import math
import random
from operator import itemgetter
import copy
import time
import sys


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


def weightEdge(v1, v2):
    return math.sqrt(((v1[1]-v2[1])**2) + ((v1[2]-v2[2])**2))


def readInput():
    description = []
    userInput = ''
    contLines = 0
    while userInput != 'EOF':
        userInput = input().strip()
        description.append(userInput)
    i = description.index('NODE_COORD_SECTION')
    constructor = description[i + 1: len(description) - 1]
    graph = Graph(len(constructor))
    for line in constructor:
        graph.setVertex(contLines + 1, float(line.split()
                                             [1]), float(line.split()[-1]))
        contLines += 1

    return graph


def nearestNeighbor(graph, randomVertex):
    firstVertex = randomVertex
    listVisit = [False] * graph.size
    listVisit[randomVertex] = True
    edges = []
    cont = 0
    while cont < graph.size - 1:
        min = math.inf
        for j in range(graph.size):
            if not listVisit[j]:
                currWeight = weightEdge(
                    graph.vertex[randomVertex], graph.vertex[j])
                if currWeight < min:
                    min = currWeight
                    lastVertex = j
        listVisit[lastVertex] = True
        edges.append(Edges(randomVertex, lastVertex, min))
        randomVertex = lastVertex
        cont += 1

    edges.append(Edges(lastVertex, firstVertex, weightEdge(
        graph.vertex[lastVertex], graph.vertex[firstVertex])))
    sumWeight = 0
    for edge in edges:
        sumWeight += edge.weight

    return sumWeight, edges


def selectNotCopy(dad, son, i, j):
    buffer = []
    buffer.extend(dad[:i])
    buffer.extend(son)
    buffer.extend(dad[j:])
    return buffer


def cross(son, buffer, dad, i, j):
    for c in son:
        if c in buffer[:i]:
            aux = buffer.index(c)
            buffer[aux] = dad[i]
        if c in buffer[j:]:
            aux = buffer[j:].index(c)
            aux += j
            buffer[aux] = dad[i]
        i += 1
    return buffer


def mutation(son):
    i = random.randint(1, len(son) - 1)
    j = random.randint(i, len(son) - 1)

    son[i], son[j] = son[j], son[i]

    return son


def makeWeight(graph, buffer):
    edges = []
    for i in range(len(buffer) - 1):
        x = graph.vertex[buffer[i]]
        y = graph.vertex[buffer[i + 1]]
        edges.append(Edges(x[0], y[0], weightEdge(x, y)))
    return edges


def partiallyMapped(d1, d2, graph):
    son1 = []
    son2 = []
    buffer1 = []
    buffer2 = []
    dad1 = copy.deepcopy(d1[1:])
    dad2 = copy.deepcopy(d2[1:])
    i = random.randint(1, len(dad1) - 1)
    j = random.randint(i, len(dad1))
    son2 = dad1[i:j]
    son1 = dad2[i:j]
    buffer1 = selectNotCopy(dad1, son1, i, j)
    buffer2 = selectNotCopy(dad2, son2, i, j)
    buffer1 = cross(son1, buffer1, dad1, i, j)
    buffer2 = cross(son2, buffer2, dad2, i, j)
    buffer1 = mutation(buffer1)
    buffer2 = mutation(buffer2)
    if 48 in buffer1:
        buffer1 = [x - 1 for x in buffer1]
    if 48 in buffer2:
        buffer2 = [x - 1 for x in buffer2]
    son1 = makeWeight(graph, buffer1)
    son2 = makeWeight(graph, buffer2)

    return son1, son2


def makeList(edges, result):
    listPath = []
    firstVertex = 0
    listPath.append(result)
    for i in range(len(edges)):
        if i == 0:
            firstVertex = edges[i].x
        listPath.append(edges[i].x)
    listPath.append(firstVertex)
    return listPath


def makePopulation():
    population = []
    graph = readInput()
    randomList = random.sample(range(1, graph.size), 47)
    for i in range(graph.size - 1):
        randomVertex = randomList.pop(0)
        result, edges = nearestNeighbor(graph, randomVertex)
        population.append(makeList(edges, result))
    population = sorted(population)
    return population, graph


def localSearch(son, population):
    sumWeight = 0
    for edge in son:
        sumWeight += edge.weight
    son = makeList(son, sumWeight)
    for i in range(len(population)):
        if son[0] < population[i][0]:
            population.insert(i, son)
            population.pop(-1)
            return population
    return population


if __name__ == '__main__':
    population = []
    partialResult1 = []
    partialResult2 = []
    population, graph = makePopulation()
    print(population)
    print("---------------------------------")
    cont = 0
    while cont != 100000:
        partialResult1, partialResult2 = partiallyMapped(
            population[0], population[1], graph)
        population = localSearch(partialResult1, population)
        cont += 1
    print(population)
