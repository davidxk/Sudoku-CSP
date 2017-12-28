from AC3SudokuSolver import AC3SudokuSolver
from AC3 import *

# AC3 filtering with Least Constraining Value ordering
class AC3LCVSudokuSolver(AC3SudokuSolver):
    def count_conflict(self, csp, Xi, x):
        cnt = 0
        for X in csp.adjList[Xi]:
            if x in csp.domains[X]:
                cnt += 1
        return cnt

    def backtrack(self, csp, uncertain):
        if not uncertain:
            return True
        X = uncertain.pop()
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
