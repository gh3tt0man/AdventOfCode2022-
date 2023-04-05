#Part 1
import os
import sys
dir = os.path.dirname(sys.argv[0])
score=0
with open(f'{dir}/input.txt','r') as f:
    for line in f:
        listOfLists =[[''] for i in range(int((len(line)-1)/3))]
        break

with open(f'{dir}/input.txt','r') as f:
    for i,line in enumerate(f):
        print(len(line))
        arr = [""]*(len(line)-1)
        for j,char in enumerate(line):
            if char == 'm':
                quit()
            if char == '\n':
                continue
            if char == ' ' or char == '[' or char == "]":
                continue
            listOfLists[int((j-1)/3)].append(char)
print(listOfLists)


#remove empty lists from list of lists

