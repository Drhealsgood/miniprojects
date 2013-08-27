'''
Created on 27/08/2013

@author: luke
'''
import unittest
from linked_list import Node, LinkedList


class TestNode(unittest.TestCase):
    """
    A node represents a segment in the linked list. It has a data field: get and setable
    to represent the data it holds and a next field that references the next: get and setable
    node in the list. 
    """
    def testData(self):
        node = Node(data="data",next=None)
        self.assertEqual(node.data,"data")
        node.data = "new_data"
        self.assertEqual(node.data,"new_data")
    
    def testNext(self):
        node = Node(data="data",next=None)
        first_node = Node(data="first",next=node)
        self.assertEqual(first_node.next,node)
        third = Node(data="third",next=None)
        node.next = third
        self.assertEqual(node.next,third)
        
class TestLinkedList(unittest.TestCase):
    
    def setUp(self):
        self._ll = LinkedList()
        
    def tearDown(self):
        del(self._ll)
    
    def testFirst(self):
        self._ll.first = Node("data",next=None)
        self.assertEqual(self._ll.first,Node("data",next=None))

    def testInsert(self):
        for i in range(10):
            self._ll.insert(Node(data=i,pos=i))
        for i,node in enumerate(self._ll):
            self.assertEqual(node.data,i)
        self._ll.insert(Node("data"),pos=1)
        self.assertEqual(Node("data"),self._ll.first.next)
        self.assertEqual(Node(2),self._ll.first.next.next)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()