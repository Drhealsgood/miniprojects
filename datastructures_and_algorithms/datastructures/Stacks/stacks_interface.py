import abc

class Stack():
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def init(self):
        """
        Makes the stack empty - initialises the stack
        """
        return

    @abc.abstractmethod
    def empty(self):
        """
        returns true if the stack is empty
        """
        return

    @abc.abstractmethod
    def push(self, val):
        """
        adds the object val to the stack
        """
        return

    @abc.abstractmethod
    def pop(self):
        """
        Removes and returns the most recently added object from the stack
        """
        return

    @abc.abstractmethod
    def top(self):
        """
        returns the item most recently added to the stack, but does not remove it
        """
        return
