'''
Created on 22 Dec. 2018

@author: Jihan
'''

import string, re
if __name__ == '__main__':
    pass

#===============================================================================
# Counting word frequency from business news articles
#===============================================================================

# Sort a dictionary of word-frequency pairs in
# order of descending frequency.

def sortFreqDict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux

def stripPunctuations(inString):
    return regex.sub('', inString)

regex = re.compile('[%s]' % re.escape(string.punctuation))
filename = "c:\\Users\\Jihan\\AliceInWonderland.txt"
wordfreq = {}

with open(filename, "r") as my_new_handle:
    for the_line in my_new_handle:
# Do something with the line we just read.
# Here we just print it.
        wordlist = stripPunctuations(the_line).split()
        for word in wordlist :
           wordfreq[word] = wordfreq.get(word, 0) + 1 

sorted_word_freq_dict = sortFreqDict(wordfreq)
for key, value in sorted_word_freq_dict :
    print(key, value, end=(" \n"))

