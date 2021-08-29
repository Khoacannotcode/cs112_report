import numpy as np
class Board():
  def __init__(self, size):
    self.board = None
    self.size = size
    self.grid_size = int(np.sqrt(size))

  def read_From_String(self, string):
    """
    Make a board from a string

    Input:
    --string : The input string
    Output (Optional):
    --board : Board after reading
    """
    list_item = string.split("-")
    list_item = [int(x) for x in list_item]
    board = []
    for i in range(len(list_item)):
        if i % self.size == 0:
            temp = []
            for j in list_item[i:i+self.size]:
                temp.append(int(j))
            board.append(temp)
    self.board = board
    return board

  def as_String(self):
    """
    Convert a board to a string representation

    Input:
    --board : a board to convert
    Ouput:
    --string : a string representation
    """
    if self.board is False:
      return("No solution!")
    return '-'.join(map(str,['-'.join(map(str, i)) for i in self.board]))

  def draw(self, name = None):
    """
    Draw the board
    """
    if name:
      print("> {}".format(name))
    if not self.board:
      print("board is None!")
    for r in range(len(self.board)):
        step = [x for x in range(self.size - 1)
                  if x%self.grid_size == 0]
        # if r == 0 or r == 3 or r == 6:
        if r in step:
            bar = self.grid_size*("+" + "-"*(3*self.grid_size + 1)) + "+"
            # print("+-------+-------+-------+")
            print(bar)
        for c in range(len(self.board[r])):
            # if c == 0 or c == 3 or c ==6:
            item = self.board[r][c]
            # item_len = len(item)
            if c in step:
                print("| ", end = "")
            if self.board[r][c] != 0:
                print(f"{item:2}", end = " ")
            else:
                print(end = "   ")
            if c == self.size - 1:
                print("|")
    # print("+-------+-------+-------+")
    print(bar)