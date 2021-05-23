run:
	poetry run python sudoku/base.py

test:
	poetry run pytest -v

coverage:
	poetry run coverage run -m pytest -v
	poetry run coverage report -m sudoku/base.py
