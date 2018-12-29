'''
Created on 29 Dec. 2018

@author: Jihan
'''

if __name__ == '__main__':
    pass
import random

#===============================================================================
# pick up with replacement i.e. with repeat numbers
#===============================================================================
def make_random_ints(num, lower_bound, upper_bound):
    """
    Generate a list containing num random ints between lower_bound
    and upper_bound. upper_bound is an open bound.
    """
    rng = random.Random()  # Create a random number generator
    result = []
    for i in range(num):
        result.append(rng.randrange(lower_bound, upper_bound))
    return result

print(make_random_ints(5, 1, 13))



