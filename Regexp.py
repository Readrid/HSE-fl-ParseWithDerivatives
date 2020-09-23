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
            return Alt(self.derivative(a, re.l), self.derivative(a, re.r))
        if (isinstance(re, Seq)):
            left = Seq(self.derivative(a, re.l), r)
            if (nullable(re.l)):
                return Alt(left, self.derivative(a, re.r))
            return left
        if (isinstance(re, Star)):
            return Seq(self.derivative(a, re.s), re.s)

    

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
        if (isinstance(l, Empty) or isinstance(r, Empty)):
            self = Empty()
        elif (isinstance(l, Epsilon)):
            self = r
        elif (isinstance(r, Epsilon)):
            self = l
        else:
            self.l = l
            self.r = r

class Alt(Regexp):
    def __init__(self, l, r):
        if (isinstance(r, Empty)):
            self = l
        elif (isinstance(l, Empty)):
            self = r
        elif (isinstance(r, Epsilon)):
            if nullable(l):
                self = l
            else:
                self = Alt(Epsilon, l)
        elif (isinstance(l, Epsilon)):
            if (nullable(r)):
                self = r
            else:
                self = Alt(Epsilon, r)
        elif l == r:
            self = r
        else:
            self.l = l
            self.r = r



class Star(Regexp):
    def __init__(self, s):
        if (isinstance(s, Epsilon)):
            self = Epsilon()
        elif (isinstance(s, Empty)):
            self = Empty()
        elif (isinstance(s, Star)):
            self = s
        else:
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
    reg = Star(Char('a'))
    print(reg.match("aaaa"))

if __name__ == '__main__':
    main(sys.argv[1:])
