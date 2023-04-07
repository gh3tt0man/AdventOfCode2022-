with open('input.txt', 'r') as f:
    contents = f.read()
# print(contents)
number = ""
listNumber = []
finalList = []
type(contents)
for line in contents:
    if line == ' ':
        continue
    if line != '\n':
        number += line
        newLine = False
    if line == '\n':
        if newLine:
            finalList.append(sum(listNumber))
            listNumber = []
            continue
        c = int(number)
        listNumber.append(c)
        newLine = True
        number = ''
print(finalList)

i = 0
biggest = 0
index = 0
secBiggest = 0
trdBiggest = 0
for item in finalList:
    if item > biggest:
        secBiggest = biggest
        index2 = index
        biggest = item
        index = i
    elif item > secBiggest:
        trdBiggest = secBiggest
        index3 = index2
        secBiggest = item
        index2 = i
    elif item > trdBiggest:
        trdBiggest = item
        index3 = i
    i += 1

print(finalList[index]+finalList[index2]+finalList[index3])
print(finalList[index], biggest)
print(finalList[index2], secBiggest)
print(finalList[index3], trdBiggest)


# for(line in contents):
