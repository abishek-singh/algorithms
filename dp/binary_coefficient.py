#! /usr/bin/env python2

import random


def binaryCoefficientGenerator(n, k):
    sol = [[0 for i in xrange(k+1)] for j in xrange(n+1)]

    for i in xrange(1, n+1):
        for j in xrange(min(i, k)+1):
            if j == 0 or j == i:
                sol[i][j] = 1
            else:
                sol[i][j] = sol[i-1][j-1] + sol[i-1][j]
    return sol[n][k]


if __name__ == "__main__":
    n = random.randint(1, 10)
    k = random.randint(0, n)
    print n, k
    out_ = binaryCoefficientGenerator(n, k)
    print out_
