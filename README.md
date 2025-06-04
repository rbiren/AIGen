# AIGen

This repository contains a simple command-line Minesweeper game written in Python.

## Running Minesweeper

Execute the game with Python 3:

```bash
python3 minesweeper.py
```

You will be prompted for the board width, height, and number of bombs. Use the defaults by pressing Enter.

During the game enter commands in the form:

- `o x y` to open the cell at column `x`, row `y`.
- `f x y` to flag or unflag the cell at column `x`, row `y`.

The board is cleared when all non-bomb cells are revealed. Stepping on a bomb ends the game.
