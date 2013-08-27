'''
Created on 27/08/2013

@author: luke
'''

class Node(object):
    
    def __init__(self,data,next=None):
        self._data = data
        self._next = next
    
    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self,new):
        self._data = new
        
    @property
    def next(self):
        return self._next
    
    @next.setter
    def next(self,new):
        self._next = new
        
    def __repr__(self):
        return '{0}(data="{1}")'.format(self.__class__.__name__, self._data)
    
    def __eq__(self,other):
        return self._data == other.data and self._next == other.next
        
class LinkedList(object):        
    
    pass
#new = Node(data=data,next=pos.next)
#        pos.next = new

if __name__ == '__main__':
    pass