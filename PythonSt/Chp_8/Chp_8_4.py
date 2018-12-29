'''
Created on 29 Dec. 2018

@author: Jihan
'''

if __name__ == '__main__':
    pass

import random

def make_random_ints_no_dups(num, lower_bound, upper_bound):
    """
    Generate a list containing num random ints between
    lower_bound and upper_bound. upper_bound is an open bound.
    The result list cannot contain duplicates.
    """
    if num >= upper_bound - lower_bound :
        print("the number of random nums required must be less the number of range values to avoid duplications")
        return []
    result = []
    rng = random.Random()
    for i in range(num):
        while True:
            candidate = rng.randrange(lower_bound, upper_bound)
            if candidate not in result:
                break
        result.append(candidate)
    return result
xs = make_random_ints_no_dups(5, 1, 10000000)
print(xs)

xs = make_random_ints_no_dups(10, 1, 6)
print(xs)