#Part 1
##FAILED approach , find_parent_node cannot find exact key if there are multiple of the same name

## Need to find path to UNIQE key, we need some kind of context
# Maybe a list of keys for current dir, we add new one wit cd blabla and remvoe last one with cd ..
import os
import sys
dir = os.path.dirname(sys.argv[0])
score=0

def find_parent_node(nested_dict, target_key, parent_path=None):
    if parent_path is None:
        parent_path = []

    for key, value in nested_dict.items():
        if isinstance(value, dict) and target_key in value:
            return parent_path + [key]
        if isinstance(value, dict):
            parent_node_path = find_parent_node(value, target_key, parent_path=parent_path + [key])
            if parent_node_path is not None:
                return parent_node_path
    return None


def add_sizes(nested_dict,key,size):
    parent = Null
    parent = find_parent_node(nested_dict,key)
    if parent:
        curr = my_object
        for key in parent:
            curr=curr[key]
            if 'size' not in curr:
                curr['size']=size
            else:
                curr['size']+=size

def getValues(nested_dict):
    sum=0
    for key,value in nested_dict.items():        
        if isinstance(value,dict):
            if 'size' in value:
                if value['size'] <= 100000:
                    sum = value['size']
            sum += getValues(value)
    return sum


my_object = {}
current = my_object

with open(f'{dir}/input.txt','r') as f:
    for i,line in enumerate(f):
        if line[0:4] == '$ cd':
            Null,command,destination = line.strip().split(' ')
            if destination == '..':
                parent = find_parent_node(my_object,lastKey)
                current = my_object
                try:
                    for key in parent:
                        current=current[key]
                        lastKey=key
                except:
                    print('Opps',i)
                continue            
            current[destination]={}
            current = current[destination]
            lastKey = destination
        if line[0].isdigit():
            if 'size' not in current:
                current['size']=int(line.split(' ')[0])
                try:
                    add_sizes(my_object,lastKey,int(line.split(' ')[0]))
                except:
                    print(line)
                    quit()                    
            else:
                current['size']+=int(line.split(' ')[0])
                add_sizes(my_object,lastKey,int(line.split(' ')[0]))
print(my_object)
        
my_object['/']['size']



print(getValues(my_object))