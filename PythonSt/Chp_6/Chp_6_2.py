'''
Created on 26 Dec. 2018

@author: Jihan
'''

if __name__ == '__main__':
    pass

with open("C:\\Users\\Jihan\\AliceInWonderland.txt", "r") as input_file:
    all_lines = input_file.readlines()

all_lines.sort()

with open("C:\\Users\\Jihan\\SortedAlice.txt", "w") as output_file:
    for line in all_lines:
        output_file.write(line)
        
        
with open("C:\\Users\\Jihan\\AliceInWonderland.txt") as f:
    content = f.read()
words = content.split()
print("There are {0} words in the file.".format(len(words)))