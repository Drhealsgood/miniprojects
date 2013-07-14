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
    
    def find_in_iter(self,some_iter):
        """
        just an examplke for someone.
        """
        if isinstance(some_iter,str):
            cond    = lambda sequence, string: [char for char in string if char in sequence] 
            vowels  = ("a,e,i,o,u")
            return [word for word in some_iter.lower().split(" ") if len(cond(vowels,word)) > 1]
        elif isinstance(some_iter[0],int):
            return [num for num in some_iter if num > 5]
            
    
    

if __name__ == '__main__':
    x       = MyString()
    word    = x.find_in_iter("a barbie vanquished the knights of the round table by hitting them in the face")
    num     = x.find_in_iter(range(10))
    print(word, '\n', num)