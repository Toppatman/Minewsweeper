from abc import ABC
import random


COVERED, UNCOVERED, FLAGGED = 1, 2, 3

class Cell(ABC):
  def __init__(self):
    self.value = None
    self.state = COVERED
  
  def uncover(self):
    if self.state != FLAGGED:
      self.state = UNCOVERED
  
  def flag(self):
    if self.state == COVERED:
      self.state = FLAGGED

  def unflag(self):
    if self.state == FLAGGED:
      self.state = COVERED

  # Return ' ' if Cell is COVERED, 'F' is Cell is FLAGGED, or Cell.value if Cell is UNCOVERED
  def show(self):
    if self.state == FLAGGED:
      return 'F'
    if self.state == UNCOVERED:
      return str(self.value)
    if self.state == COVERED:
      return ' '
      
class MineCell(Cell):
  def __init__ (self):
    super().__init__()
    self.value = '*'

class NumberedCell(Cell):
  def __init__(self, value):
    super().__init__()
    self.value = value

class Grid():
  def __init__(self, size):
    self.size = size
    self.grid = [[NumberedCell(0) for j in range(size)] for i in range(size)]
    self.numMines = size * size // 7 + 1
    self.toUncover = size * size - self.numMines
    
    temp = []
    for i in range(size):  
      for j in range(size):
        temp.append((i, j))
    self.minePos = random.sample(temp, self.numMines)
    self.placeMines()

  def placeMines(self): # Place a MineCell at each minePos position, then update the surrounding NumberCell values by +1
    for pos in self.minePos: # [(0, 0), (0, 4), (3, 4), (4, 2), (2, 3)]
      r = pos[0]
      c = pos[1]
      self.grid[r][c] = MineCell()
      for i in range(-1, 2):
        for j in range(-1, 2):
          if 0 <= r + i < self.size and 0 <= c + j < self.size and self.grid[r+i][c+j].value != '*':
            self.grid[r+i][c+j].value += 1

  def reveal(self, row, col):
    self.grid[row][col].uncover()
    if self.grid[row][col].value == '*':
      return False
    self.toUncover -= 1
    if self.grid[row][col].value != 0:
      return True
    else:
      for i in range(-1, 2):
        for j in range(-1, 2):
          if 0 <= row + i < self.size and 0 <= col + j < self.size and self.grid[row + i][col + j].state == COVERED:
            self.reveal(row + i, col + j)
    return True
  
  def flag(self, row, col):
    self.grid[row][col].flag()
    
  def unflag(self, row, col):
    self.grid[row][col].unflag()
    
  def printGrid(self):
    print('    ', end='')
    for i in range(self.size):
      print(i, end='   ')
    print()
    print('  ╔', end='')
    for i in range(self.size - 1):
      print('═══╦', end='')
    print('═══╗')
    for i in range(self.size):
      print(i, end=' ')
      for j in range(self.size):
        print('║ ' + self.grid[i][j].show() + ' ',end='')
      print('║')
      if i < self.size - 1:
        print('  ╠', end='')
        for i in range(self.size - 1):
          print('═══╬', end='')
        print('═══╣')
    print('  ╚', end='')
    for i in range(self.size - 1):
      print('═══╩', end='')
    print('═══╝')

class MineSweeper():
  def __init__(self):
    self.grid = Grid(10 )
    self.startGame()

  def startGame(self):
    while True:
      self.grid.printGrid()
      move = input("Please make a move: ")
      row = int(move[0])
      col = int(move[2])
      act = move[4].lower()
      if act == "r":
        if not self.grid.reveal(row, col):
          self.grid.printGrid()
          print("You lost!*******")
          break
      elif act == "f":
        self.grid.flag(row, col)
      elif act == "u":
        self.grid.unflag(row, col)
      if self.grid.toUncover == 0:
        self.grid.printGrid()
        print("******YOU WIN!")
        break
        
game = MineSweeper()