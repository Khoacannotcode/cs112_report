from board import Board
import copy
import os

class BruteforceSudokuSolver():
  def __init__(self):
    # The set contains all solution found
    self.solutions = set()
  
  def find_Zero_Indexs(self, string):
    out_list = []
    for idx in range(len(string)):
      if string[idx] == "0":
        out_list.append(idx)
    return out_list

  # def find_Zero(self, board):
  #   """
  #   Find the first index of zero in the board.

  #   Input:
  #   --board : board to search
  #   Outout:
  #   --(row, col) : position of the first zero, if not found return False.
  #   """
  #   for row in range(9):
  #     if 0 in board[row]:
  #       col = board[row].index(0)
  #       return (row, col)
  #   return False

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
    for j in range(9):
      if board[row][j] == value:
        return False
    # Check column:
    for i in range(9):
      if board[i][col] == value:
        return False
    # Check block
    block_row = row // 3
    block_col = col // 3
    for i in range(3):
      for j in range(3):
        if board[3*block_row + i][3*block_col + j] == value:
          return False
    return True

  def check(self, board):
    for row in range(9):
      for col in range(9):
        value = board[row][col]
        board[row][col] = 0
        if not self.is_Valid(board, row, col, value):
          return False
        board[row][col] = value
    return True

  def gen_Try_Board(self, ori_string, try_string, try_idx_list, size):
    out_string = copy.deepcopy(ori_string)
    for idx in try_idx_list:
      out_string = out_string[:idx] + try_string[0] + out_string[idx+1:]
      try_string = try_string[1:]
    out_board = Board(size)
    out_board.read_From_String(out_string)
    return out_board

  def solve(self, board, demo=False):
    size = board.size
    ori_string = board.as_String()
    try_idx_list = self.find_Zero_Indexs(ori_string)
    n = len(try_idx_list)
    start = int("1"*n)
    stop = int("9"*n)
    for try_string in range(start, stop+1):
      try_string = str(try_string)
      if "0" in try_string:
        continue
      try_board = self.gen_Try_Board(ori_string, try_string, try_idx_list, size)
      if demo:
        os.system("cls")
        try_board.draw(name="Method: Bruteforce")
      if self.check(try_board.board):
        board = copy.deepcopy(try_board)
        # print("avarv")
        # print(board.as_String())
        return board

  # def solve(self, board):
  #   """
  #   Solve the Sudoku board using Backtracking Algorithm

  #   Input:
  #   --board : board after solving
  #   Output:
  #   --board : Solved board
  #   """
  #   cell = self.find_Zero(board.board)
  #   if not cell:
  #     return True
  #   else:
  #     row, col = cell
  #   for val in range(1,10):
  #     if self.is_Valid(board.board, row, col, val):
  #       board.board[row][col] = val
  #       if self.solve(board):
  #         # self.solutions.add(board.to_String())
  #         return board
  #       # Trigger for backtracking
  #       board.board[row][col] = 0
  #   return False