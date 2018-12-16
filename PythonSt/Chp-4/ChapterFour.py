'''
Created on 14 Dec. 2018

@author: E491529
'''


if __name__ == '__main__':
    pass



import sys
import os

print(str(sys.path))

dir_path = os.path.dirname(os.path.realpath(__file__))
print("current working dir: {dir_path}")

#root_dir = dir_path.replace("/util", '', 1)
#print("root dir: {root_dir}")

#sys.path.insert(0, root_dir)

#print(str(sys.path))