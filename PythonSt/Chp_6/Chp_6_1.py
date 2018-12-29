'''
Created on 25 Dec. 2018

@author: Jihan
'''

if __name__ == '__main__':
    pass

#Use a mask to multiply all values below 100 in the following list by 2:
#Repeat this until all values are above 100. (Not manually, but by looping)
#Then, select all values between 150 < a < 200.

import numpy as np

a = np.array([230, 10, 284, 39, 76])

while any(a <100): 
    a[a < 100] += 2 
    print(a)
idx = np.where((a < 200) & (a> 150))
print(a[idx])    