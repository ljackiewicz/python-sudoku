#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Simple Sudoku CLI Application.

Example usage:
sudoku COMMAND INPUT_GRID

sudoku show INPUT_GRID
sudoku solve INPUT_GRID
sudoku validate INPUT_GRID

Format of INPUT_GRID: nine nine-digit numbers separated by commas
530070000,600195000,098000060,800060003,400803001,700020006,060000280,000419005,000080079
"""

import fire

from sudoku.base import Sudoku, SudokuGridError


class SudokuCLI(object):
    """Simple Sudoku CLI Application."""

    @staticmethod
    def _parse_input_grid(input_grid):
        grid = []

        if ',' in input_grid:
            if input_grid.count(',') != 8:
                raise SudokuGridError("Invalid input grid format.")
        else:
            raise SudokuGridError("Invalid input grid format.")

        for i in input_grid.split(','):
            grid.append([int(j) for j in list(i)])

        return grid

    def show(self, input_grid):
        """Prints Sudoku grid in nice format."""
        grid = self._parse_input_grid(input_grid)

        Sudoku.show(grid)

    def solve(self, input_grid):
        """Solves Sudoku puzzle."""
        grid = self._parse_input_grid(input_grid)
        sudoku = Sudoku(grid)

        sudoku.solve_puzzle()

    def validate(self, input_grid):
        """Validates correctness of the grid."""
        grid = self._parse_input_grid(input_grid)
        sudoku = Sudoku(grid)

        if sudoku.validate_grid():
            print("Valid grid")
        else:
            print("Invalid grid")


def main():
    fire.Fire(SudokuCLI, name='sudoku')
