'''
Created on 18 Dec. 2018

@author: E491529
'''

if __name__ == '__main__':
    pass

out_string = "Hello World"
new_string = out_string.swapcase()
print(new_string)
print(list(enumerate(new_string)))
print(len(new_string))
print(new_string[len(new_string)-1])

print(new_string[-2])

for letter in new_string :
    print(letter, end=" ")
    
friends = ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]
print(friends[4:], friends[:-3], end=", ")
print("\n")

def find(haystack, needle, start=0):
    for index,letter in enumerate(haystack[start:]):
        print(index, letter, needle)
        if letter == needle:
            return index + start
    return -1
    
print(find(friends, "Thandi", -2))