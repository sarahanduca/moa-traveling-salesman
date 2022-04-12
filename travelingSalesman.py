import math
import random
import copy
import time
import sys

TESTS = [
    './pr1002.tsp',
    './fnl4461.tsp',
    './brd14051.tsp',
    './d15112.tsp',
    './d18512.tsp',
    './pla7397.tsp',
    './pla33810.tsp',
    './pla85900.tsp'
]


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


def makeGraph(test):
    if test == './pr1002.tsp':
        contLines = 0
        file = open(test, 'r')
        graph = Graph(1002)
        for line in file:
            graph.setVertex(contLines + 1, float(line.split()
                                                 [1]), float(line.split()[-1]))
            contLines += 1
        return graph
    elif test == './fnl4461.tsp':
        contLines = 0
        file = open(test, 'r')
        graph = Graph(4461)
        for line in file:
            graph.setVertex(contLines + 1, float(line.split()
                                                 [1]), float(line.split()[-1]))
            contLines += 1
        return graph
    elif test == './brd14051.tsp':
        contLines = 0
        file = open(test, 'r')
        graph = Graph(14051)
        for line in file:
            graph.setVertex(contLines + 1, float(line.split()
                                                 [1]), float(line.split()[-1]))
            contLines += 1
        return graph
    elif test == './d15112.tsp':
        contLines = 0
        file = open(test, 'r')
        graph = Graph(15112)
        for line in file:
            graph.setVertex(contLines + 1, float(line.split()
                                                 [1]), float(line.split()[-1]))
            contLines += 1
        return graph
    elif test == './d18512.tsp':
        contLines = 0
        file = open(test, 'r')
        graph = Graph(18512)
        for line in file:
            graph.setVertex(contLines + 1, float(line.split()
                                                 [1]), float(line.split()[-1]))
            contLines += 1
        return graph
    elif test == './pla7397.tsp':
        contLines = 0
        file = open(test, 'r')
        graph = Graph(7397)
        for line in file:
            graph.setVertex(contLines + 1, float(line.split()
                                                 [1]), float(line.split()[-1]))
            contLines += 1
        return graph
    elif test == './pla33810.tsp':
        contLines = 0
        file = open(test, 'r')
        graph = Graph(33810)
        for line in file:
            graph.setVertex(contLines + 1, float(line.split()
                                                 [1]), float(line.split()[-1]))
            contLines += 1
        return graph
    elif test == './pla85900.tsp':
        contLines = 0
        file = open(test, 'r')
        graph = Graph(85900)
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


def isAllTrue(list):
    for i in list:
        if not i:
            return False
    return True


def nearestVertex(graph, vertex, listVisit):
    lastvertex = 0
    min = math.inf
    for i in range(graph.size):
        if not listVisit[i]:
            currWeight = weightEdge(
                graph.vertex[vertex], graph.vertex[i])
            if currWeight < min:
                min = currWeight
                lastvertex = i
    return lastvertex


def insertInPath(graph, nearest, path, listVisit):
    choseIndex = math.inf
    best = math.inf

    lengthPath = len(path) - 1
    for i in range(0, lengthPath):
        if i == 0:
            initialCost = weightEdge(graph.vertex[0], graph.vertex[lengthPath])
            finalCost = weightEdge(graph.vertex[0], graph.vertex[nearest]) + weightEdge(
                graph.vertex[nearest], graph.vertex[lengthPath])
        else:
            initialCost = weightEdge(graph.vertex[i], graph.vertex[i - 1])
            finalCost = weightEdge(graph.vertex[i - 1], graph.vertex[nearest]) + weightEdge(
                graph.vertex[nearest], graph.vertex[i])

        total = finalCost - initialCost

        if total < best:
            best = total
            choseIndex = i

    if choseIndex == lengthPath:
        path.append(nearest)
    else:
        path.insert(choseIndex, nearest)
    listVisit[nearest] = True


