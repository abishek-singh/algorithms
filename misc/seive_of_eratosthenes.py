#! /usr/bin/env python2

def main(n):
    num = [True] * (n+1)
    p = 2
    while p * p <= n:
        if num[p] == True:
            for i in xrange(2, n / p + 1):
                num[i*p] = False

        p += 1

    count = 0
    for i in xrange(2, n+1):
        if num[i]:
            print i,
            count += 1
    print
    print count


if __name__ == "__main__":
    n = int(raw_input().strip())
    main(n)
