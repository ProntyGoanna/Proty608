'''
Created on 29 Dec. 2018

@author: Jihan
'''

if __name__ == '__main__':
    pass
import random
#===============================================================================
# pick random number without repeated numbers. However, it only works with small set.
# There is a performance issue with large sets
#===============================================================================

xs = list(range(1,13)) # Make list 1..12 (there are no duplicates)
rng = random.Random() # Make a random number generator
rng.shuffle(xs) # Shuffle the list
result = xs[:5] # Take the first five elements

print(result)