import os
import sys
import time
import pandas as pd 

def sand_mover(map: list,coordinates: tuple)-> bool:
    if coordinates[1] > 198 or map[coordinates[1]][coordinates[0]] == 'o':
        return False
    down = (coordinates[0],coordinates[1]+1)
    down_left = (coordinates[0]-1,coordinates[1]+1)
    down_right = (coordinates[0]+1,coordinates[1]+1)
    if map[down[1]][down[0]] == '.':
        return sand_mover(map,(down[0],down[1]))
    elif  map[down_left[1]][down_left[0]] == '.':
        return sand_mover(map,(down_left[0],down_left[1]))
    elif  map[down_right[1]][down_right[0]] == '.':
        return sand_mover(map,(down_right[0],down_right[1]))
    map[coordinates[1]][coordinates[0]] = 'o'
    return True

def custom_range(start, end):
    step = 1 if start <= end else -1
    return list(range(start, end + step, step))

def main(*args) -> None:
    
    cave_array = [['.' for x in range(0,800)] for y in range(0,200)]
    dir = os.path.dirname(sys.argv[0])
    maxY=0
    with open(f'{dir}/input.txt', 'r') as f:
        for line in f:
            rock = line.strip().split('->')
            for i,dot in enumerate(rock):
                startX,startY = (int(element) for element in dot.strip().split(','))
                try:
                    endX,endY = (int(element) for element in rock[i+1].strip().split(','))
                    for k in custom_range(startY,endY):
                        maxY = max(maxY,endY)
                        for j in custom_range(startX,endX):
                            cave_array[k][j] = '#'
                except IndexError:
                    _ = 'end of list'

    if args[0] == 1:
        can_move = True
        sand_units = 0
        while can_move:
            can_move = sand_mover(cave_array,(500,0))
            sand_units += 1
        df = pd.DataFrame(cave_array)
        selected_data = df.iloc[0:180, 480:600]
        print(selected_data)
        print(sand_units-1)
        selected_data.to_csv(f'{dir}/filled_cave.csv')

    if args[0] == 2:
        can_move = True
        sand_units = 0
        for i,_ in enumerate(cave_array[maxY+2]):
            cave_array[maxY+2][i] = '#'
        while can_move:
                can_move = sand_mover(cave_array,(500,0))
                sand_units += 1
        df = pd.DataFrame(cave_array)
        selected_data = df.iloc[0:180, 200:800]
        print(selected_data)
        print(sand_units-1)
        selected_data.to_csv(f'{dir}/filled_cave2.csv')        
if __name__ == '__main__':
    startTime = time.time()
    main(1)
    print('Part1',time.time()-startTime)
    startTime = time.time()
    main(2)
    print('Part2',time.time()-startTime)