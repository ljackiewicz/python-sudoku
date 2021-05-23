# Python Sudoku Solver and Generator

Project prepared for educational purposes. It is intended to help expand and organize the current Python-around knowledge.

## Description
To be completed.

## Usage
#### Preparing an environment
```shell
# creating virtual environment
poetry env use python

# activating virtual environment
poetry shell  # runs new shell with activated virtual environment
# or
source $(poetry env info --path)/bin/activate  # for POSIX shell
source {path_to_venv}\Scripts\activate.bat  # for Windows

# installing dependencies
poetry install
```

#### Running project
```shell
poetry run python -m sudoku.base
```

#### Running unit tests
```shell
poetry run python -m unittest -v
# or
poetry run pytest -v
```

## ToDos
#### General ToDos
- [x] Simple sudoku solver
- [x] Validation of input grid
- [ ] Generating Sudoku Puzzles
- [ ] Other solving algorithms
- [ ] Assessment of the difficulty level of puzzle
- [ ] Generating Sudoku Puzzle of specific difficulty level

#### Minor ToDos
- simple tests for cli module

#### Things to check out
- Badges
- GitHub Actions
- Unit Testing in Python
- Building Python packages
