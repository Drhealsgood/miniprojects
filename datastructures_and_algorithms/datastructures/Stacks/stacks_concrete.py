import abc
from stacks_interface import Stack

class RegisteredStack(Stack):

    def __init__(self):
        """
        initialise a stack of size zero
        """
        self.init()
        
    def init(self):
        """
        Makes the stack empty - initialises the stack
        """
        self.__stack = []

    def empty(self):
        """
        returns true if the stack is empty
        """
        return self.__stack == []

    def push(self, *args):
        """
        adds the object arg to the stack
        """
        for arg in args:
            self.__stack.append(arg)

    def pop(self):
        """
        Removes and returns the most recently added object from the stack
        """
        popped_object   = self.__stack[-1]
        self.__stack    = self.__stack[:-1]
        return popped_object

    def top(self):
        """
        returns the item most recently added to the stack, but does not remove it
        """
        return self.__stack[-1]
    
    def __str__(self):
        return str(self.__stack)
    
    def __len__(self):
        return len(self.__stack)
    
