# -*- coding: cp1252 -*-

#A* algorithm

boardFile = open("board-1-1.txt", "r")

nx, ny = 20, 7         #antall kolonner og rader
A,B = -1, -1          #Initiell node for A og B

board = []      #brettet som en liste

parent, hValues, gValues, cost = [], [], [], []
#parent har referanse til hvilken node som er forelder
#H-verdier for alle noder
#G-verdier for alle noder
#cost angir kostnader for å komme til en gitt node

openList, closedList = [], []

#Initialisering --------------------------------------------------------------------

def fillBoard(boardFile):
    for y in range(ny):
        string = boardFile.readline().strip('\n')
        for c in string:
            board.append(c)

def updateA(board):             #finner node A
    for n in range(ny*nx):
        if board[n] == 'A':
            global A
            A = n
            openList.append(A)

def updateB(board):             #finner node B
    for n in range(ny*nx):
        if board[n] == 'B':
            global B
            B = n

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
    print(name)
    for n in range(nx*ny):
        if n % nx == 0: #modulo
            print('\n')
        print("{:2}".format(listToPrint[n]))
    print('\n')

#Initialisering ---------------------------------------------------------------------

fillBoard(boardFile)
updateA(board)
updateB(board)
initHValues()
initGValues()
initParent()
initCost()


#Logikk for å legge til nabonoder-------------------------------------------------------------------           

def addRight(c):
    if (c+1) in closedList or (c+1) >= nx*ny:
        return
    if (c+1) in openList:
        if gValues[c] + cost[c+1] < gValues[c+1]:
                gValues[c+1] = gValues[c] + cost[c+1]
                parent[c+1] = c
                return
    if (c+1) % nx != 0:
        if board[c+1] != '#':
            openList.append(c+1)
            gValues[c+1] = gValues[c] + cost[c+1]
            parent[c+1] = c
            
        else:
            closedList.append(c+1)

def addLeft(c):
    if (c-1) in closedList or (c-1) % nx == 19:
        return
    if (c-1) in openList:
        if gValues[c] + cost[c-1] < gValues[c-1]:
                gValues[c-1] = gValues[c] + cost[c-1]
                parent[c-1] = c
                return
    if (c-1) % nx != 19:
        if board[c-1] != '#':
            openList.append(c-1)
            gValues[c-1] = gValues[c] + cost[c-1]
            parent[c-1] = c
            
        else:
            closedList.append(c-1)

def addOver(c):
    if (c-nx) in closedList or (c-nx) < 0:
        return
    if (c-nx) in openList:
        if gValues[c] + cost[c-nx] < gValues[c-nx]:
                gValues[c-nx] = gValues[c] + cost[c-nx]
                parent[c-nx] = c
                return
    if board[c-nx] != '#':
        openList.append(c-nx)
        gValues[c-nx] = gValues[c] + cost[c-nx]
        parent[c-nx] = c
            
    else:
        closedList.append(c-nx)

def addUnder(c):
    if (c+nx) in closedList or (c+nx) >= nx*ny:
        return
    if (c+nx) in openList:
        if gValues[c] + cost[c+nx] < gValues[c+nx]:
            gValues[c+nx] = gValues[c] + cost[c+nx]
            parent[c+nx] = c
            return
    if board[c+nx] != '#':
        openList.append(c+nx)
        gValues[c+nx] = gValues[c] + cost[c+nx]
        parent[c+nx] = c
            
    else:
        closedList.append(c+nx)


def addNeighboursTo(c):         #Samler det å legge til nye nabonoder
    addRight(c)
    addLeft(c)
    addOver(c)
    addUnder(c)

#Finner ny current ----------------------------------------------------
def findNewCurrent():           
    fLow = 1000
    node = -1
    for n in openList:
        if gValues[n] + hValues[n] <= fLow:
            fLow = gValues[n] + hValues[n]
            node = n
    return node
        
#main() ---------------------------------------------------------
c = A

while c != B:
    c = findNewCurrent()
    closedList.append(c)
    openList.remove(c)
    addNeighboursTo(c)
    
shortestPath = []
spStart = c
while spStart != A:
    if spStart != B and spStart != A:
        shortestPath.append(spStart)
    spStart = parent[spStart]

for node in shortestPath:
    board[node] = "O"

#printBoard("G-verdier", gValues)
printBoard("Løsning", board)


