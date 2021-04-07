#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Sudoku(object):
    def __init__(self, grid: list = None) -> None:
        if grid is None:
            grid = []

        self.grid = grid

    def show(self) -> None:
        grid = ""

        for y in range(9):
            for x in range(9):
                spacer = "  " if (x+1) % 3 else "  " * 2
                grid += str(self.grid[y][x]) + spacer

            liner = "\n" if (y+1) % 3 else "\n" * 2
            grid += liner

        print(grid.strip())


def main():
    grid = [[0] * 9] * 9

    sudoku = Sudoku(grid)

    sudoku.show()


if __name__ == "__main__":
    main()
