#Part 1

import os
import sys
dir = os.path.dirname(sys.argv[0])
score=0


def add_sizes(nested_dict,key,size,dir):
    
    if dir:
        curr = my_object
        for key in dir:
            curr=curr[key]
            if 'size' not in curr:
                curr['size']=size
            else:
                curr['size']+=size

def getValues(nested_dict):
    sum=0    
    for key,value in nested_dict.items():        
        if isinstance(value,dict):
            if 'size' in value:
                if value['size'] <= 100000:
                    sum += value['size']
            sum += getValues(value)
    return sum


my_object = {}
current = my_object
currDir=[]
with open(f'{dir}/input.txt','r') as f:
    for i,line in enumerate(f):
        if line[0:4] == '$ cd':
            Null,command,destination = line.strip().split(' ')
            if destination == '..':                
                currDir = currDir[:-1]
                current = my_object                
                for key in currDir:
                    current=current[key]
                    lastKey=key

                continue
            currDir.append(destination)
            current[destination]={}
            current = current[destination]
            lastKey = destination
        if line[0].isdigit():
            if 'size' not in current:
                current['size']=int(line.split(' ')[0])
                try:
                    add_sizes(my_object,lastKey,int(line.split(' ')[0]),currDir[:-1])
                except:
                    print(line)
                    quit()                    
            else:
                current['size']+=int(line.split(' ')[0])
                add_sizes(my_object,lastKey,int(line.split(' ')[0]),currDir[:-1])


print(getValues(my_object))

#Part2
totalFree = 70000000 -my_object['/']['size']
totalNeeded = 30000000-totalFree
print(totalNeeded)
def getBiggest(nested_dict):
    sum=[]    
    for key,value in nested_dict.items():        
        if isinstance(value,dict):
            if 'size' in value:
                if value['size'] >= 4359867:
                    sum.append(value['size'])
            a = getBiggest(value)
            if a:
                for lst in a:
                    sum.append(lst)            
    if sum:
        return sum
bigg=[]    

bigg=getBiggest(my_object)
bigg.sort()
print(bigg[0])