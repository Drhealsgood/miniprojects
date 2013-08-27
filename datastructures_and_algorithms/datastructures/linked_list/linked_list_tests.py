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
    
    def _populate_list(self):
        for i in range(10):
            self._ll.insert(Node(i))
    
    def setUp(self):
        self._ll = LinkedList()
        
    def tearDown(self):
        del(self._ll)
    
    def testFirst(self):
        """
        First returns the first item in the Linked list.
        """
        self.assertIsNone(self._ll.first)
        self._ll.insert(Node("data"))
        self.assertEqual(self._ll.first,Node("data",next=None))
        self._ll.insert(Node("First!"),ref_node=self._ll.first)
        self.assertEqual(self._ll.first,Node("data",next=Node("First",next=None)))

    def testInsert(self):
        """
        The list inserts the given node and the given position
        if position is not given it inserts at the end of the list
        """
        for i in range(10):
            self._ll.insert(Node(data=i))
        i = 0
        temp = self._ll.first
        while temp.next != None:
            self.assertEqual(temp.data,i)
            temp = temp.next
            i += 1
        self._ll.insert(Node("data"),ref_node=self._ll.first)
        self.assertEqual(Node("data"),self._ll.first.next)
        self.assertEqual(Node(2),self._ll.first.next.next)
        
    def testDelete(self):
        """
        The list deletes the node after the node referenced by pos
        """
        self._populate_list()
        self._ll.delete(5)
        self.assertNotIn(6,[node.data for node in self._ll])
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()