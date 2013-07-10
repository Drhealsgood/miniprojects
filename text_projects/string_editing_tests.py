'''
Created on 10/07/2013

@author: luke
'''
import unittest
from string_editing import *

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
        tests       = ["Hello World!", (1,2,3,4), [9,8,7,6,5,4,3,2,1]]
        for i in tests:
            orig        = i
            obj_reversed= reversed(orig)
            # I shouldn't have done this maybe. Or I should be able to do it neater - use map
            # or perhaps I check via sequence
            if isinstance(i, str):
                expected    = "".join(obj_reversed) 
            if isinstance(i, list):
                expected    = list(obj_reversed)
            if isinstance(i, tuple):
                expected    = tuple(obj_reversed)
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
        
    def test_count_words_string(self): 
        """
        Counts the number of individual words in a string. 
        It is possible to read these strings in from a text file
        and generate a report
        count_words will take any of three inputs: 
        None will return 0
        string="some_string"     will return the length of the string
        file="some_file"         will return the length of th string in the file
        
        """
        string      = "This is a string of some length that I will work out by using a function"
        words       = string.split()
        word_count  = len(words)
        self.assertEqual(self.myString.count_words(string=string), word_count) # check string word count
        file        = "test_resources/test_file.txt" 
        with open(file) as f:
            string  = f.read()
            words   = string.split()
            word_count = len(words)
            self.assertEqual(self.myString.count_words(file=file), word_count) # check file string word count