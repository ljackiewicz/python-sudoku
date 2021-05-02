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

        self._solution = None

    def get_row(self, row_id: int):
        """Takes row by number (id) in human-readable format."""
        if type(row_id) is not int:
            raise TypeError

        if row_id not in range(1, 10):
            raise Exception("There are only 9 rows in range from 1 to 9.")

        return list(self.grid[row_id-1])

    def get_column(self, column_id: int):
        """Takes column by number (id) in human-readable format."""
        if type(column_id) is not int:
            raise TypeError

        if column_id not in range(1, 10):
            raise Exception("There are only 9 columns in range from 1 to 9.")

        return [row[column_id-1] for row in self.grid]

    def get_box(self, box_id: int):
        """Takes box (subgrid) by number (id) in human-readable format."""
        if type(box_id) is not int:
            raise TypeError

        if box_id not in range(1, 10):
            raise Exception("There are only 9 boxes in range from 1 to 9.")

        y = (box_id - 1) // 3
        x = (box_id - 1) % 3

        return [self.grid[sub_y + (y * 3)][sub_x + (x * 3)]
                for sub_y in range(3) for sub_x in range(3)]

    def validate_grid(self) -> bool:
        """Validates correctness of the input grid."""
        if not self.grid:
            return False

        # grid type and length
        if type(self.grid) is not list or len(self.grid) != 9:
            return False

        for row in self.grid:
            # rows type and length
            if type(row) is not list or len(row) != 9:
                return False

            # numbers type and range
            for number in row:
                if type(number) is not int or number not in range(0, 10):
                    return False

        # duplicates in row, column, box
        for i in range(1, 10):
            row = self.get_row(i)
            column = self.get_column(i)
            box = self.get_box(i)

            for number in range(1, 10):
                if row.count(number) > 1 or column.count(number) > 1 or \
                        box.count(number) > 1:
                    return False

        return True

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

        if self._solution is None:
            self._solution = [list(row) for row in self.grid]
        else:
            raise Exception("Found multiple solutions for given grid.")

    def solve_puzzle(self) -> None:
        """Wrapper method for solve and print Sudoku puzzle."""
        if not self.validate_grid():
            raise Exception(
                "The given grid is not provided in the correct format.")

        self.solve()

        if self._solution:
            self.show(self._solution)
        else:
            raise Exception("No solution was found for the given grid.")

    @staticmethod
    def show(grid: list) -> None:
        """Prints sudoku grid in nice format."""
        formatted_grid = ""

        for y in range(9):
            for x in range(9):
                spacer = "  " if (x+1) % 3 else "  " * 2
                formatted_grid += str(grid[y][x]) + spacer

            liner = "\n" if (y+1) % 3 else "\n" * 2
            formatted_grid += liner

        print(formatted_grid.strip())


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

    sudoku.solve_puzzle()


if __name__ == "__main__":
    main()
