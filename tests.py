#!/usr/bin/python3
# -*- coding: utf-8 -*-
import unittest

from sudoku import Sudoku


class TestSudoku(unittest.TestCase):

    def setUp(self) -> None:
        self.sudoku = Sudoku(
            [
                [5, 3, 0,   0, 7, 0,   0, 0, 0],
                [6, 0, 0,   1, 9, 5,   0, 0, 0],
                [0, 9, 8,   0, 0, 0,   0, 6, 0],

                [8, 0, 0,   0, 6, 0,   0, 0, 3],
                [4, 0, 0,   8, 0, 3,   0, 0, 1],
                [7, 0, 0,   0, 2, 0,   0, 0, 6],

                [0, 6, 0,   0, 0, 0,   2, 8, 0],
                [0, 0, 0,   4, 1, 9,   0, 0, 5],
                [0, 0, 0,   0, 8, 0,   0, 7, 9],
            ]
        )

    def test_possible_in_row(self):
        """
        Tests if _possible method correctly detects a possibility to place
        specified digit in row.
        """
        self.assertTrue(self.sudoku._possible(7, 2, 2))
        self.assertFalse(self.sudoku._possible(7, 2, 1))

    def test_possible_in_column(self):
        """
        Tests if _possible method correctly detects a possibility to place
        specified digit in column.
        """
        self.assertTrue(self.sudoku._possible(1, 6, 3))
        self.assertFalse(self.sudoku._possible(1, 6, 2))

    def test_possible_in_box(self):
        """
        Tests if _possible method correctly detects a possibility to place
        specified digit in box.
        """
        self.assertTrue(self.sudoku._possible(3, 5, 7))
        self.assertFalse(self.sudoku._possible(3, 5, 2))
