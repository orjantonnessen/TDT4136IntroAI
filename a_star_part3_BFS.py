# -*- coding: cp1252 -*-

#A* algorithm

boardFile = open("board-2-1.txt", "r")

nx, ny = 40, 10         #antall kolonner og rader
A,B = -1, -1          #Initiell node for A og B

board = []      

parent, hValues, gValues, fValues, cost = [], [], [], [], []
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
        x = n % nx
        y = n // nx
        hValues.append((abs(Bx-x)+abs(By-y)))


def initGValues():
    for n in range(nx*ny):
        gValues.append(-1)
    gValues[A] = 0

def initCost():
    for n in board:
        if n == 'w': cost.append(100)     
        if n == 'm': cost.append(50) 
        if n == 'f': cost.append(10) 
        if n == 'g': cost.append(5) 
        if n == 'r': cost.append(1) 
        if n == 'A': cost.append(0) 
        if n == 'B': cost.append(0) 
            


def initParent():
    for n in range(nx*ny):
        parent.append(-1)

def initFValues():
    for n in range(nx*ny):
        if(gValues[n] != -1):
            fValues.append(gValues[n] + hValues[n])
        else:
            fValues.append(-1)

# Printing -----------------------------------------------------------------
def printBoard(name, listToPrint):
    print name

    if(name == "Løsning"):
        for n in range(nx*ny):
            if n % nx == 0:
                print '\n'

            if n == A or n == B or listToPrint[n] == 'O':
                print "{:3}".format(listToPrint[n]),

            elif n in closedList:
                print "{:3}".format('X'),
            elif n in openList:
                print "{:3}".format('*'),

            else:    
                print "{:3}".format(listToPrint[n]),
        print ('\n')

    else:
        for n in range(nx*ny):
            if n % nx == 0:
                print '\n'
            print "{:3}".format(listToPrint[n]),
        print ('\n')

#Initialisering ---------------------------------------------------------------------

fillBoard(boardFile)
updateA(board)
updateB(board)
initCost()
initGValues()
initHValues()

initParent()



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
        openList.append(c+1)
        gValues[c+1] = gValues[c] + cost[c+1]
        parent[c+1] = c

def addLeft(c):
    if (c-1) in closedList or (c-1) % nx == nx - 1:
        return
    if (c-1) in openList:
        if gValues[c] + cost[c-1] < gValues[c-1]:
            gValues[c-1] = gValues[c] + cost[c-1]
            parent[c-1] = c
        return
    if (c-1) % nx != nx - 1:
        openList.append(c-1)
        gValues[c-1] = gValues[c] + cost[c-1]
        parent[c-1] = c

def addOver(c):
    if (c-nx) in closedList or (c-nx) < 0:
        return
    if (c-nx) in openList:
        if gValues[c] + cost[c-nx] < gValues[c-nx]:
            gValues[c-nx] = gValues[c] + cost[c-nx]
            parent[c-nx] = c
        return
    openList.append(c-nx)
    gValues[c-nx] = gValues[c] + cost[c-nx]
    parent[c-nx] = c

def addUnder(c):
    if (c+nx) in closedList or (c+nx) >= nx*ny:
        return
    if (c+nx) in openList:
        if gValues[c] + cost[c+nx] < gValues[c+nx]:
            gValues[c+nx] = gValues[c] + cost[c+nx]
            parent[c+nx] = c
        return
    openList.append(c+nx)
    gValues[c+nx] = gValues[c] + cost[c+nx]
    parent[c+nx] = c


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
        if(n in closedList):
            break
        if gValues[n] + hValues[n] <= fLow:
            fLow = gValues[n] + hValues[n]
            node = n
    return node
        
#main() ---------------------------------------------------------
c = 1

while c != B:
    c = openList[0]
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

printBoard("Løsning", board)


