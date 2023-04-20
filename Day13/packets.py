import os
import sys
import time
import pandas as pd 

def comparePackets(array_first,array_second):
    if isinstance(array_second,int):
        array_second = [array_second]
    if isinstance(array_first,int):
        array_first = [array_first]
    for i,item in enumerate(array_first):
        if isinstance(item,list):
            try:
                result = comparePackets(item,array_second[i])
                if result == False:
                    return False
                if result == True:
                    return True                
            except IndexError:
                return False
        else:
            try:
                array_second[i]
            except IndexError:
                return False                
            if isinstance(array_second[i],list):
                result = comparePackets(item,array_second[i])
                if result == False:
                    return False
                if result == True:
                    return True

            else:                       
                if item < array_second[i]:
                    return True
                elif item == array_second[i]:
                    continue
                else:
                    return False
    if len(array_second) > len(array_first):
        return True
    return 'Continue'
def main(*args) -> None:
    
    dir = os.path.dirname(sys.argv[0])
    i=0
    j=False
    rightOrder=[]
    first_line=[]
    second_line=[]
    to_sort=[]
    with open(f'{dir}/input.txt', 'r') as f:
        to_sort.append([[2]])
        to_sort.append([[6]])
        for line in f:
            if line == '\n':
                j = False
                continue
            if j:
                second_line = eval(line.strip())
                in_order = comparePackets(first_line,second_line)
                if in_order==True or in_order =='Continue':
                    rightOrder.append(i)
                    to_sort.append(first_line)
                    to_sort.append(second_line)
                else:
                    to_sort.append(second_line)
                    to_sort.append(first_line)                    
                        
            else:
                first_line = eval(line.strip())
                j=True
                i+=1
      
    print(rightOrder)
    print(sum(rightOrder))


    #Part2,
    oredered = False
    
    while not oredered:
        oredered = True
        for k,item in enumerate(to_sort):
            try:
                if not comparePackets(item,to_sort[k+1]):
                    to_sort[k],to_sort[k+1] = to_sort[k+1],to_sort[k]
                    oredered = False
            except IndexError:
                _ = 'end of array'

    indice1, indice2 = [k + 1 for k, item in enumerate(to_sort) if item in ([[6]], [[2]])]

    print(indice1*indice2)
  #  df = pd.DataFrame(to_sort)
   # print(df)

if __name__ == '__main__':
    startTime = time.time()
    main()
    print('',time.time()-startTime)
