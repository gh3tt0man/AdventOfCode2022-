# Part 1
import os
import sys
dir = os.path.dirname(sys.argv[0])


def calcWin(x, y):
    return {
        'A': {'Y': 8,
              'X': 4,
              'Z': 3}.get(y),
        'B': {'Y': 5,
              'X': 1,
              'Z': 9}.get(y),
        'C': {'Y': 2,
              'X': 7,
              'Z': 6}.get(y),
    }.get(x)  # 0 is the default value if x is not found in the dictionary


score = 0
with open(f'{dir}/input.txt', 'r') as f:
    for line in f:
        score += calcWin(line[0], line[2])
    print(score)


# Part2
# Y Draw
# X loose
# Z Win

# A Rock
# B Paper
# C Scisors
'''
(1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round 
(0 if you lost, 3 if the round was a draw, and 6 if you won).
'''
# Part 1


def calcWin2(x, y):
    return {
        'A': {'Y': 4,
              'X': 3,
              'Z': 8}.get(y),
        'B': {'Y': 5,
              'X': 1,
              'Z': 9}.get(y),
        'C': {'Y': 6,
              'X': 2,
              'Z': 7}.get(y),
    }.get(x)  # 0 is the default value if x is not found in the dictionary


score = 0
with open(f'{dir}/input.txt', 'r') as f:
    for line in f:
        score += calcWin2(line[0], line[2])
    print(score)
