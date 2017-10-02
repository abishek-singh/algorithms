#! /usr/bin/env python2

def main(arr, n, sum_):
    if sum_ == 0:
        return True
    if n == 0 and sum_ > 0:
        return False

    sol = [[False for _ in xrange(sum_+1)] for _ in xrange(n+1)]

    for i in xrange(n+1):
        sol[i][0] = False
    for i in xrange(sum_+1):
        sol[0][i] = True

    for i in xrange(1, n+1):
        for j in xrange(1, sum_+1):
            if j < arr[i-1]:
                sol[i][j] = sol[i-1][j]
            else:
                sol[i][j] = sol[i-1][j] or sol[i-1][j-arr[i-1]]


    print sol[n][sum_]

    for a in sol:
        print a



if __name__ == "__main__":
    arr = [1, 2, 3]
    sum_ = 187
    main(arr, 3, sum_)
