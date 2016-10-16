# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 16:37:47 2016

@author: lruhlen
"""
import itertools
import random

class Room(object):
    """Rooms are the atomic units of a maze"""
    def __init__(self, col_loc, row_loc):
        self.col_loc = col_loc
        self.row_loc = row_loc
        self.is_exit_loc = False
        self.is_start_loc = False
        self.neighbors = self.__create_neighbors_list()
        self.contents = dict()

    def __create_neighbors_list(self):
        neighbors = dict()
        neighbors["North"] = (self.col_loc, self.row_loc - 1)
        neighbors["South"] = (self.col_loc, self.row_loc + 1)
        neighbors["East"] = (self.col_loc + 1, self.row_loc)
        neighbors["West"] = (self.col_loc - 1, self.row_loc)

        return neighbors
        

    def remove_neighbor(self, direction_key):
        del self.neighbors[direction_key]
        
        return None
        
        
    # Note: need to ensure start != exit loc.
    def set_as_start_loc(self):
        self.is_start_loc = True
        self.contents = "This is the start of the maze."
    
    
    def set_as_exit_loc(self):
        self.is_exit_loc = True
        self.contents = "This is the exit!  HOORAY!  You're free"
        
 
    def display_flavor_text(self):
        """Function that prints out 'There are exits to the
        West and South...' and/or 'The room contains a sword/enemy/etc'"""
        # Probably want to split this into its own method
        if self.contents:
            print "There are THINGS in this room! They are:"
            for item in self.contents:
                print "\t+ ", item

        # Probably want to splint this into its own method
        if self.neighbors:
            print "There are doors leading to the: "
            for door in self.neighbors:
                print "\t+ ", door
        return None



class Maze(object):
    """The Maze() object coordinates groups of rooms"""
    def __init__(self, n_cols, n_rows, start_loc=None,exit_loc=None):
        self.n_cols = n_cols
        self.n_rows = n_rows
        self.start_loc = start_loc
        self.exit_loc = exit_loc
        self.rooms_container = self.__make_rooms_container__()
        self.__set_start_and_exit_locs()
        self.__validate_all_neighbors()
        

    def __make_rooms_container__(self):
        room_coords = list(itertools.product(range(self.n_cols),
                                             range(self.n_rows)))
        all_rooms = {x : Room(col_loc=x[0], row_loc=x[1]) 
                     for x in room_coords}

        return all_rooms
        
        
    def __set_start_and_exit_locs(self):
        if not self.start_loc:
            self.start_loc = (0,0)
        if not self.exit_loc:
            self.exit_loc = (self.n_cols/2, self.n_rows-1)
            
        self.get_room(self.start_loc).set_as_start_loc()     
        self.get_room(self.exit_loc).set_as_exit_loc()
        
        return None
            


    def __validate_all_neighbors(self):
        for room_key in self.rooms_container.keys():
            this_room = self.get_room(room_key)
            
            for direction_key in this_room.neighbors.keys():
                if not self.__is_room_location_allowed(this_room.neighbors[direction_key]):
                    this_room.remove_neighbor(direction_key)
        
        return None
                               
                               
    def __is_room_location_allowed(self, location):
        col_loc = location[0]
        row_loc = location[1]
        
        return ((col_loc >= 0) and (col_loc < self.n_cols) 
                and (row_loc >= 0) and (row_loc < self.n_rows))
                
    
    def _prune_paths(self):
        if not (self.start_loc and self.exit_loc):
            raise Exception("No start or exit position specified")
        
        # Start at the exit node, and move towards the start
        this_room = self.get_room(exit_loc) 
        visited_room_keys = []
                       
            
        return None
     
     
    def get_room(self, room_key):
        return self.rooms_container[room_key]
        

    def show_room(self, room_key):
        this_room = self.get_room(room_key).display_flavor_text()
        return None
        
    
# ------- Testing out how to render the maze ------
def render_room(room):
    neighbors = room.neighboors
    
    v_connect = "|"
    h_connect = "-"
    ws = " "
    cell_array = [[ws, ws, ws], [ws, ws, ws], [ws, ws, ws]]
    
    if "East" in neighbors.keys():
        cell_array[1][2] = h_connect
    if "West" in neighbors.keys():
        cell_array[1][0] = h_connect
    if "North" in neighbors.keys():
        cell_array[0][1] = v_connect
    if "South" in neighbors.keys():
        cell_array[2][1] = v_connect
        
    