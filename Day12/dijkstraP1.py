### Very slow Dijkstras implementation with a Ordrered dict
import os
import sys
import pandas as pd
from collections import OrderedDict
import time
sys.setrecursionlimit(10000)
def findNeighbour(map: list,point: tuple)-> list:
    neighbours = []
    y = point[0]
    x = point[1]

    if map[y-1][x]-1 <= map[y][x] and y-1 >= 0:
        neighbours.append((y-1,x))
    if map[y][x-1]-1 <= map[y][x] and x-1 >= 0:
        neighbours.append((y,x-1))
    if x+1 <= len(map[0])-1:    
        if map[y][x+1]-1 <=map[y][x]:
            neighbours.append((y,x+1))
    if y+1 <= len(map)-1:
        if map[y+1][x]-1 <= map[y][x]:
            neighbours.append((y+1,x))
    return neighbours

def visitPoint(members,point,array,visited=OrderedDict()):
    neigh = findNeighbour(array,point)
    for x in neigh:
        try:
            members[x][0] = members[point][0]+1
        except:
            _ ="bla"
              
    visited[point]= members.pop(point)
    #unVisited = OrderedDict((k,v) for k,v in members.items() if v[1] <1 )
    try:
        nxt = next(iter(OrderedDict(sorted(members.items(),key=lambda x: x[1][0]))))
        visitPoint(members,nxt,array,visited)
    except StopIteration:
        return visited
    return visited
def main(*args) -> None:
    # Part 1

    dir = os.path.dirname(sys.argv[0])
    
    with open(f'{dir}/input.txt', 'r') as f:
        map = f.read()
    array =[[]]
    j = 0
    lenLine=0
    lenLine = map.index('\n')
    for i,char in enumerate(map):
        if char == '\n':
            j+=1
            array.append([])            
        else:        
            ascii = int(ord(char))-97
            array[j] += [ascii]
            if ascii == -14:
                startIndex = [j,i-(lenLine+1)*j]
            if ascii == -28:
                endIndex = [j,i-(lenLine+1)*j]

    #df =  pd.DataFrame(array)

    #print(endIndex)

    array[startIndex[0]][startIndex[1]] = 0
    array[endIndex[0]][endIndex[1]] = 25
    print(findNeighbour(array,(0,0)))

    members = {}
    for i,x in enumerate(array):
        for j,z in enumerate(x):
            members[i,j] =[99999,0]
    sum=0
                                
    #set initial start point to 0 distance
    members = OrderedDict(members)
    members[tuple(startIndex)][0] = 0
    b = visitPoint(members,tuple(startIndex),array)
    print(b)
    print(b[tuple(endIndex)])
'''
    while unvisited:
        neighbors = findNeighbour(array,unvisited[0])
        for x in neighbors:
            members[x]=
 '''   
if __name__ == '__main__':
    startTime = time.time()
    main()
    endTime = time.time()
    print(endTime-startTime)
   # main(2)
