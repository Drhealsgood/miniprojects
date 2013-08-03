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
        
    @property
    def title(self):
        return self._title
    
    @property
    def isbn(self):
        return self._isbn
    
    @property
    def author(self):
        return self._author
    
    @property
    def genre(self):
        return self._genre
        
        
if __name__ == '__main__':
    pass