'''
Created on 28 Dec. 2018

@author: Jihan
'''

if __name__ == '__main__':
    pass

import random

# Create a black box object that generates random numbers
rng = random.Random()

dice_throw = rng.randrange(1,7) # Return an int, one of 1,2,3,4,5,6
delay_in_seconds = rng.random() * 5.0

print(delay_in_seconds)

random_odd = rng.randrange(1, 100, 1)

print(random_odd)


cards = list(range(52)) # Generate ints [0 .. 51]
print(cards)
#representing a pack of cards.
rng.shuffle(cards) # Shuffle the pack
print(cards)