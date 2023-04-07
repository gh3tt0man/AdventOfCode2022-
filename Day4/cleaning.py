# Part 1
import os
import sys
dir = os.path.dirname(sys.argv[0])
score = 0
with open(f'{dir}/input.txt', 'r') as f:
    for i, line in enumerate(f):
        first, second = line.split(",")
        arr1 = list(
            range(int(first.split("-")[0]), int(first.split("-")[1])+1))
        arr2 = list(
            range(int(second.split("-")[0]), int(second.split("-")[1])+1))

        if all(item in arr1 for item in arr2):
            score += 1
        elif all(item in arr2 for item in arr1):
            score += 1


print(score)

# part2
score = 0
with open(f'{dir}/input.txt', 'r') as f:
    for i, line in enumerate(f):
        first, second = line.split(",")
        arr1 = list(
            range(int(first.split("-")[0]), int(first.split("-")[1])+1))
        arr2 = list(
            range(int(second.split("-")[0]), int(second.split("-")[1])+1))
        if any([item in arr1 for item in arr2]):
            score += 1

print(score)
