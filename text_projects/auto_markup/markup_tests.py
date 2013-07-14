'''
Created on 15/07/2013

@author: luke
'''
import unittest
from markup import *

class TestParser(unittest.TestCase):


    def setUp(self):
        self.x = Parser(Handler())


    def tearDown(self):
        pass


    def testInit(self):
        """
        A parser should have a handler, a list of rules, and a list of filters


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()