# -*- coding: utf-8 -*-
import copy

class MyStack(object): # PascalCase for class names
    """My stack implementation"""

    def __init__(self):
        self.__contents = () # Double underscore to make implementation details private


    def empty(self):
        return len(self.__contents) == 0 # Multiple lines just to return boolean


    def push(self, val):
        self.__contents = (val, self.__contents)


    def pop(self): # Return None or raise exception?
        try:
            val = self.__contents[0]
            self.__contents = self.__contents[1]
            return val
        except:
            return None


    def peek(self): # Return None or raise exception?
        try: # Popping and re-pushing adds unnecessary complexity, though I see where you were coming from for DRYness. Could break out the WET part as a decorator?
            return self.__contents[0]
        except:
            return None


    def search(self, match_val): # Copying is space inefficient, and iterating twice (once for the copy) is inefficient
        current_loc = 0
        match_loc = -1
        val = None
        starting_state = copy.deepcopy(self.__contents)

        while not self.empty(): # May as well just make it the loop condition
            current_loc += 1
            val = self.pop()

            if val == match_val:
                match_loc = current_loc
                break

        self.__contents = starting_state
        return match_loc


    def size(self): # Could be made more efficient. First thought is to keep a self.size counter and increment/decrement as necessary
        starting_state = copy.deepcopy(self.__contents)
        return_val = 0

        while not self.empty(): # Can't do .empty() on the tuple itself
            return_val +=1
            self.pop()

        self.__contents = starting_state # Don't forget to put the contents back
        return return_val


class MyQueue(object): # PascalCase for class names
    """My queue implementation""" # Can't peek?

    def __init__(self):
        self.__main_stack = MyStack() # Double underscore to make implementation details private
        self.__reserve_stack = MyStack() # Double underscore to make implementation details private


    def empty(self):
        return self.__main_stack.empty() and self.__reserve_stack.empty() # Storing a variable just to return it, and wrong var names


    def enqueue(self, val):
        self.__main_stack.push(val)


    def dequeue(self): # Moving everything between the two stacks every time is inefficient
        while not self.__main_stack.empty():
            self.__reserve_stack.push(self.__main_stack.pop())

        return_val = self.__reserve_stack.pop()

        while not self.__reserve_stack.empty():
            self.__main_stack.push(self.__reserve_stack.pop())

        return return_val


    def size(self):
        return self.__main_stack.size() # Storing a variable just to return it
