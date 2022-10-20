import heapq
from heapq import heappush, heappop, heapify
import math
from Utility import Node as n
from numpy import *

def  converttomatrix(puzzleOrder):
    matrix=[[0,0,0],[0,0,0],[0,0,0]]

    counter=0
    for i in range(3):
        for j in range(3):
            matrix[i][j]=puzzleOrder[counter]
            counter=counter+1
 #   for i in range(3):
   #     for j in range(3):


 #           print(matrix[i][j])

    return matrix
def getZeroIndex(p):
    for i in range(3):
        for j in range(3):
            if(p[i][j]=="0"):

                return i,j;
    return False,False;
def swapping(matrixpuzzle,x1,y1,x2,y2):
    path=""
    print("in swapping")
    matrixhelper = matrixpuzzle.copy()



    matrixhelper[x1][y1]=matrixhelper[x2][y2]
    matrixhelper[x2][y2] = "0"

    for i in range(3):
       for j in range(3):
           path=path+matrixhelper[i][j]


    print("path is "+ path)
    return path
def possibleMoves(puzzleOrder):
    possibleNodes=list()
    matrixpuzzle=array(converttomatrix(puzzleOrder))

    x,y=getZeroIndex(matrixpuzzle)
    #upmove
    if(x>0):

        newpath=swapping(matrixpuzzle,x,y,x-1,y)
        possibleNodes.append(newpath)


    #down move
    if(x!="2"):
        newpath = swapping(matrixpuzzle, x, y, x + 1, y)
        possibleNodes.append(newpath)
    #right move
    if(int(y)<2):

        newpath = swapping(matrixpuzzle, x, y, x , y+1)
        possibleNodes.append(newpath)
    #left move
    if (int(y) > 0):
        newpath = swapping(matrixpuzzle, x, y, x, y - 1)
        possibleNodes.append(newpath)
    return possibleNodes




def euclideanDistance(currstate):
    sum=0
    index=0

    for i in range(3):
        for j in range(3):
            xgoal=currstate.puzzleprder[index]/3
            ygoal=currstate.puzzleprder[index]%3
            index=index+1
            sum=sum+math.sqrt(math.pow(i-xgoal,2)+math.pow(j-ygoal,2))

    return sum





def aStar(initialState,heustric):
    global goalState
    goalState="012345678"
    depth=0;
    explored={}
    #current node #initial state
    rootnode=n.Node(depth,0,initialState)
    forinter=list()
    heapq.heappush(forinter,rootnode.cost)
    #check available moves
    newNodes=possibleMoves(initialState)
    depth=depth+1
    for x in range(len(newNodes)):
        print(newNodes[x])
        #n.Node(depth,cost,newNodes[x])
    #create new nodes and calculate its values in forinter









    #heap of nodes
aStar("125340678",5464)