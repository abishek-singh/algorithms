#! /usr/bin/env python

class Matrix(object):
    def __init__(self, mat, r, c):
        self.matrix = mat
        self.row = r
        self.column = c

    def find_subarray(self):
        sol = [[0 for _ in xrange(self.column)] for _ in xrange(self.row)]
        for i in xrange(self.column):
            sol[0][i] = self.matrix[0][i]
        for i in xrange(self.row):
            sol[i][0] = self.matrix[i][0]

        for i in xrange(1, self.row):
            for j in xrange(1, self.column):
                if self.matrix[i][j] == 0:
                    sol[i][j] = 0
                else:
                    sol[i][j] = min(sol[i-1][j], sol[i][j-1], sol[i-1][j-1]) + 1

        for row in sol:
            print row


if __name__ == "__main__":
    matrix =  [[0, 1, 1, 0, 1], [1, 1, 0, 1, 0], [0, 1, 1, 1, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]
    Matrix(matrix, 6, 5).find_subarray()
