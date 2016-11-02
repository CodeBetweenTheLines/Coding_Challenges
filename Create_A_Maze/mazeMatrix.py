# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 14:26:24 2016

@author: lruhlen
"""
import numpy as np
import itertools

class MazeMatrix(object):
    def __init__(self, n_cols, n_rows):
        self.connect_flag = 1
        self.n_cols = n_cols
        self.n_rows = n_rows
        self.cols_per_cell = 3
        self.rows_per_cell = 3
        self.matrix = np.zeros((self.n_rows * self.rows_per_cell,
                                self.n_cols * self.cols_per_cell))
        self.room_list = list(itertools.product(range(self.n_cols),
                                                range(self.n_rows)))
        self.relative_directions = {"North": (0,-1), "South": (0,1),
                                    "East": (1,0), "West":(-1,0)}
        self.set_centers()

    def get_cell(self, col_loc, row_loc):
        col_start = col_loc * self.cols_per_cell
        col_end = (col_loc + 1) * self.cols_per_cell
        row_start = row_loc * self.rows_per_cell
        row_end = (row_loc + 1) * self.rows_per_cell
        cell = self.matrix[row_start:row_end, col_start:col_end]

        return cell


    def get_neighbor_cell(self, (current_col, current_row), direction=None):
        rel_dir = self.relative_directions[direction]
        (neighbor_col, neighbor_row) = (current_col + rel_dir[0],
                                        current_row + rel_dir[1])
        if ((not (0 <= neighbor_col < self.n_cols))
        or (not (0 <= neighbor_row < self.n_rows))):
            return None

        return self.get_cell(neighbor_col, neighbor_row)


    def set_centers(self):
        for (col, row) in self.room_list:
             self.get_cell(col, row)[1, 1] = self.connect_flag
        return None


    def connect_cells(self, current_col, current_row, direction=None):
        neighbor_cell = self.get_neighbor_cell((current_col, current_row),
                                               direction=direction)
        if neighbor_cell and direction:
            connect_current_to_neighbor()
            connect_neighbor_to_current()
            

    def connect_cell_to_neighbor(self, (current_col, current_row), 
                                 direction=None):
        
        neighbor_loc = 
        

    def print_maze(self):
        for row in self.matrix:
            print row
        return None
