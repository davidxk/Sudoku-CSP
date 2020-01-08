from AC3MRVLCVSudokuSolver import AC3MRVLCVSudokuSolver
from TestSudokuSolver import TestSudokuSolver

with open("input.txt", "r") as fd:
    ncases = int(fd.readline())
    cases = []
    for i in range(ncases):
        case = []
        for j in range(9):
            case.append(fd.readline().split())
        cases.append(case)

sol = AC3MRVLCVSudokuSolver()
test = TestSudokuSolver()
for board in cases:
    sol.solveSudoku(board)
    print(test.printBoard(board))
    print()
