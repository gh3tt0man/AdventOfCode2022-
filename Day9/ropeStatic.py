# Part 1

##Make the tail positions 1s , and mark with 1 where the tail has been
import os
import sys
import pandas as pd
dir = os.path.dirname(sys.argv[0])
score = 0

array=[[0 for x in range(0,1000)] for z in range(0,1000)]

Hx=500
Hy=500
Tx=500
Ty=500
array[Tx][Ty]=1
with open(f'{dir}/input.txt', 'r') as f:
    for i, line in enumerate(f):
        direction,moves = line.strip().split(' ')
        moves = int(moves)
        len(array)
        if direction == 'R':
            for move in range(0,moves):
                Hx += 1       
                if Hx - Tx  in range(-1,2) and Ty - Hy in range(-1,2):
                    continue
                if Ty - Hy == 0:
                    Tx = Hx-1
                    array[Tx][Ty] = 1
                else:
                    Ty = Hy
                    Tx = Hx-1
                    array[Tx][Ty] = 1
                        
        if direction == 'L':
            for move in range(0,moves):
                Hx += -1       
                if Hx - Tx  in range(-1,2) and Ty - Hy in range(-1,2):
                    continue
                if Ty - Hy == 0:
                    Tx = Hx+1
                    array[Tx][Ty] = 1
                else:
                    Ty = Hy
                    Tx = Hx+1
                    array[Tx][Ty] = 1
        if direction == 'U':
            for move in range(0,moves):
                Hy += 1       
                if Hx - Tx  in range(-1,2) and Ty - Hy in range(-1,2):
                    continue
                if Tx - Hx == 0:
                    Ty = Hy-1
                    array[Tx][Ty] = 1
                else:
                    Tx = Hx
                    Ty = Hy-1
                    array[Tx][Ty] = 1      
        if direction == 'D':
            for move in range(0,moves):
                Hy -= 1       
                if Hx - Tx  in range(-1,2) and Ty - Hy in range(-1,2):
                    continue
                if Tx - Hx == 0:
                    Ty = Hy+1
                    array[Tx][Ty] = 1
                else:
                    Tx = Hx
                    Ty = Hy+1
                    array[Tx][Ty] = 1            

print(sum(element for row in array for element in row))
# Create a DataFrame from the 2D array
'''
df = pd.DataFrame(array)
df = df.T
df = df.iloc[::-1]
df.reset_index(drop=True, inplace=True)



# Display the DataFrame
print(df)

'''

#part2
def position_next(Px,Py,Nx,Ny):
    if Px - Nx in range(-1,2) and Py - Ny in range(-1,2):
        return [Px,Py]    
    if Py - Ny <= -1 and Py - Ny != 0:
        Py += 1
    elif Py - Ny >= 1 and Py - Ny != 0:
        Py -= 1
    if Px - Nx <= -1 and Px - Nx != 0:
        Px += 1
    elif Px - Nx >= 1 and Px - Nx !=0:
        Px -=1

    return [Px,Py]



array=[[0 for x in range(0,1000)] for z in range(0,1000)]

Hx=500
Hy=500
Tx=500
Ty=500
array[Tx][Ty]=1

posRope = [[500,500] for x in range(0,10)]


with open(f'{dir}/input.txt', 'r') as f:
    for i, line in enumerate(f):
        direction,moves = line.strip().split(' ')
        moves = int(moves)
        if direction == 'R':
            for move in range(0,moves):
                Hx += 1
                #Head X is 0,0 head Y iaz 0,1
                posRope[0][0]+=1
                for i,item in enumerate(posRope[1:10]):
                    posRope[i+1] = position_next(item[0],item[1],posRope[i][0],posRope[i][1])
                    if i == 8:
                        array[posRope[i+1][0]][posRope[i+1][1]] = 1
                        
        if direction == 'L':
            for move in range(0,moves):                
                #Head X is 0,0 head Y iaz 0,1
                posRope[0][0]-=1
                for i,item in enumerate(posRope[1:10]):
                    posRope[i+1] = position_next(item[0],item[1],posRope[i][0],posRope[i][1])
                    if i == 8:
                        array[posRope[i+1][0]][posRope[i+1][1]] = 1

        if direction == 'U':
            for move in range(0,moves):
                posRope[0][1]+=1
                for i,item in enumerate(posRope[1:10]):
                    posRope[i+1] = position_next(item[0],item[1],posRope[i][0],posRope[i][1])
                    if i == 8:
                        array[posRope[i+1][0]][posRope[i+1][1]] = 1

        if direction == 'D':
            for move in range(0,moves):
                posRope[0][1]-=1
                for i,item in enumerate(posRope[1:10]):
                    posRope[i+1] = position_next(item[0],item[1],posRope[i][0],posRope[i][1])
                    if i == 8:
                        array[posRope[i+1][0]][posRope[i+1][1]] = 1


print(sum(element for row in array for element in row))

df = pd.DataFrame(array)
df = df.T
df = df.iloc[::-1]
df.reset_index(drop=True, inplace=True)
df =df.iloc[490:510, 490:510]


# Display the DataFrame
#print(df)


