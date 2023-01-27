from AC3SudokuSolver import AC3SudokuSolver
from AC3 import *
from random import choice

# AC3 filtering with Minimum Remaining Values and Least Constraining Value
# ordering
class AC3MRVLCVSudokuSolver(AC3SudokuSolver):
    def count_conflict(self, csp, Xi, x):
        cnt = 0
        for X in csp.adjList[Xi]:
            if x in csp.domains[X]:
                cnt += 1
        return cnt

    def popMin(self, array, key):
        minimum, idx = float("inf"), 0
        for i in range(len(array)):
            if key(array[i]) < minimum:
                idx = i
                minimum = key(array[i])
        array[idx], array[-1] = array[-1], array[idx]
        return array.pop()

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # Build CSP problem
        csp, assigned = self.buildCspProblem(board)
        # Enforce AC3 on initial assignments
        if not AC3(csp, makeArcQue(csp, assigned)):
            return False
        # If there's still uncertain choices
        uncertain = []
        for i in range(9):
            for j in range(9):
                if len(csp.domains[(i, j)]) > 1:
                    uncertain.append((i, j))
        # Search with backtracking
        if not self.backtrack(csp, uncertain):
            return False
        # Fill answer back to input table
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    assert len(csp.domains[(i, j)]) == 1
                    board[i][j] = str( csp.domains[(i, j)].pop() + 1 )
        return True

    def backtrack(self, csp, uncertain):
        if not uncertain:
            return True
        X = self.popMin(uncertain, key=lambda X: len(csp.domains[X]))
        removals = defaultdict(set)
        # Sort the values in domain in the order of LCV and loop in that order
        domainlist = list(csp.domains[X])
        domainlist.sort(key=lambda x: self.count_conflict(csp, X, x))
        for x in domainlist:
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
