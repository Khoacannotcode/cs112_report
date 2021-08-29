# CS112
## All source code of CS112 report

## 1. Sudoku solver
```
$cd sudoku
```
To generate data
```

$python gen_val.py --size --num_test
--size: The size of sudoku board (eg. 9, 16)
--num_test: Number of case of will be gen for each n level (default=1)
```

For example if you want to gen sudoku board for 9x9 with num_test=1:
```
$python gen_val.py --size 9 --num_test 1
```

To evaluate the running time
```
python main.py --method <method> --eval 1
--method include: backtracking, bruteforce, greedy
```
* For now, after update, bruteforce and greedy are no longer available for few days

To play a demo
```
$python main.py --method <method> --demo 1
```

To check the accuracy
```
python main.py --method <method> --data_path <data_path>
```
*The example data_path is in sudoku/puzzles, sudoku/val9, sudoku/val16
