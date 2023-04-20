import os
import sys
import pandas as pd
from collections import OrderedDict
import time
import heapq
import copy

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

#Find path using Dijstras with priority queue
def visitPoint(memb,point: tuple,array):
    
    visited = OrderedDict()
    members=copy.deepcopy(memb)
    queue = [point]
    members[point[1]][0] = 0
    while queue:
       
        nxt = heapq.heappop(queue)
   
        neigh = findNeighbour(array,nxt[1])
        
        for x in neigh:
            if x not in visited:
                if members[x][0] > members[nxt[1]][0]+1:
                    members[x] = [members[nxt[1]][0]+1,nxt[1]]           
                    heapq.heappush(queue,(members[x][0],x))
                 
        visited[nxt[1]]= members[nxt[1]]
       
    
    return visited

#Find the path with A*
def aStar(memb,point: tuple,array,endIndex):
    
    visited = OrderedDict()
    members=copy.deepcopy(memb)
    queue = [point]
    members[point[1]][0] = 0
    while queue:
       
        nxt = heapq.heappop(queue)
   
        neigh = findNeighbour(array,nxt[1])
        
        for x in neigh:
            if x not in visited:
                if members[x][0] > members[nxt[1]][0]+1:
                    members[x] = [members[nxt[1]][0]+1,nxt[1]]
                    #Manhattan distance heuristic
                    #dist = abs(endIndex[0]-x[0])+abs(endIndex[1]-x[1])
                    #Height difference heuristic + Manhattan
                    dist = abs(endIndex[0]-x[0])+abs(endIndex[1]-x[1]) + 2*(array[endIndex[0]][endIndex[1]]-array[x[0]][x[1]])
                    heapq.heappush(queue,(members[x][0]+dist,x))
                 
        visited[nxt[1]]= members[nxt[1]]
        if nxt[1]==tuple(endIndex):            
            return visited
    
    return visited    
def main(*args) -> None:
    # Part 1
    startIndex =[]
    endIndex = []
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



    array[startIndex[0]][startIndex[1]] = 0
    array[endIndex[0]][endIndex[1]] = 25

    memb = {}
    zeros=[]
    for i,x in enumerate(array):
        for j,z in enumerate(x):
            memb[i,j] =[float('inf'),None]
            if z == 0:
                zeros+= [(i,j)]
    
                            
    #set initial start point to 0 distance
    memb = OrderedDict(memb)
    startTuple=(0,tuple(startIndex))
    #Part1
    if args[0] == 1:
        b = visitPoint(memb,startTuple,array)
        #
        print(b[tuple(endIndex)])


    #Part 2
        #reverse the map and find the shortest path from the end to all other points
        aIndex = []

        for k,z in enumerate(array):
            for f,l in enumerate(z):
                array[k][f]=25-array[k][f]
                if array[k][f] == 25:
                    aIndex.append([k,f])
        startTuple = (0,tuple(endIndex))
        a = visitPoint(memb,startTuple,array)
        pathsToA=[]
        for iPoint in aIndex:
            try:
                pathsToA.append(a[tuple(iPoint)][0])
            except KeyError:
                _ = "No path"
            
        print(min(pathsToA))

    if args[0] == '1*':
        b = aStar(memb,startTuple,array,endIndex)
        #
        print(b[tuple(endIndex)])
        x=0
        y=0
        
        for key,value in b.items():
            if y < key[0]:
                y = key[0]
            if x < key[1]:
                x = key[1]
        visual = [['.' for k in range(0,x+1)] for h in range(0,y+1)]
        startReached = tuple(copy.deepcopy(endIndex))
        while startReached:
            visual[startReached[0]][startReached[1]] = '*'
            startReached = b[startReached][1]
        df = pd.DataFrame(visual)
        #print(df)
        df.to_csv(f'{dir}/path.csv')
        visual = [['.' for k in range(0,x+1)] for h in range(0,y+1)]
        #Visualize all explored nodes
        for key,value in b.items():
            visual[key[0]][key[1]] = '*'
        
        df = pd.DataFrame(visual)
        #print(df)
        df.to_csv(f'{dir}/visited2.csv')
        
    if args[0] == '2*':
        
        
        #Part 2 A*
        c=[]   
        for item in zeros:
            startTpl = (0,item)        
            a = aStar(memb,startTpl,array,endIndex)
            print(item,end="\r")
            #print(a[tuple(endIndex)])
            try:
                c += [a[tuple(endIndex)]]
            except KeyError:
                _ ='no path'
        
        print('MIN value is',min(c))

if __name__ == '__main__':
    startTime = time.time()
    main(1)
    print('Dijkstras',time.time()-startTime)
    startTime = time.time()
    #main('2*')
    print('A*',time.time()-startTime)