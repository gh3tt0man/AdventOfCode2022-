# Part 1

##Make the tail positions 1s , and mark with 1 where the tail has been
import os
import sys
import pandas as pd
dir = os.path.dirname(sys.argv[0])
score = 0

array=[['0']]

x=0
y=0
with open(f'{dir}/input.txt', 'r') as f:
    for i, line in enumerate(f):
        direction,moves = line.strip().split(' ')
        len(array)
        if direction == 'R':
            if len(array)-x-1 < int(moves):
                for j in range(0,int(moves)-len(array)+x+1):
                    cp = array[0].copy()
                    array.append(cp)
            try:           
                array[x+int(moves)][y] = '1'
            except:
                print('err')
            x +=  int(moves)
        if direction == 'L':
            array[x-int(moves)][y] = '1'
            x -= int(moves)
        if direction == 'U':
            if len(array[0])-y-1 < int(moves):
                for j in range(0,int(moves)-len(array[0])+y+1):
                    array = [row + ['0'] for row in array]
            array[x][y+int(moves)] = '1'
            y +=  int(moves)            
print(array)

# Create a DataFrame from the 2D array
df = pd.DataFrame(array)
df = df.T
df = df.iloc[::-1]
df.reset_index(drop=True, inplace=True)

# Display the DataFrame
print(df)