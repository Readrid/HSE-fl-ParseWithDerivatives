

class Regexp {
public:
    virtual Regexp derivative(char c, const Regexp& re);

private:

};

class Empty : Regexp {
public:

};

class Epsilon : Regexp {
public:
};

class Char : Regexp {

};

class Seq : Regexp {

};

class Alt : Regexp {

};

class Star : Regexp {

};