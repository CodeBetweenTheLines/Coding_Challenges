# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class myStack(object):
    'My stack implementation'
    def __init__(self):
        self.contents = ()
        
    
    def __is_empty__(self):
        if len(self.contents):
            return False
        else:
            return True

    
    def push(self, val):
        self.contents = (val, self.contents)
        
        
    def pop(self):
        try:
            val = self.contents[0]
            self.contents = self.contents[1]
            return val
        except:
            return None

            
    def peek(self):
        val = self.pop()
        self.push(val)
        return val

        
    def search(self, match_val):
        loc = 0
        val = None
        print loc, self.contents
        
        while True:
            if self.__is_empty__():
                return -1
            
            loc += 1
            val = self.pop()
            
            if val == match_val:
                return loc
            
        return -1