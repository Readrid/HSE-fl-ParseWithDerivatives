from typing import List
import sys

class Regexp:
    def match(self, w, l = None):
        if (l == None):
            l = self

        if (w == ""):
            return nullable(l)

        return self.match(w[1:], self.derivative(w[0], l))

    def derivative(self, a, re = None):
        if (re == None): re = self
        if (isinstance(re, Empty) or isinstance(re, Epsilon)):
            return Empty()
        if (isinstance(re, Char)):
            if (re.c == a): return Epsilon()
            else: return Empty()
        if (isinstance(re, Alt)):
            return alt(self.derivative(a, re.l), self.derivative(a, re.r))
        if (isinstance(re, Seq)):
            left = seq(self.derivative(a, re.l), re.r)
            if (nullable(re.l)):
                return alt(left, self.derivative(a, re.r))
            return left
        if (isinstance(re, Star)):
            return seq(self.derivative(a, re.s), re)

    
class Empty(Regexp):
    def __init__(self):
        pass

class Epsilon(Regexp):
    def __init__(self):
        pass

class Char(Regexp):
    def __init__(self, c):
        self.c = c

class Seq(Regexp):
    def __init__(self, l, r):
        self.l = l
        self.r = r

class Alt(Regexp):
    def __init__(self, l, r):
        self.l = l
        self.r = r

class Star(Regexp):
    def __init__(self, s):
        self.s = s

def seq(l, r):
    if isinstance(l, Empty) or isinstance(r, Empty):
        return Empty()
    elif isinstance(l, Epsilon):
        return r
    elif isinstance(r, Epsilon):
        return l
    else:
        return Seq(l, r)

def alt(l, r):
    if (isinstance(r, Empty)):
        return l
    elif (isinstance(l, Empty)):
        return r
    elif (isinstance(r, Epsilon)):
        if nullable(l):
            return l
        else:
            return alt(Epsilon, l)
    elif (isinstance(l, Epsilon)):
        if (nullable(r)):
            return r
        else:
            return alt(Epsilon, r)
    #elif l == r:
    #    return r
    else:
        return Alt(l , r)


def star(s):
    if (isinstance(s, Empty)):
        return Empty()
    elif (isinstance(s, Epsilon)):
        return Epsilon()
    elif (isinstance(s, Star)):
        return s
    else:
        return Star(s)

def nullable(re):
    if (isinstance(re, Empty) or isinstance(re, Char)):
        return False
    if (isinstance(re, Epsilon) or isinstance(re, Star)):
        return True
    if (isinstance(re, Alt)):
        return nullable(re.l) or nullable(re.r)
    if (isinstance(re, Seq)):
        return nullable(re.l) and nullable(re.r)

def main(args_str: List[str]):
    reg = seq(alt(Char('a'), Char('c')), Char('b'))
    re2 = Star(Char('a'))
    print(re2.match("aaaaaa"))

if __name__ == '__main__':
    main(sys.argv[1:])
