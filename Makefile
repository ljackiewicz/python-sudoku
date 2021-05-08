run:
	poetry run python sudoku.py

test:
	poetry run python -m unittest -v

coverage:
	poetry run coverage run -m	unittest -v
	poetry run coverage report -m sudoku.py
