from Regexp import *
from datetime import datetime


a = Char('a')
b = Char('b')
c = Char('c')


def testStar():
    re1 = Star(a)
    re2 = Star(Seq(a, b))
    re3 = Star(Alt(a, b))
    re4 = Star(Star(a))
    re5 = Star(Epsilon())
    assert re1.match("aaaaaaa")
    assert re1.match("b") == False
    assert re2.match("abababababab")
    assert re2.match("abbaabba") == False
    assert re3.match("aaaaa")
    assert re3.match("bbbbbbbbbbb")
    assert re3.match("aabbbab")
    assert re4.match("")
    assert re4.match("a")
    assert re4.match("ab") == False
    assert re5.match("")
    assert re5.match("asd") == False
    return True


def testSeq():
    re1 = Seq(Epsilon(), Alt(a, b))
    re2 = Seq(Star(a), Alt(Seq(a, b),c))
    re3 = Seq(Seq(a, b), Seq(c, Star(a)))
    re4 = Seq(Seq(c, Alt(b, a)), a)
    assert re1.match("a")
    assert re1.match("b")
    assert re1.match("")
    assert re2.match("aaaaaaaaaaac")
    assert re2.match("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab")
    assert re2.match("aaaaaaaaaa") == False
    assert re3.match("abca")
    assert re3.match("abc")
    assert re3.match("bcaaa") == False
    assert re4.match("cba")
    assert re4.match("caa")
    assert re4.match("cbaa") == False


def testAlt():
    re1 = Alt(Alt(Alt(Alt(Alt(Char('1'), Char ('2')), Char('3')), Char('4')), Char('5')), Char('6'))
    re2 = Alt(Star(a), b)
    re3 = Alt(Seq(a, b), Epsilon())
    assert re1.match("1")
    assert re1.match("5")
    assert re1.match("7") == False
    assert re2.match("aaaaaaaa")
    assert re2.match("b")
    assert re2.match("aaaaaaaaab") == False
    assert re3.match("")
    assert re3.match("ab")
    assert re3.match("a") == False


def testTwoSeconds():
    re = Seq(Star(Alt(a, b)), Seq(a, Star(Alt(a, b)))) # (a | b)*a(a | b)*
    long_string = ''.join("a" for _ in range(1000))

    last_time = datetime.now()
    re.match(long_string)
    time_delta = datetime.now() - last_time

    print("2 seconds example:", time_delta.total_seconds(), "sec")


def testCompareRegexp():
    re1 = Seq(Star(Alt(a, a)), Seq(a, Star(Alt(a, a))))
    re2 = Seq(a, Star(a))

    long_string = ''.join("a" for _ in range(1000))

    last_time1 = datetime.now()
    re1.match(long_string)
    time_delta1 = datetime.now() - last_time1

    last_time2 = datetime.now()
    re2.match(long_string)
    time_delta2 = datetime.now() - last_time2
    
    print("Compare results:", time_delta1.total_seconds() > time_delta2.total_seconds())


def main():
    if testStar() or testSeq() or testAlt():
        print("tests passed")
    testTwoSeconds()
    testCompareRegexp()

if __name__ == "__main__":
    main()
