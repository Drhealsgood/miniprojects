'''
Created on 15/07/2013

@author: luke

@todo: implement more rules and filters; tests.
'''
from abc import *
import re

class Utils():
    """
    """
    
    @classmethod
    def getBlocksFile(cls,text):
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
    
    @classmethod
    def getBlocksString(cls,text):
        def blocks():
            block   = []
            for line in text.split("\n"):
                if line.strip():
                    block.append(line)
                elif block:
                    yield ''.join(block)
                    block   = []
        return list(blocks())
    
    @classmethod
    def output(cls,content):
        with open('output/output.html','w') as f:
            f.write(content)
        assert(f.closed)

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
        return self.callback('end_', name)
    
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
    
class HTMLRenderer(Handler):
    
    # html document rules
    def start_document(self):
        """
        @return: basic start of HTML document
        """
        return '<html><head><title></title></head><body>'
    
    def end_document(self):
        return '</body></html>'

    # paragraph rules
    def start_paragraph(self):
        return '<p>'
    
    def end_paragraph(self):
        return '</p>'
    
    # heading rules
    def start_heading(self):
        return '<h1>'
    
    def end_heading(self):
        return '</h1>'
    
    # substitutions
    def sub_strong(self,match):
        return '<strong>{0}</strong>'.format(match.group(1))
    
    def data(self,block):
        return block
    
    
class Rule(metaclass=ABCMeta):
    """
    A rule has a condition and an action and a type.
    If the condition is met, the action will be applied.
    Each rule should have a type to explain its intention, no type means there 
    is no rule to accomplish 
    """
    def action(self, block, handler):
        """
        @return: String - block with rule applied or Boolean - NA
            Action should be the same for all rules
        """
        if self._type:
            # feed handler instructions > start > data > end for block modifications
            return ''.join([handler.start(self._type),handler.data(block),handler.end(self._type)])
        # if there is no type return False - there is no rule.
        return False
    
    @abstractmethod
    def condition(self,block):
        """
        @return: Boolean
            Check to see if block meets condition of the rule
        """
        return False
        
    def type(self):
        """
            @return: String representation of the rule type
        """
        return self._type
    
class HeadingRule(Rule):
    """
        HeadingRule condition: A block is a Heading if:    
                 it is one line (does not contain \n)
                 lte 70 characters
    """
    _type       = "heading"
    
    def condition(self,block):
        return (('\n' not in block) and (len(block)<=70))
    
class ParagraphRule(Rule):
    """
        ParagraphRule is going to be the end rule as it's
        the default rule if no others are followed up - for HTML
    """
    _type       = "paragraph"
    
    def condition(self, block):
        return True
    
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
        self._handler   = handler
        self._rules     = []
        self._filters   = []
        
    @property
    def handler(self):
        return self._handler
    
    @property
    def rules(self):
        return self._rules
    
    def add_rule(self, rule):
        self._rules.append(rule)
    
    @property
    def filters(self):
        return self._filters
    
    def add_filter(self, pattern, name):
        """
        appends a filter function to filters
        @param pattern: pattern to find, eg r'\8(.+?)\*
        @param name:    name of the pattern
        """
        def apply_filter(block,handler):
            """
            @param block: the block of text we are working with
            @param handler: renderer
            """
            return re.sub(pattern,handler.sub(name),block)
        self._filters.append(apply_filter)
        
    def parse(self,content):
        """
        @return: a string representation of the resultant from parsing content through 
        self.handler
        """
        def parse_help():
            # apply starting document rule
            yield self.handler.start("document")
            for block in Utils.getBlocksFile(content):
                # apply filters
                for filter_meth in self.filters: 
                    block   = filter_meth(block,self.handler)
                # apply rules
                for rule in self._rules:
                    if rule.condition(block): # check to see if condition applies
                        
                        action  = rule.action(block,self._handler)
                        # yield action if one exists
                        if action:
                            yield action
                        break;
            # apply end document rule    
            yield self.handler.end("document")
        
        return "".join([x for x in parse_help() if isinstance(x,str)])
    

    
if __name__ == "__main__":
    y       = HTMLRenderer()
    x       = Parser(y)
    f       = "../test_resources/markup_text.txt"
    x.add_rule(ParagraphRule())
    x.add_filter(r"\*(.+|.?)\*", 'strong')
    t       = x.parse(f)
    Utils.output(t)
    