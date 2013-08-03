'''
Created on 3/08/2013

@author: luke
'''

class Library(object):
    pass

class Book(object):
    
    def __init__(self,title,isbn,author,genre):
        self._title     = title
        if len(isbn)!= 13:
            raise AttributeError
        self._isbn      = isbn
        self._author    = author
        self._genre     = genre
        
        
if __name__ == '__main__':
    pass