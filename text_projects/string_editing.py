'''
Created on 10/07/2013

@author: luke
'''

class MyString():
    
    def reverse(self, to_rev):
        """
            Input:     sequence of anything
            output:    sequence reversed 
        """
        return to_rev[::-1]
    
    def count_vowels(self, string):
        """
            Input:     a string
            output:    No. of vowels or 0
        """
        vowels      = "aeiou"
        return len([char for char in string if char in vowels])
    
    
    

if __name__ == '__main__':
    pass