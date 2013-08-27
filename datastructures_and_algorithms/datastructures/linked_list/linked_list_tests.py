'''
Created on 27/08/2013

@author: luke
'''
import unittest
from linked_list import Node


class TestNode(unittest.TestCase):
    """
    A node represents a segment in the linked list. It has a data field: get and setable
    to represent the data it holds and a next field that references the next: get and setable
    node in the list. 
    """

    def setUp(self):
        pass


    def tearDown(self):
        pass


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


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()