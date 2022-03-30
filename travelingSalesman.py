import math
import random
import copy


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

# class Edges:
#     def __init__(self, vertex1, vertex2, edge):
#         self.vertex1 = vertex1
#         self.vertex2 = vertex2
#         self.edge = edge

#     def setVertex(self, vertex1, vertex2):
#         self.vertex1 = vertex1
#         self.vertex2 = vertex2

#     def setEdge(self, edge):
#         self.edge = edge


def weightEdge(v1, v2):
    return math.sqrt(((v1.x-v2.x)**2) + ((v1.y-v2.y)**2))


def readInput():
    description = []
    listVertex = []
    userInput = ''
    contLines = 0
    while userInput != 'EOF':
        userInput = input().strip()
        description.append(userInput)
    i = description.index('NODE_COORD_SECTION')
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
        edges.append(Edges(randomVertex, i, min))
        randomVertex = i

    edges.append(Edges(i, firstVertex, graph.getElement(i, firstVertex)))
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
                if graph.getElement(randomVertex, j) > max:
                    max = graph.getElement(randomVertex, j)
                    i = j
        listVisit.append(i)
        edges.append([(randomVertex, i), max])
        randomVertex = i
    betterWeight = [item[1] for item in edges]
    return sum(betterWeight)


def isAdjacent(currEdge, randomEdge):
    return currEdge.x == randomEdge.x or currEdge.y == randomEdge.x or randomEdge.y == currEdge.x or currEdge.y == randomEdge.y


def twoOpt(edges, graph):
    for index, edge in enumerate(edges):
        randomList = random.sample(range(0, graph.n), graph.n)
        while len(randomList) > 0:
            randomIndex = randomList.pop()
            randomEdge = edges[randomIndex]
            if not isAdjacent(edge, randomEdge):
                newEdge1 = graph.getElement(edge.x, randomEdge.x)
                newEdge2 = graph.getElement(edge.y, randomEdge.y)
                if (newEdge1 + newEdge2) < (edge.weight + randomEdge.weight):
                    swap(edge, randomEdge, graph)

    sumWeight = 0
    for edge in edges:
        sumWeight += edge.weight

    return sumWeight


def swap(edge1, edge2, graph):
    y = edge1.y
    edge1.setEdge(edge1.x, edge2.x, graph.getElement(edge1.x, edge2.x))
    edge2.setEdge(y, edge2.y, graph.getElement(y, edge2.y))


if __name__ == '__main__':
    graph = readInput()
    result, edges = nearestNeighbor(graph)
    result2 = twoOpt(edges, graph)

    print(result2)
