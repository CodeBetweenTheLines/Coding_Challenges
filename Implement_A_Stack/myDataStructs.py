# -*- coding: utf-8 -*-
import copy

class MyStack(object):
    """My stack implementation"""

    def __init__(self):
        self.__contents = ()


    def empty(self):
        return len(self.__contents) == 0


    def push(self, val):
        self.__contents = (val, self.__contents)


    def pop(self):
        try:
            val = self.__contents[0]
            self.__contents = self.__contents[1]
            return val
        except:
            return None


    def peek(self):
        try:
            return self.__contents[0]
        except:
            return None


    def search(self, match_val):
        current_loc = 0
        match_loc = -1
        val = None
        starting_state = copy.deepcopy(self.__contents)

        while not self.empty():
            current_loc += 1
            val = self.pop()

            if val == match_val:
                match_loc = current_loc
                break

        self.__contents = starting_state
        return match_loc


    def size(self):
        starting_state = copy.deepcopy(self.__contents)
        return_val = 0

        while not self.empty():
            return_val +=1
            self.pop()

        self.__contents = starting_state
        return return_val


class MyQueue(object):
    """My queue implementation"""

    def __init__(self):
        self.__main_stack = MyStack()
        self.__reserve_stack = MyStack()


    def empty(self):
        return self.__main_stack.empty() and self.__reserve_stack.empty()


    def enqueue(self, val):
        self.__main_stack.push(val)


    def dequeue(self):
        while not self.__main_stack.empty():
            self.__reserve_stack.push(self.__main_stack.pop())

        return_val = self.__reserve_stack.pop()

        while not self.__reserve_stack.empty():
            self.__main_stack.push(self.__reserve_stack.pop())

        return return_val


    def size(self):
        return self.__main_stack.size()
