from AC3SudokuSolver import AC3SudokuSolver
from AC3 import *
from random import choice

# AC3 filtering with Minimum Remaining Values ordering
class AC3MRVSudokuSolver(AC3SudokuSolver):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # Build CSP problem
        csp, assigned = self.buildCspProblem(board)
        # Enforce AC3 on initial assignments
        AC3(csp, makeArcQue(csp, assigned))
        # If there's still uncertain choices
        uncertain = []
        for i in range(9):
            for j in range(9):
                if len(csp.domains[(i, j)]) > 1:
                    uncertain.append((i, j))
        # Search with backtracking
        self.backtrack(csp, uncertain)
        # Fill answer back to input table
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    assert len(csp.domains[(i, j)]) is 1
                    board[i][j] = str( csp.domains[(i, j)].pop() + 1 )

    def popMinRandom(self, array, key):
        minimum, indices = float("inf"), []
        for i in xrange(len(array)):
            if key(array[i]) < minimum:
                indices = [i]
                minimum = key(array[i])
            elif key(array[i]) == minimum:
                indices.append(i)
        idx = choice(indices)
        array[idx], array[-1] = array[-1], array[idx]
        return array.pop()

    def popMin(self, array, key):
        minimum, idx = float("inf"), 0
        for i in xrange(len(array)):
            if key(array[i]) < minimum:
                idx = i
                minimum = key(array[i])
        array[idx], array[-1] = array[-1], array[idx]
        return array.pop()

    def backtrack(self, csp, uncertain):
        if not uncertain:
            return True
        X = self.popMin(uncertain, key=lambda X: len(csp.domains[X]))
        removals = defaultdict(set)
        for x in csp.domains[X]:
            domainX = csp.domains[X]
            csp.domains[X] = set([x])
            if AC3(csp, makeArcQue(csp, [X]), removals):
                retval = self.backtrack(csp, uncertain)
                if retval:
                    return True
            csp.restore_domains(removals)
            csp.domains[X] = domainX
        uncertain.append(X)
        return False
