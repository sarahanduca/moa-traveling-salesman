import math
import random
import re

class Matrix:
    def __init__(self, n, m):
        self.matrix = self.getMatrix(n, m)
        self.n = n

    def getMatrix(self, n, m):
        num = math.inf
        matrix = [[None for j in range(m)] for i in range(n)]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = num
        return matrix

    def getElement(self, i, j):
        return self.matrix[i-1][j-1]

    def setElement(self, i, j, element):
        self.matrix[i-1][j-1] = element


class Vertex:
    def __init__(self, id, x, y):
        self.id = int(id)
        self.x = float(x)
        self.y = float(y)

def weightEdge(v1, v2):
    return math.sqrt(((v1.x-v2.x)**2) + ((v1.y-v2.y)**2))


# def makeMatrix():
#     listVertex = []
#     contLines = 0
#     file = open('pontos.txt', 'r')
#     for line in file:
#         listVertex.append(
#             Vertex(contLines + 1, line.split()[1], line.split()[-1]))
#         contLines += 1

#     graph = Matrix(contLines, contLines)

#     for i in range(len(listVertex)):
#         for j in range(len(listVertex)):
#             graph.setElement(i, j, weightEdge(listVertex[i], listVertex[j]))

#     return graph


def readInput():
    description = []
    listVertex = []
    userInput = ''
    contLines = 0
    
    while userInput != 'EOF':
        userInput = input().strip()
        description.append(userInput)
    i = description.index('a')
    constructor = description[i + 1: len(description) - 1]
    for line in constructor:
        listVertex.append(
            Vertex(contLines + 1, line.split()[1], line.split()[-1]))
        contLines += 1

    graph = Matrix(contLines, contLines)

    for i in range(len(listVertex)):
        for j in range(len(listVertex)):
            graph.setElement(i, j, weightEdge(listVertex[i], listVertex[j]))

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
                if graph.getElement(randomVertex, j) < min:
                    min = graph.getElement(randomVertex, j)
                    i = j

        listVisit.append(i)
        edges.append([[randomVertex, i], min])
        randomVertex = i
    edges.append([[i, firstVertex], graph.getElement(i, firstVertex)])
    # for element in edges:
    #     print(element)

    betterWeight = [item[1] for item in edges]
    return sum(betterWeight), edges


def farestNeighbor(graph):
    randomVertex = random.randint(0, graph.n)

    listVisit = []
    listVisit.append(randomVertex)
    edges = []

    while len(listVisit) < graph.n:
        max = 0
        for j in range(graph.n):
            if j not in listVisit:
                if graph.getElement(randomVertex, j) > max:
                    max = graph.getElement(randomVertex, j)
                    i = j
        listVisit.append(i)
        edges.append([(randomVertex, i), max])
        randomVertex = i

    for element in edges:
        print(element)

    betterWeight = [item[1] for item in edges]

    return sum(betterWeight)

def isAdjacent(currEdge, randomEdge, beforeCurr):
    return currEdge[0][0] == randomEdge or currEdge[0][1] == randomEdge or beforeCurr[0][0] == randomEdge

def twoOpt(edges, graph):
    for index, edge in enumerate(edges):
        randomList = random.sample(range(0, graph.n), graph.n)
        while len(randomList) != 0:
            randomIndex = randomList.pop()
            randomEdge = edges[randomIndex]
            if not isAdjacent(edge, randomEdge[0][0], edges[index - 1]):
                newEdge1 = graph.getElement(edge[0][0], randomEdge[0][0])
                newEdge2 = graph.getElement(edge[0][1], randomEdge[0][1])
                if newEdge1 + newEdge2 < edge[1] + randomEdge[1]:
                    swap(edge[0][0], randomIndex, edges)

    return sum([item[1] for item in edges])

def swap(vertex1, vertex2, edges):
    print(edges)
    listEdges = list(edges)
    i1 = getIndex(vertex1, listEdges)
    i2 = getIndex(vertex2, listEdges)
    print(edges[i1][0][1])
    print(listEdges[i2][0][0])
    listEdges[i2][0][0] = edges[i1][0][1]
    listEdges[i1][0][1] = edges[i2][0][0]

    

def getIndex(vertex, edges):
    cont = 0
    for edge in edges:
        if edge[0][0] == vertex:
            return cont
        cont += 1

if __name__ == '__main__':
    graph = readInput()
    result, edges = nearestNeighbor(graph)
    result2 = twoOpt(edges, graph)

    print(result, result2)