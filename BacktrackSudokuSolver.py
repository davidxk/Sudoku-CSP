from SudokuSolver import SudokuSolver

class BacktrackSudokuSolver(SudokuSolver):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        heng = [set() for i in range(9)]
        zong = [set() for i in range(9)]
        gezi = [set() for i in range(9)]
        blank = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    k = i / 3 * 3 + j / 3
                    num = ord(board[i][j]) - ord('0') - 1
                    heng[i].add(num); zong[j].add(num); gezi[k].add(num)
                else:
                    blank.append((i, j))

        def backtrack(start):
            if start >= len(blank):
                return True
            i, j = blank[start]
            k = i / 3 * 3 + j / 3
            for num in range(9):
                if num not in heng[i] and num not in zong[j] and\
                        num not in gezi[k]:
                    board[i][j] = chr(ord('0') + num + 1)
                    heng[i].add(num); zong[j].add(num); gezi[k].add(num)
                    if backtrack(start + 1):
                        return True
                    heng[i].remove(num); zong[j].remove(num); gezi[k].remove(num)
                    board[i][j] = '.'
            return False

        backtrack(0)
        return None
