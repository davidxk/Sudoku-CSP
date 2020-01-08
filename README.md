# Sudoku
## Sudoku Solvers with CSP techniques
Implement sudoku solvers with the following techniques for solving Constraint Satisfaction Problems(CSP): 

* Backtracking
* Backtracking with AC-3 filtering
* Backtracking with AC-3 filtering and LCV ordering
* Backtracking with AC-3 filtering and MRV ordering
* Backtracking with AC-3 filtering, MRV and LCV ordering

AC-3 stands for Arc-Consistency Algorithm, which is a inference algorithm for solving CSP problems. MRV and LCV stands for Minimum Remaining Values and Least Constraining Value respectively, which are ordering techniques for CSP search. 

All sudoku solvers implements the following interface

```python
def solveSudoku(self, board):
	"""
	:type board: List[List[str]]
	:rtype: void Do not return anything, modify board in-place instead.
	"""
	pass
```

To test these algorithms, run command

```shell
$ python3 TestSudokuSolver.py
```

## Generate Random Sudoku Grid
Generate random filled Sudoku grid with the following command:

```shell
$ python3 SudokuGenerator.py
```

Sudoku puzzles creation is a problem in the Mathematical Contest in Modeling(MCM) in 2008. Generate random filled Sudoku grid can be considered as the first step in this problem. My algorithm using the following strategy:

1. Randomly fill 18 to 24 numbers in a grid while maintaining consistency
2. Use an efficient Sudoku Solver to search for a solution to this half-filled grid

The general strategy is to fill some boxes randomly, and fill the rest of the boxes with a sudoku solver if a solution exists. 

The key here is to introduce just the right amount of randomness. If too many boxes are filled randomly, then it will probably result in a grid with no solution at all. But if too few boxes are filled, then the task of searching for a solution might take forever. 

## Solve Sudoku
Put sudoku problems in file `input.txt` in the given format, where the first line specify the number of cases and the following lines list the problem. Numbers are separated by spaces and empty boxes are represented as dots. There is no empty lines between cases.

Run command

```shell
$ python3 SolveSudoku.py
```
