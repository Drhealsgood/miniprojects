'''
Created on 16/07/2013

@author: luke
'''
"""
Fuck I'm a retard, this was resumably because I was attempting to set the method handler/rules/filters
when they have no set property. /facepalm
"""
class Parser(object):
    
    def __init__(self,handler):
        '''
        Constructor
        @param handler: which renderer to use
        rules and filters handles layout while filters
        handle detection of strings such as emphasis/mail
        '''
        self.__handler   = handler
        self.__rules     = []
        self.__filters   = []
        
    @property
    def handler(self):
        return self.__handler
    
    @property
    def rules(self):
        return self.__rules
    
    def add_rule(self, rule):
        self.__rules.append(rule)
    
    @property
    def filters(self):
        return self._filters
        
class Handler(object):
    
    def callback(self,prefix,name,*args):
        # call back method pass with args
        method      = getattr(self,prefix+name,None) # find method
        try:    return method(*args)
        # if we fail just return None
        except: return None
        
    def start(self, name):
        return self.callback('start_',name)
    
    def end(self,name):
        return self.callback('end', name)
    
    def sub(self,name):
        def substitution(match):
            result  = self.callback('sub_',name,match)
            if result is None: 
                result = match.group(0)
            return result
        return substitution
    
class Renderer(Handler):
        def some_method(self):
            return '12345\n'


    

if __name__ == '__main__':
    y       = Renderer()
    x       = Parser(y)
    