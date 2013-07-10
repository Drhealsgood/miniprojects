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
        expected    = "".join(reversed(orig)) # Must remember reversed() returns a reversed object - iterable
        output      = self.myString.reverse(orig)
        self.assertEquals(output, expected, "{0} expected, but got {1}".format(expected, output))
        
    def test_count_vowels(self):
        """
            Count vowels will take a string and return the amount of vowels contained in the string
        """
        some_string     = "testing one two three" # 7 vowels
        no_vowels       = 7
        actual          = self.myString.count_vowels(some_string)
        self.assertEqual(actual, no_vowels, "{0} expected, but got {1}".format(no_vowels, actual))
        
    def test_is_palindrome(self):
        """
            Returns true if the passed argument is a palindrome
        """
        for phrase in ["mum mum", "racecar"]:
            self.assertTrue(self.myString.is_palindrome(phrase))
        self.assertFalse(self.myString.is_palindrome("not_a_palindrome"))
        
        
        
