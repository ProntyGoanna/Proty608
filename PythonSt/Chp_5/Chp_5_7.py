'''
Created on 20 Dec. 2018

@author: E491529
'''

if __name__ == '__main__':
    pass

this = ["I", "am", "not", "a", "crook"]
that = ["I", "am", "not", "a", "crook"]
print("Test 1: {0}".format(this is that))
that = this
print("Test 2: {0}".format(this is that))

def add_vectors(a, b):
    if len(a) != len(b) :
        print("input vectors must be the same length.")
        return None
    else :
        return[a[x]+b[x] for x in range(0, len(a))]
        
def scalar_mult(s, a):
    return [a[x]*s for x in range(0, len(a))]

def dot_product(a, b):
    sum = 0
    if len(a) != len(b) :
        print("input vectors must be the same length.")
        return None
    else :
        for x in range(0, len(a)):
            sum += a[x]*b[x] 
        return sum
        
print(add_vectors([1, 1], [1, 1]))
print(add_vectors([1, 2], [1, 4]))
print(add_vectors([1, 2, 1], [1, 4, 3]))

print(scalar_mult(5, [1, 2]))
print(scalar_mult(3, [1, 0, -1]))
print(scalar_mult(7, [3, 0, 5, 11, 2]))

print(dot_product([1, 1], [1, 1]))
print(dot_product([1, 2], [1, 4]))
print(dot_product([1, 2, 1], [1, 4, 3]))