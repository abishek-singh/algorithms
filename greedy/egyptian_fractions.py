#! /usr/bin/env py2

import random


class EgyptianFraction(object):
    def __init__(self, nr, dr):
        self.nr = nr
        self.dr = dr

    def egyptian_fraction(self):
        if self.nr == 0 or self.dr == 0:
            print "Improper Fraction"
            return

        if self.dr % self.nr == 0:
            print "1/%s" % str(self.dr / self.nr)
            return

        if self.nr % self.dr == 0:
            print self.nr / self.dr
            return

        if self.nr > self.dr:
            print "1 + ",
            self.nr = self.nr % self.dr
            self.egyptian_fraction()
            return

        ceil = self.dr / self.nr + 1
        print "1/%s + " % str(ceil),
        self.nr = self.nr * ceil - self.dr
        self.dr = self.dr * ceil
        self.egyptian_fraction()
        return


if __name__ == "__main__":
    nr = random.randint(10, 50)
    dr = random.randint(10, 50)
    print str(nr) + "/" + str(dr) + " ===> ",
    EgyptianFraction(nr, dr).egyptian_fraction()
