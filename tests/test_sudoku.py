#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest

from sudoku.base import Sudoku


class TestSudoku(unittest.TestCase):

    def setUp(self) -> None:
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

        self.sudoku = Sudoku(grid)

    def test_get_row_returns_correct_row(self):
        self.assertTrue(self.sudoku.get_row(1) == [5, 3, 0, 0, 7, 0, 0, 0, 0])
        self.assertTrue(self.sudoku.get_row(2) == [6, 0, 0, 1, 9, 5, 0, 0, 0])
        self.assertTrue(self.sudoku.get_row(3) == [0, 9, 8, 0, 0, 0, 0, 6, 0])
        self.assertTrue(self.sudoku.get_row(4) == [8, 0, 0, 0, 6, 0, 0, 0, 3])
        self.assertTrue(self.sudoku.get_row(5) == [4, 0, 0, 8, 0, 3, 0, 0, 1])
        self.assertTrue(self.sudoku.get_row(6) == [7, 0, 0, 0, 2, 0, 0, 0, 6])
        self.assertTrue(self.sudoku.get_row(7) == [0, 6, 0, 0, 0, 0, 2, 8, 0])
        self.assertTrue(self.sudoku.get_row(8) == [0, 0, 0, 4, 1, 9, 0, 0, 5])
        self.assertTrue(self.sudoku.get_row(9) == [0, 0, 0, 0, 8, 0, 0, 7, 9])

    def test_get_row_raise_Exception_while_wrong_parameter_value(self):
        with self.assertRaises(Exception):
            self.sudoku.get_row(-5)

        with self.assertRaises(Exception):
            self.sudoku.get_row(0)

        with self.assertRaises(Exception):
            self.sudoku.get_row(10)

    def test_get_row_raise_TypeError_while_wrong_parameter_type(self):
        with self.assertRaises(TypeError):
            self.sudoku.get_row([1, 2, 3])

        with self.assertRaises(TypeError):
            self.sudoku.get_row('r')

        with self.assertRaises(TypeError):
            self.sudoku.get_row("row")

    def test_get_column_returns_correct_column(self):
        self.assertTrue(self.sudoku.get_column(1) == [5, 6, 0, 8, 4, 7, 0, 0, 0])
        self.assertTrue(self.sudoku.get_column(2) == [3, 0, 9, 0, 0, 0, 6, 0, 0])
        self.assertTrue(self.sudoku.get_column(3) == [0, 0, 8, 0, 0, 0, 0, 0, 0])
        self.assertTrue(self.sudoku.get_column(4) == [0, 1, 0, 0, 8, 0, 0, 4, 0])
        self.assertTrue(self.sudoku.get_column(5) == [7, 9, 0, 6, 0, 2, 0, 1, 8])
        self.assertTrue(self.sudoku.get_column(6) == [0, 5, 0, 0, 3, 0, 0, 9, 0])
        self.assertTrue(self.sudoku.get_column(7) == [0, 0, 0, 0, 0, 0, 2, 0, 0])
        self.assertTrue(self.sudoku.get_column(8) == [0, 0, 6, 0, 0, 0, 8, 0, 7])
        self.assertTrue(self.sudoku.get_column(9) == [0, 0, 0, 3, 1, 6, 0, 5, 9])

    def test_get_column_raise_Exception_while_wrong_parameter_value(self):
        with self.assertRaises(Exception):
            self.sudoku.get_column(-5)

        with self.assertRaises(Exception):
            self.sudoku.get_column(0)

        with self.assertRaises(Exception):
            self.sudoku.get_column(10)

    def test_get_column_raise_TypeError_while_wrong_parameter_type(self):
        with self.assertRaises(TypeError):
            self.sudoku.get_column([1, 2, 3])

        with self.assertRaises(TypeError):
            self.sudoku.get_column('c')

        with self.assertRaises(TypeError):
            self.sudoku.get_column("column")

    def test_get_box_returns_correct_box(self):
        self.assertTrue(self.sudoku.get_box(1) == [5, 3, 0, 6, 0, 0, 0, 9, 8])
        self.assertTrue(self.sudoku.get_box(2) == [0, 7, 0, 1, 9, 5, 0, 0, 0])
        self.assertTrue(self.sudoku.get_box(3) == [0, 0, 0, 0, 0, 0, 0, 6, 0])
        self.assertTrue(self.sudoku.get_box(4) == [8, 0, 0, 4, 0, 0, 7, 0, 0])
        self.assertTrue(self.sudoku.get_box(5) == [0, 6, 0, 8, 0, 3, 0, 2, 0])
        self.assertTrue(self.sudoku.get_box(6) == [0, 0, 3, 0, 0, 1, 0, 0, 6])
        self.assertTrue(self.sudoku.get_box(7) == [0, 6, 0, 0, 0, 0, 0, 0, 0])
        self.assertTrue(self.sudoku.get_box(8) == [0, 0, 0, 4, 1, 9, 0, 8, 0])
        self.assertTrue(self.sudoku.get_box(9) == [2, 8, 0, 0, 0, 5, 0, 7, 9])

    def test_get_box_raise_Exception_while_wrong_parameter_value(self):
        with self.assertRaises(Exception):
            self.sudoku.get_box(-5)

        with self.assertRaises(Exception):
            self.sudoku.get_box(0)

        with self.assertRaises(Exception):
            self.sudoku.get_box(10)

    def test_get_box_raise_TypeError_while_wrong_parameter_type(self):
        with self.assertRaises(TypeError):
            self.sudoku.get_box([1, 2, 3])

        with self.assertRaises(TypeError):
            self.sudoku.get_box('b')

        with self.assertRaises(TypeError):
            self.sudoku.get_box("box")

    def test_validate_grid_works_correctly_for_valid_grid(self):
        self.assertTrue(self.sudoku.validate_grid())

    def test_validate_grid_invalid_for_empty_grid(self):
        sudoku = Sudoku([])

        self.assertFalse(sudoku.validate_grid())

    def test_validate_grid_invalid_for_wrong_grid_type(self):
        sudoku = Sudoku("sudoku")

        self.assertFalse(sudoku.validate_grid())

    def test_validate_grid_invalid_for_wrong_grid_length(self):
        grid = [
            [5, 3, 0,   0, 7, 0,   0, 0, 0],
            [6, 0, 0,   1, 9, 5,   0, 0, 0],
            [0, 9, 8,   0, 0, 0,   0, 6, 0],
        ]

        sudoku = Sudoku(grid)

        self.assertFalse(sudoku.validate_grid())

    def test_validate_grid_invalid_for_wrong_digits_type(self):
        grid = self.sudoku.grid
        grid[0] = [5, 6, 0,   8, '4', 7,   0, 0, 0]

        sudoku = Sudoku(grid)

        self.assertFalse(sudoku.validate_grid())

    def test_validate_grid_invalid_for_wrong_digits_range(self):
        grid = self.sudoku.grid
        grid[0] = [5, 6, 0,   8, 4, 10,   0, 0, 0]

        sudoku = Sudoku(grid)

        self.assertFalse(sudoku.validate_grid())

    def test_validate_grid_invalid_while_duplicate_in_row(self):
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

        sudoku = Sudoku(grid)

        self.assertFalse(sudoku.validate_grid())

    def test_validate_grid_invalid_while_duplicate_in_column(self):
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

        sudoku = Sudoku(grid)

        self.assertFalse(sudoku.validate_grid())

    def test_validate_grid_invalid_while_duplicate_in_box(self):
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

        sudoku = Sudoku(grid)

        self.assertFalse(sudoku.validate_grid())

    def test_possible_in_row(self):
        self.assertTrue(self.sudoku._possible(7, 2, 2))
        self.assertFalse(self.sudoku._possible(7, 2, 1))

    def test_possible_in_column(self):
        self.assertTrue(self.sudoku._possible(1, 6, 3))
        self.assertFalse(self.sudoku._possible(1, 6, 2))

    def test_possible_in_box(self):
        self.assertTrue(self.sudoku._possible(3, 5, 7))
        self.assertFalse(self.sudoku._possible(3, 5, 2))
