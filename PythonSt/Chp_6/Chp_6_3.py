'''
Created on 26 Dec. 2018

@author: Jihan
'''

if __name__ == '__main__':
    pass
import urllib.request

url = "https://www.abc.net.au/news/2018-12-26/amazon-dominate-retail-within-years-slow-start/10667884?section=business"
destination_filename = "C:\\Users\\Jihan\\abc-new-amazon.txt"

urllib.request.urlretrieve(url, destination_filename)
