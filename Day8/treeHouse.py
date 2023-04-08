# Part 1

import os
import sys
dir = os.path.dirname(sys.argv[0])
score = 0

array = []
with open(f'{dir}/input.txt', 'r') as f:
    for i, line in enumerate(f):
        array.append([x for x in line.strip()])


sum=0
rowLength=0
for rowNum,row in enumerate(array):
    rowLength = len(row)
    for charNum,char in enumerate(row):
        visible=0
        if rowNum == 0 or charNum == 0 or charNum == len(row)-1 or rowNum == len(array)-1:
            continue
        #left search
        for x in range(0,charNum):
            if row[x] < char:
                visible += 1            
        if visible >= charNum:
            sum +=1
            continue
        visible = 0
        for z in range(charNum+1,len(row)): # charNum=1 , range 2 to 5 , 2,3,4 ,visible = 3
            if row[z] < char:
                visible += 1
        if visible >= len(row)-1-charNum: # 5 - 1 - 1 = 3        
            sum +=1
            continue
        visible = 0
        for y in range(0,rowNum):
            if array[y][charNum] < char:
                visible += 1
        if visible >= rowNum:        
            sum +=1
            continue 
        visible = 0 
        for k in range(rowNum+1,len(array)):
            if array[k][charNum] < char:
                visible +=1
        if visible >= len(array)-1-rowNum:            
            sum +=1 
    #print(char)
sum += rowLength * 2 + (len(array)-2)*2
print(sum)


#Part2

# Part 1

score = 0

array = []
with open(f'{dir}/input.txt', 'r') as f:
    for i, line in enumerate(f):
        array.append([x for x in line.strip()])


arrayViews=[]
sum=0
rowLength=0
for rowNum,row in enumerate(array):
    rowLength = len(row)
    for charNum,char in enumerate(row):
        visibleX=0
        visibleY=0
        visibleZ=0
        visibleD=0
        if rowNum == 0 or charNum == 0 or charNum == len(row)-1 or rowNum == len(array)-1:
            continue
        #left search
        for x in range(charNum-1,-1,-1):
            if row[x] < char:
                visibleX += 1            
            else:
                visibleX += 1
                break
        for z in range(charNum+1,len(row)): # charNum=1 , range 2 to 5 , 2,3,4 ,visible = 3
            if row[z] < char:
                visibleY += 1
            else:
                visibleY += 1
                break
        for y in range(rowNum-1,-1,-1):
            if array[y][charNum] < char:
                visibleZ += 1
            else:
                visibleZ += 1
                break
        for k in range(rowNum+1,len(array)):
            if array[k][charNum] < char:
                visibleD +=1
            else:
                visibleD += 1
                break                
        if visibleX and visibleY and visibleZ and visibleD:
            arrayViews.append(visibleX*visibleY*visibleZ*visibleD)
    #print(char)

arrayViews.sort()
print(arrayViews[-1])