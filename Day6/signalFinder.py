#Part 1
import os
import sys
dir = os.path.dirname(sys.argv[0])
score=0
with open(f'{dir}/input.txt','r') as f:
    a=f.read()


for i,char in enumerate(a):
    if i>2:
        if len(set([a[i-3],a[i-2],a[i-1],a[i]])) == 4:
            print(i+1)
            break

#Part 1

for i,char in enumerate(a):
    if i>12:
        if len(set([a[x] for x in range(i-13,i+1)])) == 14:
            print(i+1)
            break

