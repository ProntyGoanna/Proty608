'''
Created on 17 Dec. 2018

@author: E491529
'''

if __name__ == '__main__':
    pass

n = 1027371

while n != 1:
    print(n, end=",  ")
    if n % 2 == 0 :
        n = n // 2
    else:
        n = n * 3 + 1
        
print(n, end=".\n")