'''
Created on 10/07/2013

@author: luke
'''
import unittest
from string_editting import *

class StringEditingTests(unittest.TestCase):
    """
    StringEditing will contain a bunch of methods to edit
    and play with strings
    """
    def setUp(self):
        self.myString = MyString()
    
    def test_reverse(self):
        """
        Reverse a string takes a string as an input
        and returns the string reversed
        """
        orig        = "Hello World!"
        expected    = "".join(reversed(orig))
        output      = self.myString.reverse(orig)
        self.assertEquals(output, expected, "{0} expected, but got {1}".format(expected, output))
