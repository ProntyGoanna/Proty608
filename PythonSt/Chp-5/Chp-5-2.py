'''
Created on 18 Dec. 2018

@author: E491529
'''
from builtins import reversed

if __name__ == '__main__':
    pass



import string

def remove_punctuation(phrase):
    phrase_sans_punct = ""
    for letter in phrase:
        if letter not in string.punctuation:
            phrase_sans_punct += letter
    return phrase_sans_punct


my_story = """
Pythons are constrictors, which means that they will 'squeeze' the life
out of their prey. They coil themselves around their prey and with
each breath the creature takes the snake will squeeze a little tighter
until they stop breathing completely. Once the heart stops the prey
is swallowed whole. The entire animal is digested in the snake's
stomach except for fur or feathers. What do you think happens to the fur,
feathers, beaks, and eggshells? The 'extra stuff' gets passed out as ---
you guessed it --- snake POOP! """

words = remove_punctuation(my_story).split()
print(words)

age = 10
phase = "I am a lumberjack {0}, and I am {1}.".format("Jihan", "Fine", age)
print(phase)



def isPalindrome(inputString):
    return list(inputString) == list(reversed(inputString))

for word in words:
    print("Word {0} in words is a {1} palindrome.".format(word, isPalindrome(word)))


while True:
    tempString = input("Please input a string to check: ")
    if tempString == "-1" : break
    print(isPalindrome(tempString))