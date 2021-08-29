from board import Board
from backtrackingSudoku import BacktrackingSudokuSolver
from bruteforceSudoku import BruteforceSudokuSolver
from greedySudoku import GreedySudokuSolver
from sudokuLoader import Sudoku_Loader
from tqdm import tqdm

import argparse
import time
import os
import numpy as np

parser = argparse.ArgumentParser(description='Sudoku Solver')
parser.add_argument('--method', 
                    type=str, 
                    help="""
                    Choose the method to use:
                    - bruteforce
                    - greedy
                    - backtracking
                    """
)
parser.add_argument('--data_path',
                    default="puzzles\\test.txt",
                    type=str, 
                    help="Path to the txt file"
)
parser.add_argument('--show',
                    type=bool,
                    default=False,
                    help="show the sudoku boards"
)
parser.add_argument('--demo',
                    type=bool,
                    default=False,
                    help="demo the way to run of the method"
)
parser.add_argument('--eval',
                    type=bool,
                    default=False,
                    help="do evaluation"
)
args = parser.parse_args()

def get_Solver():
  if args.method == "bruteforce":
    solver = BruteforceSudokuSolver()
  elif args.method == "backtracking":
    solver = BacktrackingSudokuSolver()
  elif args.method == "greedy":
    solver = GreedySudokuSolver()
  return solver

def eval(size):
  log = []
  print("Method: ", args.method)
  solver = get_Solver()
  board = Board(size)
  list_n = [x for x in range(190, int(size)**2) if x%10==0][1:]
  for n in list_n:
    print("n = ", n, end=" ==> ")
    path = "val" + str(size) + "\\" + str(n) + ".txt"
    with open(path) as f:
      lines = f.readlines()
    if lines[-1][-1] != "\n":
      lines[-1] += "\n"
    # if args.method == "bruteforce":
    # lines = lines[:10]
    total_time = 0
    print("process:", end="")
    for idx in range(len(lines)):
      print(end="-")
      puzzle_string = lines[idx][:-1]
      board.read_From_String(puzzle_string)
      t0 = time.time()
      solver.solve(board, args.demo)
      t1 = time.time()
      total_time += (t1 - t0)
    avg_time = round(total_time / len(lines), 4)
    log.append([n, avg_time])
    print("avg_time = ", avg_time)
  for item in log:
    print(item[0], item[1])
  # for item in log:
  #   print(item[1])



# Driver Code~
def main():
  os.system('cls')
  dataloader = Sudoku_Loader()
  puzzle_list, GT_list = dataloader.load_From_Path(args.data_path)
  size = int(np.sqrt(puzzle_list[0].count("-") + 1))
  # size = int(np.sqrt(len(puzzle_list[0])))
  solver = get_Solver()
  if args.eval:
    eval(size)
    return
  for idx in range(len(puzzle_list)):
    puzzle_string = puzzle_list[idx]
    GT_string = GT_list[idx]
    board = Board(size)
    # print(board.size)
    # print(board.grid_size)
    board.read_From_String(puzzle_string)
    # board.draw()
    # return
    # continue
    print("Test case {}".format(idx+1))
    if args.show:
      board.draw()
    t0 = time.time()
    solver.solve(board, args.demo)
    t1 = time.time()
    if args.show:
      board.draw(name="Answer:")
    # if board.as_String() == GT_string:
    # if answer.as_String() == GT_string:
    print(solver.answer)
    if solver.answer == GT_string:
      print("✔ Passed!")
    else:
      print("❌ Wrong Answer!")
    print("Running time = {}".format(round(t1-t0, 5)))
    print("\n")

main()