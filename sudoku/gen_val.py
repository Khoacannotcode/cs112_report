import os
import random

import argparse

parser = argparse.ArgumentParser(description='gen sudoku board')
parser.add_argument('--size',
                    type=str,
                    default=9,
)
parser.add_argument('--num_test',
                    type=int,
                    default=1,
)
args = parser.parse_args()

root = "val" + args.size
if not os.path.exists(root):
    os.makedirs(root)

source_txt = "all" + args.size + ".txt"

remove = os.listdir(root)
remove.remove(source_txt)
# print("remove: ", remove)
for item in remove:
  os.remove(os.path.join(root,item))

list_n = [x for x in range(int(args.size)**2) if x%10==0][1:]

with open(os.path.join(root, source_txt)) as f:
  lines = f.readlines()
lines[-1] += "\n"
puzzle_list = []

for idx in range(len(lines)):
  puzzle_list.append(lines[idx][:-1])
# for puzzle in puzzle_list:
#   print(len(puzzle))
puzzle_list = puzzle_list[:1]

idx_list = [x for x in range(int(args.size)**2)]


for n in list_n:
  print("gen testcase for m = ", n)
  txt_file = open(root + "\\{}.txt".format(str(n)),"w+")
  for puzzle in puzzle_list:
    for _ in range(args.num_test):
      sample = random.sample(idx_list, n)     
      tmp_list = puzzle.split("-")
      for idx in sample:
        tmp_list[idx] = 0
        # tmp_string = tmp_string[:idx] + "0" + tmp_string[idx+1:]
      # tmp_string = "-".join(tmp_string)
      tmp_string = '-'.join(str(i) for i in tmp_list)
      # print(tmp_string)
      txt_file.write(tmp_string + "\n")



