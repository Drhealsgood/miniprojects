'''
Created on 15/07/2013

@author: luke
'''
import re

class Utils():
    
    def getBlocks(self,text):
        """
        we want to read the text in line at a time so we 
        can apply our rules and stuff
        """
        def blocks():
            block   = []
            for line in open(text,'r').readlines():
                if line.strip():
                    block.append(line)
                elif block:
                    yield ''.join(block).strip()
                    block   = []
        return list(blocks())

class Handler():
    def callback(self,prefix,name,*args):
        # call back method pass with args
        method      = getattr(self,prefix+name,None) # find method
        try:    return method(*args)
        # if we fail just return None
        except: return None
        
    def start(self, name):
        """
        start rules
        start simply calls the method start_name
        where name is the param passed
        """
        return self.callback('start_',name)
    
    def end(self,name):
        """
        end rules
        end simply calls the method end_name
        where name is the param passed
        """
        return self.callback('end', name)
    
    def sub(self,name):
        """
        substitution rules
        """
        def substitution(match):
            result  = self.callback('sub_',name,match)
            if result is None: 
                result = match.group(0)
            return result
        return substitution
    

class Parser(object):
    '''
    classdocs
    '''


    def __init__(self,handler):
        '''
        Constructor
        @param handler: which renderer to use
        rules and filters handles layout while filters
        handle detection of strings such as emphasis/mail
        '''
        self.handler    = handler
        self.rules      = []
        self.filters    = []
        
    @property
    def handler(self):
        return self.handler
    
    @property
    def rules(self):
        return self.rules
    
    def add_rule(self, rule):
        self.rules.append(rule)
    
    @property
    def filters(self):
        return self.filters
    
    def add_filter(self, pattern, name):
        """
        appends a filter function to filters
        @param pattern: pattern to find, eg r'\8(.+?)\*
        @param name:    name of the pattern
        """
        def filter(block,handler):
            """
            @param block: the block of text we are working with
            @param handler: renderer
            """
            return re.sub(pattern,handler.sub(name),block)
        self.filters.append(filter)
        
    def parse(self,content):
        """
        @return: a string representation of the resultant from parsing content through 
        self.handler
        """
        def parse_help():
            # apply starting document rule
            yield self.handler.start("document")
        
        return "".join([x for x in self.parse_help(content) if isinstance(x,str)])
    
if __name__ == "__main__":
    x   = Utils
    gb  = x.getBlocks
    for i in gb("../string_editing.py","../string_editing.py"):
        print(i)