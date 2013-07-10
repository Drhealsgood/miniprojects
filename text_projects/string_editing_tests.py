'''
Created on 10/07/2013

@author: luke
'''
import unittest
from string_editting import MyString

class StringEditingTests(unittest.TestCase):
    """
    StringEditing will contain a bunch of methods to edit
    and play with strings
    """
    
    def test_reverse(self):
        """
        Reverse a string takes a string as an input
        and returns the string reversed
        """
        orig        = "Hello World!"
        expected    = reversed(orig)
        output      = Mystring.reverse(orig)
        self.assertEquals(output, expected, "{0} expected, but got {1}".format(expected, output))
