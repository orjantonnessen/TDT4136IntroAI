# A* Algorithm
# Ørjan Sandvik Tønnessen
# 22.09.2018
# TDT4136

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

#Initialization ------------------------------------------------------------

def fillBoard(boardFile):
    for y in range(ny):
        string = boardFile.readline().strip('\n')
        for c in string:
            board.append(c)

def printBoard(board):
printB=open("")
    for x in range(nx):


#Initializing -----------------------------------------------------------------
fillBoard(boardFile)




