class Sudoku_Loader():
  def __init__(self):
    pass
  # def tmp_load(self,path):
  #   with open(path) as f:
  #     lines = f.readlines()
  #   lines[-1] += "\n"
  #   puzzle_list = []
  #   for idx in range(len(lines)):
  #     puzzle_list.append(lines[idx][:-1])
  #   return puzzle_list
  def load_From_Path(self, path):
    with open(path) as f:
      lines = f.readlines()
    if lines[-1][-1] != "\n":
      lines[-1] += "\n"
    puzzle_list = []
    GT_list = []
    for idx in range(len(lines)):
      if idx%2 == 0:
        puzzle_list.append(lines[idx][:-1])
      else:
        GT_list.append(lines[idx][:-1])
    return (puzzle_list, GT_list)

