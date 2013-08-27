'''
Created on 12/03/2013

@author: luke
'''
import unittest
from stacks_concrete import RegisteredStack


class TestRegisteredStack(unittest.TestCase):


    def setUp(self):
        self.stack = RegisteredStack()


    def tearDown(self):
        self.stack = None


    def testInit(self):
        """
        Initialisation of a stack results in an empty stack
        """
        self.assertEqual(str(self.stack), str([]), "Init Expected empty stack")
        
    def testEmpty(self):
        """
        Empty tests whether the stack is empty.
        """
        self.assertTrue(self.stack.empty())
        self.stack.push(1)
        self.assertFalse(self.stack.empty())
        
    def testPush(self):
        """
        push(vals) adds the value(s) vals to the stack
        """
        self.stack.push(1)
        self.assertEqual(self.stack.top(), 1)
        self.stack.push(2,3,4,5)
        for i in range(5, 0, -1):
            self.assertEqual(self.stack.pop(), i)
            
    def testPop(self):
        """
        Removes and returns the most recently added object from the stack
        """
        self.stack.push(1,2,3,4,5)
        size = len(self.stack)
        for i in range(5,0,-1):
            self.assertEqual(self.stack.pop(), i)
            self.assertEqual(len(self.stack), size-1)
            size = size - 1
            
    def testTop(self):
        """
        returns the item most recently added to the stack, but does not remove it
        """
        for i in range(5):
            self.stack.push(i)
            self.assertEqual(self.stack.top(), i)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()