# Given 2 arrays, create a function
# That let's user know (true/false)
# whether these arrays contain common items.

# inputs: arrays
# outputs: true/false

from collections import defaultdict

def commonItems(array1, array2):
    items = defaultdict()
    for item in array1:
        items[item] = 1
    
    for item in array2:
        if items.get(item, None):
            return True

    return False



array1 = ['a', 'b', 'c', 'x']
array2 = ['z', 'y', 'i']

array3 = ['a', 'b', 'c', 'x', 'x']
array4 = ['z', 'x', 'z', 'y']

print(commonItems(array1, array2))
print(commonItems(array3, array4))
