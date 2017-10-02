#!/usr/bin/env python2


class Rod(object):
    def __init__(self, n, prices):
        self.rod_length = n
        self.prices = prices

    def cutRod(self):
        if self.rod_length == 0:
            return 0
        if self.rod_length == 1:
            return self.prices[0]

        sol = [0] * (self.rod_length + 1)

        sol[0] = 0

        for i in xrange(1, self.rod_length+1):
            for j in xrange(i):
                sol[i] = max(sol[i], sol[i-j-1] + self.prices[j])

        return sol[self.rod_length]


if __name__ == "__main__":
    arr = [1, 5, 8, 9, 10, 17, 17, 20]
    print Rod(8, arr).cutRod()
