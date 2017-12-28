from random import *
from copy import deepcopy
class SudokuGenerator:
    def __init__(self, solver):
        self.solver = solver

    def generateSudoku(self):
        board = [['.'] * 9 for i in range(9)]

        horizontal = [set(range(9)) for i in range(9)]
        vertical = [set(range(9)) for i in range(9)]
        regional = [set(range(9)) for i in range(9)]

        numFill = randrange(18, 25)

        for cnt in range(numFill):
            i, j = randrange(9), randrange(9)
            while board[i][j] != '.':
                i, j = randrange(9), randrange(9)
            k = i / 3 * 3 + j / 3

            intersect = horizontal[i] & vertical[j] & regional[k]
            if not intersect:
                break
            num = choice(list(intersect))
            board[i][j] = chr(ord('0') + num + 1)
            horizontal[i].remove(num)
            vertical[j].remove(num)
            regional[k].remove(num)

        solution = deepcopy(board)
        if self.solver.solveSudoku(solution):
            return board, solution
        return None, None

from AC3MRVLCVSudokuSolver import AC3MRVLCVSudokuSolver
if __name__ == "__main__":
    gen = SudokuGenerator(AC3MRVLCVSudokuSolver())
    cnt = 1
    while cnt < 6:
        board, solution = gen.generateSudoku()
        if board:
            print "Problem %d" % cnt
            print "\n".join(map(" ".join, board))
            print "Solution %d" % cnt
            print "\n".join(map(" ".join, solution))
            print
            cnt += 1
