from collections import defaultdict
from SudokuCSP import SudokuCSP

class SudokuSolver(object):
    def __addEdge__(self, i, j, adjList):
        k = i // 3 * 3 + j // 3
        for num in range(9):
            if num != i:
                adjList[(i, j)].add((num, j))
            if num != j:
                adjList[(i, j)].add((i, num))
            row = num//3 + k//3 * 3
            col = num%3 + k%3 * 3
            if row != i or col != j:
                adjList[(i, j)].add((row, col))

    def buildCspProblem(self, board):
        adjList = defaultdict(set)
        # Build graph (contraints)
        for i in range(9):
            for j in range(9):
                self.__addEdge__(i, j, adjList)
        # Set domains
        variables = []
        assigned = []
        domains = {}
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    domains[(i, j)] = set(range(9))
                    variables.append((i, j))
                else:
                    domains[(i, j)] = set([int(board[i][j]) - 1])
                    assigned.append((i, j))
        return SudokuCSP(variables, adjList, domains), assigned

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        pass
