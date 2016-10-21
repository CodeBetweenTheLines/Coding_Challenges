# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 14:26:24 2016

@author: lruhlen
"""
import numpy as np
import itertools

class MazeMatrix(object):
    def __init__(self, n_cols, n_rows):
        self.connect_flag = 2
        self.room_flag = 1
        self.n_cols = n_cols
        self.n_rows = n_rows
        self.cols_per_cell = 3
        self.rows_per_cell = 3
        self.matrix = np.zeros((self.n_rows * self.rows_per_cell,
                                self.n_cols * self.cols_per_cell))
        self.room_list = list(itertools.product(range(self.n_cols),
                                                range(self.n_rows)))

        self.relative_directions = {"West": (-1,0), "East": (1,0),
                                    "South": (0,1), "North":(0,-1)}

        self.direction_pairings = {"North": "South",
                                   "South": "North",
                                   "East": "West",
                                   "West": "East"}
        self.set_centers()

    def get_cell(self, (col_loc, row_loc)):
        col_start = col_loc * self.cols_per_cell
        col_end = (col_loc + 1) * self.cols_per_cell
        row_start = row_loc * self.rows_per_cell
        row_end = (row_loc + 1) * self.rows_per_cell
        cell = self.matrix[row_start:row_end, col_start:col_end]

        return cell


    def get_neighbor_cell(self, (current_col, current_row), direction="North"):
        rel_dir = self.relative_directions[direction]
        (neighbor_col, neighbor_row) = (current_col + rel_dir[0],
                                        current_row + rel_dir[1])
        if ((not (0 <= neighbor_col < self.n_cols))
        or (not (0 <= neighbor_row < self.n_rows))):
            return None

        return self.get_cell((neighbor_col, neighbor_row))


    def set_centers(self):
        for (col, row) in self.room_list:
             self.get_cell((col, row))[1, 1] = self.room_flag
        return None


    def make_door(self, (current_col, current_row), direction="North"):
        current_cell = self.get_cell((current_col, current_row))
        rel_dir = self.relative_directions[direction]
        door_coords = [x+1 for x in rel_dir]
        current_cell[door_coords[1], door_coords[0]] = self.connect_flag

    def connect_neighbors(self, (current_col, current_row), direction="North"):
        try:
            # Connect neighbor to current cell
            nei_dir = self.relative_directions[direction]
            nei_cnxn_dir = self.direction_pairings[direction]
            nei_col = current_col + nei_dir[0]
            nei_row = current_row + nei_dir[1]
            self.make_door( (nei_col, nei_row), direction=nei_cnxn_dir)

            # Connect current cell to its neighbor
            self.make_door( (current_col, current_row), direction=direction)

        except:
            print "Can't connect this room in that direction."

        return None


    def print_maze(self):
        for row in self.matrix:
            print row
        return None


def tests():
    testMaze = MazeMatrix(3,3)
    testMaze.print_maze()
    print "\n\n"
    testMaze.connect_neighbors((0,0), direction="South")
    testMaze.print_maze()

    print "\n\n"
    testMaze.connect_neighbors((1,1), direction="West")
    testMaze.print_maze()

    print "\n\n"
    testMaze.connect_neighbors((0,0), direction="North")
    testMaze.print_maze()

    testMaze.connect_neighbors((2,0), direction="South")
    testMaze.connect_neighbors((1,1), direction="South")
    testMaze.connect_neighbors((1,2), direction="East")
    testMaze.connect_neighbors((2,2), direction="North")

    blank_char = " . "
    h_char = "---"
    v_char = " | "
    room_char = " X "

    mazePicture = []
    for r, row in enumerate(testMaze.matrix):
        temp = []
        for c, col in enumerate(row):
            if testMaze.matrix[r,c] == 0:
                temp.append( blank_char )
            elif testMaze.matrix[r,c] == 1:
                temp.append( room_char)
            elif testMaze.matrix[r,c] == 2:
                if 1. in row:
                    temp.append( h_char )
                else:
                    temp.append( v_char )
        mazePicture.append(temp)

    for row in mazePicture:
        print ''.join(row)
