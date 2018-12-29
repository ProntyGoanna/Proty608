'''
Created on 26 Dec. 2018

@author: Jihan
'''

if __name__ == '__main__':
    pass
#===============================================================================
# Read an URL and print lines that contains the word - abc to a file called abc.txt
#===============================================================================

import requests

url = "https://www.abc.net.au/news/2018-12-26/amazon-dominate-retail-within-years-slow-start/10667884?section=business"
#url = "https://en.wikipedia.org/wiki/Snake"
response = requests.get(url)
cnt = 0
with open("C:\\Users\\Jihan\\abc.txt", "w") as output_file:
    for line in response:
        string_line = str(line).lower()
        if "abc" in  string_line:
            output_file.write(string_line)
            cnt += 1
            
print("there are {0} lines that contain 'abc'.".format(cnt))            