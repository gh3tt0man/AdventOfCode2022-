# Part 1
import os
import sys
dir = os.path.dirname(sys.argv[0])
score = 0
with open(f'{dir}/input.txt', 'r') as f:
    for line in f:
        listOfLists = [[''] for i in range(int(len(line)))]
        break
moveMode = False
with open(f'{dir}/input.txt', 'r') as f:
    for i, line in enumerate(f):
        if len(line) < 3:
            moveMode = True
            cleanedList = []

            for b in listOfLists:
                if b != ['']:
                    b = [c for c in b if c]
                    cleanedList.append(b)
            continue
        arr = [""]*(len(line)-1)
        if not moveMode:
            for j, char in enumerate(line):
                if char == '\n':
                    continue
                if char == ' ' or char == '[' or char == "]":
                    continue
                listOfLists[int(j)].append(char)

        if moveMode:
            move = [int(x) for x in line.strip().split(' ') if x.isdigit()]
            # originator list
            rev = cleanedList[move[1]-1][:move[0]]
            rev.reverse()

            for k in range(len(rev)-1, -1, -1):
                cleanedList[move[2]-1].insert(0, rev[k])
            del cleanedList[move[1]-1][:move[0]]


print(''.join([y[0] for y in cleanedList]))


# Part 2
# only change is removal of .reverse()
dir = os.path.dirname(sys.argv[0])
score = 0
with open(f'{dir}/input.txt', 'r') as f:
    for line in f:
        listOfLists = [[''] for i in range(int(len(line)))]
        break
moveMode = False
with open(f'{dir}/input.txt', 'r') as f:
    for i, line in enumerate(f):
        if len(line) < 3:
            moveMode = True
            cleanedList = []

            for b in listOfLists:
                if b != ['']:
                    b = [c for c in b if c]
                    cleanedList.append(b)
            continue
        arr = [""]*(len(line)-1)
        if not moveMode:
            for j, char in enumerate(line):
                if char == '\n':
                    continue
                if char == ' ' or char == '[' or char == "]":
                    continue
                listOfLists[int(j)].append(char)

        if moveMode:
            move = [int(x) for x in line.strip().split(' ') if x.isdigit()]
            # originator list
            rev = cleanedList[move[1]-1][:move[0]]
            # rev.reverse()

            for k in range(len(rev)-1, -1, -1):
                cleanedList[move[2]-1].insert(0, rev[k])
            del cleanedList[move[1]-1][:move[0]]


print(''.join([y[0] for y in cleanedList]))
