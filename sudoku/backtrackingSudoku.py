from board import Board
import os
import time

class BacktrackingSudokuSolver():
  def __init__(self):
    # The set contains all solution found
    self.answer = "No Solution!"
  
  def find_Zero(self, board):
    """
    Find the first index of zero in the board.

    Input:
    --board : board to search
    Outout:
    --(row, col) : position of the first zero, if not found return False.
    """
    for row in range(board.size):
      if 0 in board.board[row]:
        col = board.board[row].index(0)
        return (row, col)
    return False

  def is_Valid(self, board, row, col, value):
    # Check row:
    for j in range(board.size):
      if board.board[row][j] == value:
        return False
    # Check column:
    for i in range(board.size):
      if board.board[i][col] == value:
        return False
    # Check block
    block_row = row // board.grid_size
    block_col = col // board.grid_size
    for i in range(board.grid_size):
      for j in range(board.grid_size):
        if board.board[board.grid_size*block_row + i][board.grid_size*block_col + j] == value:
          return False
    return True

  def is_Valid(self, board, row, col, value):
    """
    Check if the value in position (row, col) is a valid or not.

    Input:
    --board : board to check
    --row : row to check
    --col : column to check
    --value : value to check
    Output:
    --True if valid
    --False if not valid
    """
    # Check row:
    for j in range(board.size):
      if board.board[row][j] == value:
        return False
    # Check column:
    for i in range(board.size):
      if board.board[i][col] == value:
        return False
    # Check block
    block_row = row // board.grid_size
    block_col = col // board.grid_size
    for i in range(board.grid_size):
      for j in range(board.grid_size):
        if board.board[board.grid_size*block_row + i][board.grid_size*block_col + j] == value:
          return False
    return True

  def solve(self, board, demo=False):
    """
    Solve the Sudoku board using Backtracking Algorithm

    Input:
    --board : board after solving
    Output:
    --board : Solved board
    """
    if demo:
      self.demo(board)
    cell = self.find_Zero(board)
    if not cell:
      return True
    else:
      row, col = cell
    for val in range(1,board.size+1):
      if self.is_Valid(board, row, col, val):
        board.board[row][col] = val
        if self.solve(board):
          self.answer = board.as_String()
          return board
        # Trigger for backtracking
        board.board[row][col] = 0
    return False

  def demo(self, board):
    """
    demo the running process of backtracking
    """
    def solve_this(board):
      cell = self.find_Zero(board)
      if not cell:
        return
      else:
        row, col = cell[0], cell[1]
        for val in range(1,board.size+1):
          if self.is_Valid(board, row, col, val):
            board.board[row][col] = val
            os.system("cls")
            board.draw("Method : Backtracking")
            # time.sleep(0.01)
            solve_this(board)
            # Backtrack here!
            board.board[row][col] = 0
        return None
    solve_this(board)
    return self.solutions