'''
Created on 20 Dec. 2018

@author: E491529
'''

if __name__ == '__main__':
    pass

#===============================================================================
# Replace old with new
#===============================================================================

def replace_old_with_new(original, old, new):
    return original.replace(old, new)

print(replace_old_with_new("I am a lumberjack and I am ok!", "am", "Was"))

#===============================================================================
# Dictionary
#===============================================================================

inventory = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}
inventory["apples"]=0
print(inventory)
inventory["apples"] += 300
print(inventory, len(inventory))

del inventory["apples"]
print(inventory, len(inventory))

for key in inventory.keys() :
    print("got key ", key, "which maps to values ", inventory[key])
    
print(inventory.keys())
#===============================================================================
# Dictionary short cuts
#===============================================================================
for key in inventory:
    print("got key ", key, "which maps to values ", inventory[key])

print(list(inventory.values()))

print(list(inventory.items()))

for key, value in inventory.items():
    print("got key ", key, "which maps to values ", inventory[key])    