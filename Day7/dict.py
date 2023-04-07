# Playground

nested_dict = {
    'a': {
        'x': 1,
        'y': {'j':5}
    },
    'b': {
        'z': {
            'p': 3,
            'q': 4
        }
    }
}
nested_dict['bla']=nested_dict['bla']+5

def find_parent_node(nested_dict, target_key, parent_path=None):
    if parent_path is None:
        parent_path = []
    print('launched')
    for key, value in nested_dict.items():
        if isinstance(value, dict) and target_key in value:
            return parent_path + [key]
        if isinstance(value, dict):
            parent_node_path = find_parent_node(value, target_key, parent_path=parent_path + [key])
            if parent_node_path is not None:
                return parent_node_path
    return None
target_key = 'p'
parent_key = find_parent_node(nested_dict, target_key)
print(parent_key)
# Access the value of the parent node using the parent key
if parent_key is not None:
    parent_node_value = nested_dict[parent_key]

    # Assign the value of the parent node to another object
    another_object = parent_node_value

    print(another_object)  # Output: {'p': 3, 'q': 4}
else:
    print("Parent key not found")