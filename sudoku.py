#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Sudoku(object):
    def __init__(self, grid: list = None) -> None:
        if grid is None:
            grid = []

        self.grid = grid

    def show(self) -> None:
        for x in range(9):
            for y in range(9):
                print(self.grid[x][y], end="  ")
            print()


def main():
    grid = [[0] * 9] * 9

    sudoku = Sudoku(grid)

    sudoku.show()


if __name__ == "__main__":
    main()
