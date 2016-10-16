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

    def size(self):
        starting_state = copy.deepcopy(self.contents)
        return_val = 0

        while not self.contents.empty():
            return_val +=1
            self.pop()

        return return_val


class myQueue(object):
    """My queue implementation"""
    def __init__(self):
        self.main_stack = myStack()
        self.reserve_stack = myStack()


    def empty(self):
        result = ( self.left_stack.empty() and self.right_stack.empty() )
        return result


    def enqueue(self, val):
        self.main_stack.push(val)


    def dequeue(self):
        while not self.main_stack.empty():
            self.reserve_stack.push(self.main_stack.pop())

        return_val = self.reserve_stack.pop()

        while not self.reserve_stack.empty():
            self.main_stack.push(self.reserve_stack.pop())

        return return_val

    def size(self):
        return_val = self.main_stack.size()
        return return_val
