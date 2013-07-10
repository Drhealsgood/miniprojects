'''
Created on 10/07/2013

@author: luke
'''

class MyString():
    
    def reverse(self, some_seq):
        """
            Input:     Sequence
            output:    Sequence:
                         reversed version
        """
        return some_seq[::-1]
    
    def count_vowels(self, string):
        """
            @param string:   String
            @return:         Integer:
                                No. of vowels or 0
        """
        vowels      = "aeiou"
        return len([char for char in string if char in vowels])
    
    def is_palindrome(self,some_seq):
        """
            @param some_seq: sequence of anything
            @return:         Boolean:
                        palindrome check of sequence passed 
        """
        return some_seq == self.reverse(some_seq)
    
    def count_words(self,string=None,file=None):
        """
            @param string:    A string 
            @param file:      A file to be read 
        """
        word_count      = 0
        if string:
            word_count  = len(string.split())
        if file:
            with open(file) as f:
                word_count = len(f.read().split())
        return word_count
    
    
    

if __name__ == '__main__':
    pass