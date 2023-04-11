# Part 1

##Make the tail positions 1s , and mark with 1 where the tail has been
import os
import sys
import pandas as pd
dir = os.path.dirname(sys.argv[0])

sum=0
CPUcycle=0
X=1

with open(f'{dir}/input.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if line == 'noop':
            CPUcycle+=1
            if CPUcycle in [20,60,100,140,180,220]:            
                sum+=CPUcycle*X            
                print('cycle:',CPUcycle,'sum:',sum,'X:',X)                
            continue        
        CPUcycle+=1
                        
        if CPUcycle in [20,60,100,140,180,220]:            
            sum+=CPUcycle*X            
            print('cycle:',CPUcycle,'sum:',sum,'X:',X)
        CPUcycle+=1
        if CPUcycle in [20,60,100,140,180,220]:            
            sum+=CPUcycle*X
            print('cycle:',CPUcycle,'sum:',sum,'X:',X)
        value = int(line.split(' ')[1])              
        
              
        X+=value
print(sum)

#Part2

CRT = [['.' for _ in range(0,40)] for _ in range(0,6)]

def update_crt(row,CPUcycle,X):
    if row == 0:
        dx = CPUcycle-1-X
    else:
        dx = (CPUcycle-1-40*row)-X
    if dx in range(-1,2):
        CRT[row][CPUcycle-1-row*40]='#'
    if CPUcycle%40 == 0:
        row+=1    

CPUcycle=0
X=1
row=0
with open(f'{dir}/input.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if line == 'noop':
            CPUcycle+=1
            print('CPU:',CPUcycle,'row:',row,'X:',X)

            if row == 0:
                dx = CPUcycle-1-X
            else:
               dx = (CPUcycle-1-40*row)-X                        
            if dx in range(-1,2):
                CRT[row][CPUcycle-1-row*40]='#'
            if CPUcycle%40 == 0:
                row+=1                
            continue                

        CPUcycle+=1
        print('CPU:',CPUcycle,'row:',row,'X:',X)

        if row == 0:
            dx = CPUcycle-1-X
        else:
            dx = (CPUcycle-1-40*row)-X
        if dx in range(-1,2):
            CRT[row][CPUcycle-1-row*40]='#'
        if CPUcycle%40 == 0:
            row+=1

        CPUcycle+=1
        print('CPU:',CPUcycle,'row:',row,'X:',X)

        if row == 0:
            dx = CPUcycle-1-X
        else:
            dx = (CPUcycle-1-40*row)-X
        if dx in range(-1,2):
            CRT[row][CPUcycle-1-row*40]='#' 
        if CPUcycle%40 == 0:
            row+=1

        value = int(line.split(' ')[1])              
        
              
        X+=value




df = pd.DataFrame(CRT)
# Display the DataFrame
print(df)
'''
cpu 18  X 20
18 - 20 = -2 NOK

cpu 19 X 20 = -1 OK

CPU 21 X 20 = 1 OK
CPU 22 X 20 = 2 NOK

CPU 70 X 71  = oK pixel 70#

70/2
'''