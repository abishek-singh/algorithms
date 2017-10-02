#! /usr/bin/env python2


from collections import defaultdict


class AssignCap(object):
    def __init__(self):
        self.caps = defaultdict(list)
        self.all_mask = 0
        self.total_caps = 100

    def countWaysUtil(self, dp, mask, i):
        if mask == self.all_mask:
            return 1

        if i > self.total_caps:
            return 0

        if dp[mask][i]!= -1:
            return dp[mask][i]

        ways = self.countWaysUtil(dp, mask, i+1)

        if i in self.caps:
            for ppl in self.caps[i]:
                if mask & (1 << ppl):
                    continue
                ways += self.countWaysUtil(dp, mask | (1 << ppl), i+1)

                ways = ways % ((10 ** 9) + 7)

        dp[mask][i] = ways
        return dp[mask][i]

    def countWays(self, n):
        for ppl in range(n):
            for cap in  map(int, raw_input().strip().split()):
                self.caps[cap].append(ppl)

        self.all_mask = (1 << n) - 1

        sol = [[-1 for i in range(self.total_caps+1)] for j in range(2 ** n)]

        return self.countWaysUtil(sol, 0, 1)


def main():
    num_of_people = input()
    print AssignCap().countWays(num_of_people)


if __name__ == "__main__":
    main()
