# A* Algorithm
# Ørjan Sandvik Tønnessen
# 22.09.2018
# TDT4136

boardFile = open("board-1-1.txt", "r")

nx, ny = 20, 7         #antall kolonner og rader
A,B = -1, -1          #Initiell node for A og B

board = []      #brettet som en liste

parent, hValues, gValues, fValues, cost = [], [], [], [], []
#parent har referanse til hvilken node som er forelder
#H-verdier for alle noder
#G-verdier for alle noder
#F-verdier for alle noder
# cost angir kostnader for å komme til en gitt node
import sys
openList, closedList = [], []

#Initialization ------------------------------------------------------------

def fillBoard(boardFile):
    for y in range(ny):
        string = boardFile.readline().strip('\n')
        for c in string:
            board.append(c)

def initHValues():
    Bx = B % nx
    By = B // nx
    for n in range(nx*ny):
        hValues.append(abs(((n % nx)-Bx))+abs(((n // nx)-By)))


def initGValues():
    for n in range(nx*ny):
        gValues.append(-1)
    gValues[A] = 0

def initCost():
    for n in range(nx*ny):
        cost.append(1)


def initParent():
    for n in range(nx*ny):
        parent.append(-1)

# Printing -----------------------------------------------------------------
def printBoard(name, listToPrint):
    import sys
    with open("C:\GitHub\TDT4136IntroAI\solution1-1.txt", "w") as f: #('c:\\goat.txt', 'w') as f:
        sys.stdout = f
        print(name)
        row = ""
        for n in range(nx*ny):
            row=row+listToPrint[n]
            if (n+1) % nx == 0: #modulo
                print(row)
                #print()
                row = ""

#Initializing -----------------------------------------------------------------
fillBoard(boardFile)
initHValues()
initGValues()
initParent()
initCost()

#Definitions-------------------------------------------------------------------
def x_coordinate(Node):
    counter = 0
    for ycount in range(ny):
        for xcount in range(nx):
            if counter == Node:
                return xcount
            counter += 1
            xcount += 1
        ycount += 1

def y_coordinate(Node):
    counter = 0
    for ycount in range(ny):
        for xcount in range(nx):
            if counter == Node:
                return ycount
            counter += 1
            xcount += 1
        ycount += 1

def manhattan(startNode,endNode):
        x1=x_coordinate(startNode)
        y1=y_coordinate(startNode)
        x2=x_coordinate(endNode)
        y2=y_coordinate(endNode)
        return abs(x1-x2)+abs(y1-y2)

def findA(Lista):
    n=0
    while n<=nx*ny:
        if Lista[n]=="A":
            return n
        n+=1
    return False

def findB(Listb):
    n=0
    while n<=nx*ny:
        if Listb[n]=="B":
            return n
        n += 1
    return False


# Logikk for å legge til nabonoder-------------------------------------------------------------------

def addRight(c):
    if (c + 1) in closedList or (c + 1) >= nx * ny:
        return
    if (c + 1) in openList:
        if gValues[c] + cost[c + 1] < gValues[c + 1]:
            gValues[c + 1] = gValues[c] + cost[c + 1]
            parent[c + 1] = c
            return
    if (c + 1) % nx != 0:
        if board[c + 1] != '#':
            openList.append(c + 1)
            gValues[c + 1] = gValues[c] + cost[c + 1]
            parent[c + 1] = c

        else:
            closedList.append(c + 1)


def addLeft(c):
    if (c - 1) in closedList or (c - 1) % nx == 19:
        return
    if (c - 1) in openList:
        if gValues[c] + cost[c - 1] < gValues[c - 1]:
            gValues[c - 1] = gValues[c] + cost[c - 1]
            parent[c - 1] = c
            return
    if (c - 1) % nx != 19:
        if board[c - 1] != '#':
            openList.append(c - 1)
            gValues[c - 1] = gValues[c] + cost[c - 1]
            parent[c - 1] = c

        else:
            closedList.append(c - 1)


def addOver(c):
    if (c - nx) in closedList or (c - nx) < 0:
        return
    if (c - nx) in openList:
        if gValues[c] + cost[c - nx] < gValues[c - nx]:
            gValues[c - nx] = gValues[c] + cost[c - nx]
            parent[c - nx] = c
            return
    if board[c - nx] != '#':
        openList.append(c - nx)
        gValues[c - nx] = gValues[c] + cost[c - nx]
        parent[c - nx] = c

    else:
        closedList.append(c - nx)


def addUnder(c):
    if (c + nx) in closedList or (c + nx) >= nx * ny:
        return
    if (c + nx) in openList:
        if gValues[c] + cost[c + nx] < gValues[c + nx]:
            gValues[c + nx] = gValues[c] + cost[c + nx]
            parent[c + nx] = c
            return
    if board[c + nx] != '#':
        openList.append(c + nx)
        gValues[c + nx] = gValues[c] + cost[c + nx]
        parent[c + nx] = c

    else:
        closedList.append(c + nx)


def successors(node):  # Samler det å legge til nye nabonoder
    addRight(node)
    addLeft(node)
    addOver(node)
    addUnder(node)

def findNewCurrent():
    fLow = 1000
    node = -1
    for n in openList:
        if gValues[n] + hValues[n] <= fLow:
            fLow = gValues[n] + hValues[n]
            node = n
    return node

#Main -------------------------------------------------------------------------
A=findA(board)
B=findB(board)
gValues[A]=0
hValues[A]=manhattan(A,B)
#fValues[A]=hValues[A]+gValues[A]
openList.append(A)
node=A
while node!=B:
    #if not openList:
        #return False
    node = findNewCurrent()
    closedList.append(node)
    openList.remove(node)
    #if node==B:
    #    return node,parentFinder(node)
    successors(node)

shortestPath = []
spStart = node
while spStart != A:
    if spStart != B and spStart != A:
        shortestPath.append(spStart)
    spStart = parent[spStart]

for node in shortestPath:
    board[node] = "O"


printBoard("Result:",board)



