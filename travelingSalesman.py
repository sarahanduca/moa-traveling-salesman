import math
import random


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
        self.x = int(x)
        self.y = int(y)


def weightEdge(v1, v2):
    return math.sqrt((v1.x-v2.x)**2 + (v1.y-v2.y)**2)


def makeMatrix():
    listVertex = []
    contLines = 0
    file = open('pontos.txt', 'r')
    for line in file:
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
        edges.append([(randomVertex, i), min])
        randomVertex = i

    for element in edges:
        print(element)

    betterWeight = [item[1] for item in edges]

    print(sum(betterWeight))


def main():
    graph = makeMatrix()
    nearestNeighbor(graph)


if __name__ == '__main__':
    main()
