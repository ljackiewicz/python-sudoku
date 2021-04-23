run:
	python sudoku.py

test:
	python -m unittest -v

coverage:
	coverage run -m	unittest -v
	coverage report -m sudoku.py
