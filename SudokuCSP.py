from CSP import CSP

class SudokuCSP(CSP):
    def conflicts(self, (i1, j1), x, (i2, j2), y):
        k1 = i1 / 3 * 3 + j1 / 3
        k2 = i2 / 3 * 3 + j2 / 3
        return x == y and ( i1 == i2 or j1 == j2 or k1 == k2 )

