from AC3 import *
from collections import defaultdict
from SudokuSolver import SudokuSolver

# Backtracking search with AC3 Maintaining Arc Consistency
class AC3SudokuSolver(SudokuSolver):
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
    
    def backtrack(self, csp, uncertain):
        if not uncertain:
            return True
        X = uncertain.pop()
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
