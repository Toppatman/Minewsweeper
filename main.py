# MineSweeper, Grid, Cell, MineCell, NumberCell
import random

covered, uncovered, flagged = 0, 1, 2

class Cell():
  def __init__(self):
    self.state = covered
    self.value = None # Either a number for a NumberCell or '*' for a MineCellself
  
  def uncover(self):
    if self.state == covered:
      self.state = uncovered
    
  def flag(self):
    if self.state == covered:
      self.state = flagged

  def unflag(self):
    if self.state == flagged:
      self.state = covered

  # This function should return a blank character ' ' if cell is covered, an 'F' is the cell is flagged, or self.value otherwise
  def show(self):
    if self.state == covered:
      return ' '
    if self.state == flagged:
      return 'F'
    if self.state == uncovered:
      return str(self.value)

# Initialize self.value to '*'
class MineCell(Cell):
  def __init__(self):
    super().__init__()
    self.value = '*'

# Initialize self.value to a number value taken as a parameter
class NumberCell(Cell):
  def __init__(self, value):
    super().__init__()
    self.value = value

class Grid():
  def __init__(self, size):
    self.size = size
    # self.grid = [[NumberCell(0) for j in range(size)] for i in range(size)]
    self.grid = []
    for i in range(size):
      self.grid.append([])
      for j in range(size):
        self.grid[i].append(NumberCell(0))
        
    self.minePos = random.sample([(i, j) for j in range(size) for i in range(size)], size * size // 8)
    self.placeMines()

  def placeMines(self):
    for pos in self.minePos:
      row, col = pos[0], pos[1]
      self.grid[row][col] = MineCell()
      for i in range(-1, 2):
        for j in range(-1, 2):
          if 0 <= row + i < self.size and 0 <= col + j < self.size and self.grid[row + i][col + j].value != '*':
            self.grid[row + i][col + j].value += 1

  
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
    self.grid = Grid(10)
    self.startGame()

  def startGame(self):
    while True:
      self.grid.printGrid()
      move = input("Make a move: ")
      row = int(move[0])
      col = int(move[2])
      act = move[4]
      # Reveal = R Flag = F Unflag = U
      
      if act == 'R':
        # Code to uncover cell at row, col
        pass
      elif act == 'F':
        # Code to flag cell at row, col
        pass
      elif act == 'U':
        # Code to unflag cell at row, col
        pass
      

MineSweeper()