#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Sudoku(object):
    """Represents a Sudoku puzzle.

    Args:
        grid (list): list of nine 9-elements lists that represents sudoku grid
    """

    def __init__(self, grid: list = None) -> None:
        if grid is None:
            grid = []

        self.grid = grid

    def _possible(self, y: int, x: int, digit: int) -> bool:
        """Checks if digit can be placed in x,y position."""
        for i in range(9):
            if self.grid[y][i] == digit:
                return False

        for i in range(9):
            if self.grid[i][x] == digit:
                return False

        x0 = x - x % 3
        y0 = y - y % 3

        for i in range(3):
            for j in range(3):
                if self.grid[y0+i][x0+j] == digit:
                    return False

        return True

    def solve(self) -> None:
        """Recursively solves Sudoku puzzle."""
        for y in range(9):
            for x in range(9):
                if self.grid[y][x] == 0:
                    for digit in range(1, 10):
                        if self._possible(y, x, digit):
                            self.grid[y][x] = digit
                            self.solve()
                            self.grid[y][x] = 0
                    return

        self.show()

    def show(self) -> None:
        """Prints sudoku grid in nice format."""
        grid = ""

        for y in range(9):
            for x in range(9):
                spacer = "  " if (x+1) % 3 else "  " * 2
                grid += str(self.grid[y][x]) + spacer

            liner = "\n" if (y+1) % 3 else "\n" * 2
            grid += liner

        print(grid.strip())


def main():
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

    sudoku = Sudoku(grid)

    sudoku.solve()


if __name__ == "__main__":
    main()
