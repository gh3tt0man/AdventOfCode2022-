import os
import sys
import math

class monkey():
    def __init__(self, items: list[int], inspectMultiple, test: int, monNum: int, ifTru: int, ifFalse: int) -> None:
        self.items = items
        self.inspectMultiple = inspectMultiple
        self.test = test
        self.monNum = monNum
        self.ifTru = ifTru
        self.ifFalse = ifFalse
        self.inspected = 0

    def inspectItem(self, part2=None):
        self.inspected += 1
        self.item = self.items[0]
        self.worry = self.item
        tst = self.test
        old = self.worry

        self.worry = eval(self.inspectMultiple) 

        if not part2:
            self.worry = self.worry // 3
        self.worry %= MONKEY_DIVISOR_CONSTANT
        self.items.pop(0)
        if self.worry % tst == 0:
            return [self.ifTru, self.worry]
        else:
            return [self.ifFalse, self.worry]

    def recieveItem(self, item):
        self.items += [item]

def main(*args) -> None:
    # Part 1

    dir = os.path.dirname(sys.argv[0])

    monkeyNum=0
    items=[]
    inspectMultiple=0
    test = 0
    monkeys=[]
    
    with open(f'{dir}/input.txt', 'r') as f:
        for i,line in enumerate(f):
            line = line.strip()
            if line.startswith('M'):
                monkeyNum = int(line.split(' ')[1].strip(':'))
            if line.startswith('S'):
                items = [int(x) for x in line.split(':')[1].split(',')]
            if line.startswith('O'):                
                inspectMultiple = line.split('=')[-1]                
            if line.startswith('T'):
                test = int(line.split(' ')[-1])
            if line.startswith('I'):
                if line.split(' ')[1].strip(':') == 'true':
                    ifTru = int(line.split(' ')[-1])
                if line.split(' ')[1].strip(':') == 'false':
                    ifFalse = int(line.split(' ')[-1])                                       
                    monkeys += [monkey(items,inspectMultiple,test,monkeyNum,ifTru,ifFalse)]
    #gave up checked reddit for part 2 , seems we need to use the Chinese Remainder Theorem 
    global MONKEY_DIVISOR_CONSTANT
    MONKEY_DIVISOR_CONSTANT =1 
    for mnk in monkeys:        
        MONKEY_DIVISOR_CONSTANT *= int(mnk.test) 
    if len(args) == 0:
        for _ in range(0,20):
            for mnk in monkeys:
                #print('monkeyNum:',mnk.monNum,mnk.items)            
                for __ in range(len(mnk.items)):
                    action = mnk.inspectItem()
                    monkeys[action[0]].recieveItem(action[1])

    #part 2
    if len(args) == 1:
        for _ in range(0,10000):
            print(_,end="\r")
            for mnk in monkeys:
                #print('monkeyNum:',mnk.monNum,mnk.items)            
                for __ in range(len(mnk.items)):
                    action = mnk.inspectItem(2)
                    monkeys[action[0]].recieveItem(action[1])

    ins = [x.inspected for x in monkeys]
    ins.sort()
    
    print(math.prod(ins[-2:]))
    print(ins)


if __name__ == '__main__':
    main()
    main(2)
