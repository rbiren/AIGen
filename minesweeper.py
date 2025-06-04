import random
from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class Cell:
    is_bomb: bool = False
    revealed: bool = False
    flagged: bool = False
    adjacent_bombs: int = 0

class MinesweeperBoard:
    def __init__(self, width: int, height: int, bombs: int):
        self.width = width
        self.height = height
        self.bombs = bombs
        self.board: List[List[Cell]] = [[Cell() for _ in range(width)] for _ in range(height)]
        self._place_bombs()
        self._calculate_adjacent_counts()
        self.revealed_cells = 0

    def _place_bombs(self):
        positions = [(x, y) for x in range(self.width) for y in range(self.height)]
        for x, y in random.sample(positions, self.bombs):
            self.board[y][x].is_bomb = True

    def _calculate_adjacent_counts(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x].is_bomb:
                    continue
                count = 0
                for nx, ny in self._neighbors(x, y):
                    if self.board[ny][nx].is_bomb:
                        count += 1
                self.board[y][x].adjacent_bombs = count

    def _neighbors(self, x: int, y: int) -> List[Tuple[int, int]]:
        coords = []
        for ny in range(max(0, y-1), min(self.height, y+2)):
            for nx in range(max(0, x-1), min(self.width, x+2)):
                if nx == x and ny == y:
                    continue
                coords.append((nx, ny))
        return coords

    def reveal(self, x: int, y: int) -> bool:
        cell = self.board[y][x]
        if cell.revealed or cell.flagged:
            return True
        cell.revealed = True
        if cell.is_bomb:
            return False
        self.revealed_cells += 1
        if cell.adjacent_bombs == 0:
            for nx, ny in self._neighbors(x, y):
                if not self.board[ny][nx].revealed:
                    self.reveal(nx, ny)
        return True

    def toggle_flag(self, x: int, y: int):
        cell = self.board[y][x]
        if not cell.revealed:
            cell.flagged = not cell.flagged

    def is_victory(self) -> bool:
        return self.revealed_cells == self.width * self.height - self.bombs

    def display(self, reveal_all: bool = False):
        header = "  " + " ".join(str(i) for i in range(self.width))
        print(header)
        for y in range(self.height):
            row = []
            for x in range(self.width):
                cell = self.board[y][x]
                char = '.'
                if cell.revealed or reveal_all:
                    if cell.is_bomb:
                        char = '*'
                    else:
                        char = str(cell.adjacent_bombs) if cell.adjacent_bombs > 0 else ' '
                elif cell.flagged:
                    char = 'F'
                row.append(char)
            print(f"{y} " + " ".join(row))


def main():
    print("Welcome to Minesweeper!")
    width = int(input("Width of board [10]: ") or 10)
    height = int(input("Height of board [10]: ") or 10)
    bombs = int(input("Number of bombs [10]: ") or 10)
    game = MinesweeperBoard(width, height, bombs)

    while True:
        game.display()
        action = input("Enter command (o x y = open, f x y = flag): ")
        parts = action.split()
        if len(parts) != 3:
            print("Invalid command")
            continue
        cmd, x_str, y_str = parts
        if not (x_str.isdigit() and y_str.isdigit()):
            print("Coordinates must be numbers")
            continue
        x, y = int(x_str), int(y_str)
        if not (0 <= x < width and 0 <= y < height):
            print("Out of bounds")
            continue
        if cmd.lower() == 'o':
            if not game.reveal(x, y):
                game.display(reveal_all=True)
                print("Boom! You hit a bomb. Game over.")
                break
            if game.is_victory():
                game.display(reveal_all=True)
                print("Congratulations! You cleared the board.")
                break
        elif cmd.lower() == 'f':
            game.toggle_flag(x, y)
        else:
            print("Unknown command")

if __name__ == "__main__":
    main()
