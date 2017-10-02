#! /usr/bin/env python2

import lcs

class EditDistance(object):
    def __init__(self, s1, s2):
        self.X = s1
        self.Y = s2

    def edit_distance(self):
        m = len(self.X)
        n = len(self.Y)

        table = [[0 for _ in xrange(n+1)] for _ in xrange(m+1)]

        for i in xrange(m+1):
            for j in xrange(n+1):
                if self.X[i-1] == self.Y[j-1]:
                    table[i][j] = table[i-1][j-1]

                else:
                    table[i][j] = 1 + min(table[i-1][j], table[i][j-1], table[i-1][j-1])
       
        return table[m][n]


if __name__ == "__main__":
    x = 'saturday'
    y = 'sunday'
    print EditDistance(y, x).edit_distance()