def nearestInsertion(graph):
    randomVertex = random.randint(0, graph.size - 1)
    listVisit = [False] * graph.size
    listVisit[randomVertex] = True
    path = []
    edges = []
    path.append(randomVertex)
    min = math.inf
    for i in range(graph.size):
        if not listVisit[i]:
            currWeight = weightEdge(
                graph.vertex[randomVertex], graph.vertex[i])
            if currWeight < min:
                min = currWeight
                lastvertex = i
    listVisit[lastvertex] = True
    path.append(lastvertex)

    while not isAllTrue(listVisit):
        vertex = path[random.randint(0, len(path) - 1)]
        nearest = nearestVertex(graph, vertex, listVisit)
        insertInPath(graph, nearest, path, listVisit)

    firstVertex = path[0]
    n = len(path)
    for index, i in enumerate(path):
        if i != path[n - 1]:
            edges.append(
                Edges(i, path[index + 1], weightEdge(graph.vertex[i], graph.vertex[path[index + 1]])))
    edges.append(Edges(i, firstVertex, weightEdge(
        graph.vertex[firstVertex], graph.vertex[i])))

    sumWeight = 0
    for edge in edges:
        sumWeight += edge.weight

    return sumWeight, edges


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
                                d1 = weightValue(
                                    graph.vertex[i.x], graph.vertex[i.y], graph.vertex[j.x], graph.vertex[j.y], graph.vertex[k.x], graph.vertex[k.y])
                                d2 = weightValue(
                                    graph.vertex[i.x], graph.vertex[k.y], graph.vertex[k.x], graph.vertex[i.y], graph.vertex[j.x], graph.vertex[j.y])
                                d3 = weightValue(
                                    graph.vertex[j.x], graph.vertex[i.x], graph.vertex[k.x], graph.vertex[i.y], graph.vertex[j.y], graph.vertex[k.y])
                                d4 = weightValue(
                                    graph.vertex[i.x], graph.vertex[j.x], graph.vertex[j.y], graph.vertex[k.x], graph.vertex[k.y], graph.vertex[i.y])
                                distanceList = [d1, d2, d3, d4]
                                minDistance = min(distanceList)
                                indexDistance = distanceList.index(minDistance)
                                if minDistance < (i.weight + j.weight + k.weight):
                                    if indexDistance == 0:
                                        ix, iy = i.x, i.y
                                        jx, jy = j.x, j.y
                                        kx, ky = k.x, k.y
                                        i.setEdge(ix, jx, weightEdge(
                                            graph.vertex[ix], graph.vertex[jx]))
                                        j.setEdge(iy, kx, weightEdge(
                                            graph.vertex[iy], graph.vertex[kx]))
                                        k.setEdge(jy, ky, weightEdge(
                                            graph.vertex[jy], graph.vertex[ky]))
                                        swap3(indexi, indexj, edges)
                                        swap3(indexj, indexk, edges)
                                    elif indexDistance == 1:
                                        ix, iy = i.x, i.y
                                        jx, jy = j.x, j.y
                                        kx, ky = k.x, k.y
                                        i.setEdge(ix, kx, weightEdge(
                                            graph.vertex[ix], graph.vertex[kx]))
                                        j.setEdge(jy, iy, weightEdge(
                                            graph.vertex[jy], graph.vertex[iy]))
                                        k.setEdge(jx, ky, weightEdge(
                                            graph.vertex[jx], graph.vertex[ky]))
                                        swap3(indexj, indexk, edges)
                                    elif indexDistance == 2:
                                        ix, iy = i.x, i.y
                                        jx, jy = j.x, j.y
                                        kx, ky = k.x, k.y
                                        i.setEdge(ix, jy, weightEdge(
                                            graph.vertex[ix], graph.vertex[jy]))
                                        j.setEdge(kx, jx, weightEdge(
                                            graph.vertex[kx], graph.vertex[jx]))
                                        k.setEdge(iy, ky, weightEdge(
                                            graph.vertex[iy], graph.vertex[ky]))
                                        swap3(indexi, indexj, edges)
                                    else:
                                        ix, iy = i.x, i.y
                                        jx, jy = j.x, j.y
                                        kx, ky = k.x, k.y
                                        i.setEdge(ix, jy, weightEdge(
                                            graph.vertex[ix], graph.vertex[jy]))
                                        j.setEdge(kx, iy, weightEdge(
                                            graph.vertex[kx], graph.vertex[iy]))
                                        k.setEdge(jx, ky, weightEdge(
                                            graph.vertex[jx], graph.vertex[ky]))
    sumWeight = 0
    for edge in edges:
        sumWeight += edge.weight

    return sumWeight


