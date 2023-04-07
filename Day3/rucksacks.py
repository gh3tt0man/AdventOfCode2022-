# Part 1
import os
import sys
dir = os.path.dirname(sys.argv[0])
score = 0
with open(f'{dir}/input.txt', 'r') as f:
    for i, line in enumerate(f):
        stripped = line.strip()
        for char in set(stripped[0:int(len(stripped)/2)]):
            if char in set(stripped[int(len(stripped)/2):]):
                if char.isupper():
                    score += ord(char)-38
                if char.islower():
                    score += ord(char)-96


print(score)

# Part 2
b = 0
score = 0
with open(f'{dir}/input.txt', 'r') as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        if b == 2:
            for char in set(line):
                if char in set(lines[i-1]):
                    if char in set(lines[i-2]):
                        if char.isupper():
                            score += ord(char)-38
                        if char.islower():
                            score += ord(char)-96

            b = 0
            continue
        b += 1

print(score)
