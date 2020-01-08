from time import time
from sys import stdout

class TestSudokuSolver:
    def stressTest(self, sol, name):
        with open("stress_test.txt", "r") as fd:
            cases = list(map(eval, fd.read().splitlines()))
        self.testSolver(sol, name, cases)

    def generalTest(self, sol, name):
        with open("general_test.txt", "r") as fd:
            cases = list(map(eval, fd.read().splitlines()))
        self.testSolver(sol, name, cases)

    def testSolver(self, sol, name, cases):
        start = time()
        for i, case in enumerate(cases):
            stdout.write( "\rProgress: " + "%d/%d" % (i + 1, len(cases)) )
            stdout.flush()
            sol.solveSudoku(case)
            if not self.checkSolution(case):
                print("Case %d failed\n" % i + self.printBoard(case))
                assert False
        stdout.write("\r                    \r")
        print("- %-12s\tRunning time: %f" % (name, time() - start))

    def checkSolution(self, board):
        nums = set("123456789")
        heng = [set() for i in range(9)]
        zong = [set() for i in range(9)]
        gezi = [set() for i in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] not in nums:
                    return False
                k = i // 3 * 3 + j // 3
                num = int(board[i][j]) - 1
                if num in heng[i] or num in zong[j] or num in gezi[k]:
                    return False
                heng[i].add(num)
                zong[j].add(num)
                gezi[k].add(num)
        return True

    def printBoard(self, board):
        return "\n".join(map(" ".join, board))

from AC3SudokuSolver import AC3SudokuSolver
from AC3MRVSudokuSolver import AC3MRVSudokuSolver
from AC3LCVSudokuSolver import AC3LCVSudokuSolver
from AC3MRVLCVSudokuSolver import AC3MRVLCVSudokuSolver
from BacktrackSudokuSolver import BacktrackSudokuSolver

if __name__ == "__main__":
    test = TestSudokuSolver()
    solvers = [BacktrackSudokuSolver(), AC3SudokuSolver(),
            AC3LCVSudokuSolver(), AC3MRVSudokuSolver(), AC3MRVLCVSudokuSolver()]
    names = ["Backtrack", "Backtrack AC3", "AC3 LCV", "AC3 MRV",
            "AC3 MRV LCV"]
    print("General test")
    for i in range(len(solvers)):
        test.generalTest(solvers[i], names[i])
    print("\nStress test")
    for i in range(3, len(solvers)):
        test.stressTest(solvers[i], names[i])