def writeResults(nearestNeihgborWeihgt, nearestInsertionWeight, opt2, opt3, path):
    response = "./results/"+path
    arq = open(response, 'w')
    arq.write("Teste: " + path+"\n")
    arq.write("Nearest Neihgbor: " + str(nearestNeihgborWeihgt)+"\n")
    arq.write("Opt 2 para Nearest Neihgbor: " + str(opt2[0])+"\n")
    arq.write("Opt 3 para Nearest Neihgbor: " + str(opt3[0])+"\n")
    arq.write("Nearest insertion: " + str(nearestInsertionWeight)+"\n")
    arq.write("Opt 2 para Nearest insertion: " + str(opt2[1])+"\n")
    arq.write("Opt 3 para Nearest insertion: " + str(opt3[1])+"\n")

    arq.close()


if __name__ == '__main__':
    print("Input or Test")
    answer = input()
    if answer == 'Test':
        for test in TESTS:
            resultNeighbor = 0
            resultInsertion = 0
            timeStart = time.time()
            opt2Cases = [0, 0]
            opt3Cases = [0, 0]
            graph = makeGraph(test)
            newpath = test.split("/")

            resultNeighbor, edges = nearestNeighbor(graph)
            edgesCopy = copy.deepcopy(edges)
            writeResults(resultNeighbor, resultInsertion,
                         opt2Cases, opt3Cases, newpath[1])
            print("Nearest Neihgbor ready for 2-Opt")

            result2 = twoOpt(edges, graph)
            opt2Cases[0] = result2
            writeResults(resultNeighbor, resultInsertion,
                         opt2Cases, opt3Cases, newpath[1])
            print("2-Opt Nearest Neihgbor ready for 3-Opt")

            result3 = threeOpt(edgesCopy, graph)
            opt3Cases[0] = result3
            writeResults(resultNeighbor, resultInsertion,
                         opt2Cases, opt3Cases, newpath[1])

            resultInsertion, edges = nearestInsertion(graph)
            edgesCopy = copy.deepcopy(edges)
            writeResults(resultNeighbor, resultInsertion,
                         opt2Cases, opt3Cases, newpath[1])
            print("Nearest Insertion ready for 2-Opt")

            result2 = twoOpt(edges, graph)
            opt2Cases[1] = result2
            writeResults(resultNeighbor, resultInsertion,
                         opt2Cases, opt3Cases, newpath[1])
            print("2-Opt Nearest Insertion ready for 3-Opt")

            result3 = threeOpt(edgesCopy, graph)
            opt3Cases[1] = result3
            timeEnd = time.time()
            print(timeEnd - timeStart)

            writeResults(resultNeighbor, resultInsertion,
                         opt2Cases, opt3Cases, newpath[1])
    elif answer == 'Input':
        exit = 'continue'
        while exit != "Exit":
            graph = readInput()
            resultNN, edges = nearestNeighbor(graph)
            result2 = twoOpt(edges, graph)
            result3 = threeOpt(edges, graph)
            print("Nearest Neighbor ", resultNN)
            print("2-Opt ", result2)
            print("3-Opt ", result3)
            resultNI, edges = nearestInsertion(graph)
            result2 = twoOpt(edges, graph)
            result3 = threeOpt(edges, graph)
            print("Nearest Insertion ", resultNI)
            print("2-Opt ", result2)
            print("3-Opt ", result3)
            exit = input()
