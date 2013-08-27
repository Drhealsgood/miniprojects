'''
Created on 28/08/2013

@author: luke
'''
import re
import pprint
import urllib.request

SOURCE = 'http://time.is/'

def read_data():
    return str(urllib.request.urlopen(SOURCE).read())

def get_data(pattern,text):
    return re.findall(pattern,text)

def execute():
    patterns = map(re.compile,[r'<title>(.*)</title>',r'<div id="twd">(\d\d:\d\d:\d\d)*'])
    data = read_data()
    out = ""
    for pattern in patterns:
        out = out + "\n" + "".join(get_data(pattern,data))
    return out

if __name__ == '__main__':
    print(execute())