# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 16:37:47 2016

@author: lruhlen
"""
import itertools

class Room(object):
    """Rooms are the atomic units of a maze"""
    def __init__(self, col_loc, row_loc):
        self.col_loc = col_loc
        self.row_loc = row_loc
        self.is_exit_loc = False
        self.is_start_loc = False
        self.neighbors = dict()
        self.contents = dict()

    def __connect_to_neighbor__(self, direction, neighbor_col_loc,
                                neighbor_row_loc):
        self.neighbors[direction] = {"col_loc": neighbor_col_loc,
                                     "row_loc" : neighbor_row_loc}
        return None


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
    def __init__(self, n_rows, n_cols, start_loc=None, exit_loc=None):
        self.n_cols = n_cols
        self.n_rows = n_rows
        self.start_loc = start_loc
        self.exit_loc = exit_loc
        self.rooms_container = self.__make_rooms_container__()

    def __make_rooms_container__(self):
        room_coords = list(itertools.product(range(self.n_cols),
                                             range(self.n_rows)))
        all_rooms = {x : Room(col_loc=x[0], row_loc=x[1]) for x in room_coords}

        return all_rooms

    def __connect_rooms(self):
        for room in self.rooms_container:
            room_cnxns = self.__generate_connections(room)
            for cnxn in room_cnxns:
                room.__connect_to_neighbor__(cnxn["direction"],
                                             cnxn["col_loc"],
                                             cnxn["row_loc"])
            ## Need some way to make this a 2-way connection...
            ## Also need to run __connect_to_neighbor__ on the neighbor!

    def __generate_connections(self, room):
        return "placeholder for now"