'''
Created on 12/07/2013

@author: luke
'''
from abc import *

class Entity(metaclass=ABCMeta):
    
    @abstractproperty
    def id_number(self):
        return 0

class Product(Entity):
    '''
    classdocs
    '''
    id      = 0


    def __init__(self):
        '''
        Constructor
        '''
        self._id    = Product.id
        Product.id  = Product.id + 1
    
    @property
    def id_number(self):
        return self._id
    
class Inventory(Entity):
    id      = 0
    
    def __init__(self):
        self._id        = Inventory.id
        Inventory.id    = Inventory.id + 1
        
    @property
    def id_number(self):
        return self._id
    
class ObjFactory(metaclass=ABCMeta):
    
    @abstractmethod
    def get_object(self):
        return 0
    
class InventoryFactory(ObjFactory):
    
    def get_object(self, amt=1):
        for i in range(amt):
            yield Inventory()

class ProductFactory(ObjFactory):
    
    def get_object(self, amt=1):
        for i in range(amt):
            yield Product()