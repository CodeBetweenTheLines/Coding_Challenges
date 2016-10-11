# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import copy

class myStack(object):
    'My stack implementation'
    def __init__(self):
        self.contents = ()


    def empty(self):
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
        current_loc = 0
        match_loc = -1
        val = None
        starting_state = copy.deepcopy(self.contents)

        while True:
            if self.empty():
                break

            current_loc += 1
            val = self.pop()

            if val == match_val:
                match_loc = current_loc
                break

        self.contents = starting_state

        return match_loc