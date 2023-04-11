# Part 1
import os
import sys
import pandas as pd
dir = os.path.dirname(sys.argv[0])

def update_sum_and_print(cycle, x, total):
    if cycle % 40 == 20:
        total += cycle * x
        print(f'cycle: {cycle}, sum: {total}, X: {x}')
    return total

sum = 0
CPUcycle = 0
X = 1

with open(f'{dir}/input.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if line == 'noop':
            CPUcycle += 1
            sum = update_sum_and_print(CPUcycle, X, sum)
            continue
        CPUcycle += 1
        sum = update_sum_and_print(CPUcycle, X, sum)
        CPUcycle += 1
        sum = update_sum_and_print(CPUcycle, X, sum)
        value = int(line.split(' ')[1])

        X += value
print(sum)

# Part2

CRT = [['.' for _ in range(0, 40)] for _ in range(0, 6)]
row = 0

def update_crt(CPUcycle, X, row):
    offset_cycle = CPUcycle - 1 - row * 40
    dx = offset_cycle - X
    if -2 < dx < 2:
        CRT[row][offset_cycle] = '#'
    if offset_cycle == 39:
        row += 1
    return row


CPUcycle = 0
X = 1

with open(f'{dir}/input.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if line == 'noop':
            CPUcycle += 1
            # print('CPU:',CPUcycle,'row:',row,'X:',X)
            row = update_crt(CPUcycle, X, row)
            continue

        CPUcycle += 1
        # print('CPU:',CPUcycle,'row:',row,'X:',X)
        row = update_crt(CPUcycle, X, row)

        CPUcycle += 1
        # print('CPU:',CPUcycle,'row:',row,'X:',X)
        row = update_crt(CPUcycle, X, row)

        value = int(line.split(' ')[1])

        X += value

df = pd.DataFrame(CRT)
# Display the DataFrame
print(df)
