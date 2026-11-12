# Number Board Game

A terminal-based Python puzzle game where players remove connected groups of matching numbers, earn points, and watch the remaining cells fall into place.

## Overview

Players choose a cell by entering its row and column. If the selected cell belongs to a connected group of two or more cells containing the same number, matching cells are removed. Cells above the cleared spaces fall downward, and the game continues until no valid matches remain.

A cell is connected to its immediate neighbors **above, below, left, and right** (not diagonally). Rows and columns are numbered starting at 1.

## Features

- Reads a number board from a space-separated text file
- Identifies connected matching cells using recursive traversal
- Removes groups of adjacent equal numbers
- Applies gravity to the remaining cells
- Calculates a score for each turn
- Handles out-of-bounds choices and moves that do not remove cells
- Ends when no matching adjacent cells remain

## Requirements

- Python 3
- No external dependencies

## Run the game

From the repository root, run:

```bash
python number_board_game.py examples/input.txt
```

Enter a row and column separated by a space, e.g. `1 3`.

## Sample input

A sample board is included in [`examples/input.txt`](examples/input.txt):

```text
1 0 4 7 6 8
0 5 4 4 5 5
2 1 4 4 4 6
4 1 3 7 4 4
```

The sample gameplay uses these moves:

| Input | Result | Total score |
| --- | --- | ---: |
| `1 3` | Valid move | 32 |
| `1 1` | No movement | 32 |
| `7 1` | Outside board | 32 |
| `3 4` | Valid move | 46 |
| `3 2` | Valid move; game ends | 48 |

The resulting terminal output is saved in [`examples/output.txt`](examples/output.txt). The output was generated using `number_board_game.py`, without changes to its program logic.

## Scoring

For each successful turn:

```text
Points = selected cell value × number of removed cells
```

## Project files

```text
number-board-game/
├── number_board_game.py
├── README.md
├── .gitignore
└── examples/
    ├── input.txt
    └── output.txt
```

## Notes

The program was tested with the included sample. Other board configurations may expose limitations.
