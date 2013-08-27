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
        if other == None:
            return False
        return self._data == other.data
        
class LinkedList(object):     
    
    def __init__(self, node=None):   
        self._first = node
    
    def __repr__(self):
        out = '{0}'.format(self.__class__.__name__)
        temp = self._first
        prev = None
        while temp.next != None:
            out = '{out}, {node}({data},{prev})'.format(out=out, node=Node.__class__.__name__,
                                                       data=temp.data, prev=prev)
            prev = temp
            temp = temp.next
        return out
    
    @property
    def first(self):
        return self._first
    
    def insert(self,node,ref_node=None):
        if ref_node==None:
            if self._first==None:
                # node is first in list
                self._first = node
                return True
            temp = self._first
            while temp.next != None:
                temp = temp.next
            # now at end of list
            temp.next = node
            return True
        # otherwise append to ref_node
        if ref_node.next != None:
            node.next = ref_node.next.next
        ref_node.next = node
        return True
    
    def delete(self, node):
        node.next = node.next.next
        
    def walk_through(self):
        temp = self._first
        yield temp
        while temp.next != None:
            yield temp.next
            temp = temp.next
            
    
#new = Node(data=data,next=pos.next)
#        pos.next = new

if __name__ == '__main__':
    ll = LinkedList()
    nodes = [Node(data=bin(i)) for i in range(15)]
    for node in nodes:
        ll.insert(node)
    print(list(ll.walk_through()))