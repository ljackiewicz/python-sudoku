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

    def test_get_row(self):
        """
        Tests if the get_row method works correctly.
        """
        grid = [
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

        self.assertTrue(self.sudoku.get_row(1) == grid[0])
        self.assertTrue(self.sudoku.get_row(2) == grid[1])
        self.assertTrue(self.sudoku.get_row(3) == grid[2])
        self.assertTrue(self.sudoku.get_row(4) == grid[3])
        self.assertTrue(self.sudoku.get_row(5) == grid[4])
        self.assertTrue(self.sudoku.get_row(6) == grid[5])
        self.assertTrue(self.sudoku.get_row(7) == grid[6])
        self.assertTrue(self.sudoku.get_row(8) == grid[7])
        self.assertTrue(self.sudoku.get_row(9) == grid[8])

    def test_get_row_raise_Exception(self):
        """
        Tests if get_row method raises an Exception when passed parameter out
        of desire range.
        """
        with self.assertRaises(Exception):
            self.sudoku.get_row(-5)

        with self.assertRaises(Exception):
            self.sudoku.get_row(0)

        with self.assertRaises(Exception):
            self.sudoku.get_row(10)

    def test_get_row_raise_TypeError(self):
        """
        Tests if get_row method raises TypeError if a non-integer parameter is
        passed.
        """
        with self.assertRaises(TypeError):
            self.sudoku.get_row([1, 2, 3])

        with self.assertRaises(TypeError):
            self.sudoku.get_row('c')

        with self.assertRaises(TypeError):
            self.sudoku.get_row("column")

    def test_get_column(self):
        """
        Tests if the get_column method works correctly.
        """
        transpose_grid = [
            [5, 6, 0,   8, 4, 7,   0, 0, 0],
            [3, 0, 9,   0, 0, 0,   6, 0, 0],
            [0, 0, 8,   0, 0, 0,   0, 0, 0],

            [0, 1, 0,   0, 8, 0,   0, 4, 0],
            [7, 9, 0,   6, 0, 2,   0, 1, 8],
            [0, 5, 0,   0, 3, 0,   0, 9, 0],

            [0, 0, 0,   0, 0, 0,   2, 0, 0],
            [0, 0, 6,   0, 0, 0,   8, 0, 7],
            [0, 0, 0,   3, 1, 6,   0, 5, 9],
        ]

        self.assertTrue(self.sudoku.get_column(1) == transpose_grid[0])
        self.assertTrue(self.sudoku.get_column(2) == transpose_grid[1])
        self.assertTrue(self.sudoku.get_column(3) == transpose_grid[2])
        self.assertTrue(self.sudoku.get_column(4) == transpose_grid[3])
        self.assertTrue(self.sudoku.get_column(5) == transpose_grid[4])
        self.assertTrue(self.sudoku.get_column(6) == transpose_grid[5])
        self.assertTrue(self.sudoku.get_column(7) == transpose_grid[6])
        self.assertTrue(self.sudoku.get_column(8) == transpose_grid[7])
        self.assertTrue(self.sudoku.get_column(9) == transpose_grid[8])

    def test_get_column_raise_Exception(self):
        """
        Tests if get_column method raises an Exception when passed parameter
        out of desire range.
        """
        with self.assertRaises(Exception):
            self.sudoku.get_column(-5)

        with self.assertRaises(Exception):
            self.sudoku.get_column(0)

        with self.assertRaises(Exception):
            self.sudoku.get_column(10)

    def test_get_column_raise_TypeError(self):
        """
        Tests if get_column method raises TypeError if a non-integer parameter
        is passed.
        """
        with self.assertRaises(TypeError):
            self.sudoku.get_column([1, 2, 3])

        with self.assertRaises(TypeError):
            self.sudoku.get_column('c')

        with self.assertRaises(TypeError):
            self.sudoku.get_column("column")

    def test_validate_grid_valid_grid(self):
        """
        Tests if validate_grid method returns True for a valid grid.
        """
        self.assertTrue(Sudoku.validate_grid(self.sudoku.grid))

    def test_validate_grid_empty_grid(self):
        """
        Tests if validate_grid method returns False for an empty grid (empty
        list).
        """
        self.assertFalse(Sudoku.validate_grid([]))

    def test_validate_grid_valid_grid_type(self):
        """
        Tests if validate_grid method returns False for an invalid typed grid
        (not a list).
        """
        self.assertFalse(Sudoku.validate_grid(self.sudoku))
        self.assertFalse(Sudoku.validate_grid("sudoku"))
        self.assertFalse(Sudoku.validate_grid(10))

    def test_validate_grid_valid_grid_length(self):
        """
        Tests if validate_grid method returns False for an invalid length of
        grid.
        """
        grid = [
            [5, 3, 0,   0, 7, 0,   0, 0, 0],
            [6, 0, 0,   1, 9, 5,   0, 0, 0],
            [0, 9, 8,   0, 0, 0,   0, 6, 0],
        ]

        self.assertFalse(Sudoku.validate_grid(grid))

    def test_validate_grid_valid_digits_type(self):
        """
        Tests if validate_grid method returns False for invalid digits type.
        """
        grid = self.sudoku.grid

        row = [5, 6, 0,   8, '4', 7,   0, 0, 0]
        grid[0] = row

        self.assertFalse(Sudoku.validate_grid(grid))

    def test_validate_grid_valid_digits_range(self):
        """
        Tests if validate_grid method returns False for invalid digits range
        (digits out of range from 0 to 9).
        """
        grid = self.sudoku.grid

        row = [5, 6, 0,   8, 4, 10,   0, 0, 0]
        grid[0] = row

        self.assertFalse(Sudoku.validate_grid(grid))

    def test_validate_grid_duplicate_in_row(self):
        """
        Tests if validate_grid method returns False for grid with duplicates
        in row.
        """
        grid = [
            [5, 3, 0,   3., 7, 0,   0, 0, 0],
            [6, 0, 0,   1, 9, 5,   0, 0, 0],
            [0, 9, 8,   0, 0, 0,   0, 6, 0],

            [8, 0, 0,   0, 6, 0,   0, 0, 3],
            [4, 0, 0,   8, 0, 3,   0, 0, 1],
            [7, 0, 0,   0, 2, 0,   0, 0, 6],

            [0, 6, 0,   0, 0, 0,   2, 8, 0],
            [0, 0, 0,   4, 1, 9,   0, 0, 5],
            [0, 0, 0,   0, 8, 0,   0, 7, 9],
        ]

        self.assertFalse(Sudoku.validate_grid(grid))

    def test_validate_grid_duplicate_in_column(self):
        """
        Tests if validate_grid method returns False for grid with duplicates
        in column.
        """
        grid = [
            [5, 3, 0,   0, 7, 0,   0, 0, 0],
            [6, 0, 0,   1, 9, 5,   0, 0, 0],
            [0, 9, 8,   0, 0, 0,   0, 6, 0],

            [8, 0, 0,   0, 6, 0,   0, 0, 3],
            [4, 0, 0,   8, 0, 3,   0, 0, 1],
            [7, 0, 0,   0, 2, 0,   0, 0, 6],

            [0, 6, 0,   0, 0, 0,   2, 8, 0],
            [0, 0, 0,   4, 1, 9,   0, 0, 5],
            [5., 0, 0,   0, 8, 0,   0, 7, 9],
        ]

        self.assertFalse(Sudoku.validate_grid(grid))

    def test_validate_grid_duplicate_in_box(self):
        """
        Tests if validate_grid method returns False for grid with duplicates
        in box (subgrid).
        """
        grid = [
            [5, 3, 0,   0, 7, 0,   0, 0, 0],
            [6, 0, 0,   1, 9, 5,   0, 0, 0],
            [3., 9, 8,   0, 0, 0,   0, 6, 0],

            [8, 0, 0,   0, 6, 0,   0, 0, 3],
            [4, 0, 0,   8, 0, 3,   0, 0, 1],
            [7, 0, 0,   0, 2, 0,   0, 0, 6],

            [0, 6, 0,   0, 0, 0,   2, 8, 0],
            [0, 0, 0,   4, 1, 9,   0, 0, 5],
            [0, 0, 0,   0, 8, 0,   0, 7, 9],
        ]

        self.assertFalse(Sudoku.validate_grid(grid))

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
