from Algorithm_Earley import Earley
from Algorithm_Earley import States
from InputParser import InputParser


def test_1():
    earley = Earley()
    parser = InputParser()
    rules = ['S -> <T>+<S>', 'S -> <T>', 'T -> <F>*<T>', 'T -> <F>', 'F -> (<S>)', 'F -> a']
    rules = parser.parse(rules)
    assert earley.check('((a*a)+a)', rules)


def test_2():
    earley = Earley()
    parser = InputParser()
    rules = ['S -> <T>+<S>', 'S -> <T>', 'T -> <F>*<T>', 'T -> <F>', 'F -> (<S>)', 'F -> b']
    rules = parser.parse(rules)
    assert earley.check('(b+(b*b)+b*(b*b*b*b))', rules)


def test_3():
    earley = Earley()
    parser = InputParser()
    rules = ['S -> <T>+<S>', 'S -> <T>', 'T -> <F>*<T>', 'T -> <F>', 'F -> (<S>)', 'F -> a']
    rules = parser.parse(rules)
    assert earley.check('((a+(a*(a))+a*((((a*a*a)))*a)))', rules)


def test_4():
    earley = Earley()
    parser = InputParser()
    rules = ['S -> <T>+<S>', 'S -> <T>', 'T -> <F>*<T>', 'T -> <F>', 'F -> (<S>)', 'F -> a']
    rules = parser.parse(rules)
    assert earley.check('(((a+(a*(a))+a*((((a*((a)*a))))*a))))', rules)


def test_5():
    earley = Earley()
    parser = InputParser()
    rules = ['S -> a']
    rules = parser.parse(rules)
    assert earley.check('a', rules)


def test_6():
    earley = Earley()
    parser = InputParser()
    rules = ['S -> a', 'S -> a<A>', 'A -> b']
    rules = parser.parse(rules)
    assert earley.check('ab', rules)


def test_7():
    earley = Earley()
    parser = InputParser()
    rules = ['S -> a', 'S -> a<S>', 'S -> b']
    rules = parser.parse(rules)
    assert earley.check('aaaaaaaaaab', rules)


def test_8():
    earley = Earley()
    parser = InputParser()
    rules = ['S -> a', 'S -> <A>a', 'A -> b']
    rules = parser.parse(rules)
    assert not earley.check('abadfasdf', rules)


def test_9():
    earley = Earley()
    parser = InputParser()
    rules = ['S -> <T>+<S>', 'S -> <T>', 'T -> <F>*<T>', 'T -> <F>', 'F -> (<S>)', 'F -> a']
    rules = parser.parse(rules)
    assert earley.check('(a+a)', rules)


def test_predict1():
    earley = Earley()
    parser = InputParser()
    earley.word = 'a'
    rules = ['S -> a']
    earley.rules = parser.parse(rules)
    earley.D[0] = set()
    earley.D[0].add(States('<S$>', ['<S>'], 0, 0))
    for i in range(1, len(earley.word) + 1):
        earley.D[i] = set()
    earley.predict(0)

    is_added = False
    add = States('<S>', ['a'], 0, 0)
    for situation in earley.D[0]:
        if (situation.left == add.left and situation.right == add.right and
                situation.i == add.i and situation.point == add.point):
            is_added = True

    assert is_added


def test_predict2():
    earley = Earley()
    parser = InputParser()
    earley.word = '(a+a)'
    rules = ['S -> <T>+<S>', 'S -> <T>', 'T -> <F>*<T>', 'T -> <F>', 'F -> (<S>)', 'F -> a']
    earley.rules = parser.parse(rules)
    earley.D[0] = set()
    earley.D[0].add(States('<S$>', ['<S>'], 0, 0))
    for i in range(1, len(earley.word) + 1):
        earley.D[i] = set()
    earley.predict(0)

    is_added = False
    add = States('<S>', ['<T>'], 0, 0)
    for situation in earley.D[0]:
        if (situation.left == add.left and situation.right == add.right and
                situation.i == add.i and situation.point == add.point):
            is_added = True
    assert is_added


def test_predict3():
    earley = Earley()
    parser = InputParser()
    earley.word = '(a+a)'
    rules = ['S -> <T>+<S>', 'S -> <T>', 'T -> <F>*<T>', 'T -> <F>', 'F -> (<S>)', 'F -> a']
    earley.rules = parser.parse(rules)
    earley.D[0] = set()
    earley.D[0].add(States('<S$>', ['<S>'], 0, 0))
    for i in range(1, len(earley.word) + 1):
        earley.D[i] = set()
    earley.predict(0)

    is_added = False
    add = States('<S>', ['<T>', '+', '<S>'], 0, 0)
    for situation in earley.D[0]:
        if (situation.left == add.left and situation.right == add.right and
                situation.i == add.i and situation.point == add.point):
            is_added = True
    assert is_added


def test_scan1():
    earley = Earley()
    parser = InputParser()
    earley.word = 'a'
    rules = ['S -> a']
    earley.rules = parser.parse(rules)
    earley.D[0] = set()
    earley.D[0].add(States('<S$>', ['<S>'], 0, 0))
    for i in range(1, len(earley.word) + 1):
        earley.D[i] = set()
    earley.D[0].add(States('<S>', ['a'], 0, 0))
    earley.scan(0)

    is_added = False
    add = States('<S>', ['a'], 0, 1)
    for situation in earley.D[1]:
        if (situation.left == add.left and situation.right == add.right and
                situation.i == add.i and situation.point == add.point):
            is_added = True

    assert is_added


def test_scan2():
    earley = Earley()
    parser = InputParser()
    earley.word = '(a+a)'
    rules = ['S -> <T>+<S>', 'S -> <T>', 'T -> <F>*<T>', 'T -> <F>', 'F -> (<S>)', 'F -> a']
    earley.rules = parser.parse(rules)
    earley.D[0] = set()
    earley.D[0].add(States('<S$>', ['<S>'], 0, 0))
    for i in range(1, len(earley.word) + 1):
        earley.D[i] = set()
    earley.D[2].add(States('<S>', ['<T>', '+', '<S>'], 1, 1))
    earley.scan(2)

    is_added = False
    add = States('<S>', ['<T>', '+', '<S>'], 1, 2)
    for situation in earley.D[3]:
        if (situation.left == add.left and situation.right == add.right and
                situation.i == add.i and situation.point == add.point):
            is_added = True

    assert is_added
