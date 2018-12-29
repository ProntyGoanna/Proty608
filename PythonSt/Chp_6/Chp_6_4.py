'''
Created on 26 Dec. 2018

@author: Jihan
'''

if __name__ == '__main__':
    pass
import requests

url = "https://www.abc.net.au/news/2018-12-26/amazon-dominate-retail-within-years-slow-start/10667884?section=business"
#url = "https://en.wikipedia.org/wiki/Snake"
response = requests.get(url)
counter = 0
for line in response:
    print(line)
    counter += 1
print(counter)    