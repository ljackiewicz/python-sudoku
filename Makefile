run:
	poetry run python sudoku/base.py

test:
	poetry run python -m unittest -v

coverage:
	poetry run coverage run -m	unittest -v
	poetry run coverage report -m sudoku/base.py
