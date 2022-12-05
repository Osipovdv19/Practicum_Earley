import unittest
from Algorithm_Earley import Earley
from Algorithm_Earley import States


class TestEarley(unittest.TestCase):
    def test_1(self):
        earley = Earley()
        self.assertEqual(earley.check('((a*a)+a)',
                                      ['S -> T+S', 'S -> T', 'T -> F*T', 'T -> F', 'F -> (S)', 'F -> a']), True)

    def test_2(self):
        earley = Earley()
        self.assertEqual(earley.check('(b+(b*b)+b*(b*b*b*b))',
                                      ['S -> T+S', 'S -> T', 'T -> F*T', 'T -> F', 'F -> (S)', 'F -> b']), True)

    def test_3(self):
        earley = Earley()
        self.assertEqual(earley.check('((a+(a*(a))+a*((((a*a*a)))*a)))',
                                      ['S -> T+S', 'S -> T', 'T -> F*T', 'T -> F', 'F -> (S)', 'F -> a']), True)

    def test_4(self):
        earley = Earley()
        self.assertEqual(earley.check('(((a+(a*(a))+a*((((a*((a)*a))))*a))))',
                                      ['S -> T+S', 'S -> T', 'T -> F*T', 'T -> F', 'F -> (S)', 'F -> a']), True)
    
    def test_5(self):
        earley = Earley()
        self.assertEqual(earley.check('a', ['S -> a']), True)

    def test_6(self):
        earley = Earley()
        self.assertEqual(earley.check('ab', ['S -> a', 'S -> aA', 'A -> b']), True)

    def test_7(self):
        earley = Earley()
        self.assertEqual(earley.check('aaaaaaaaaab', ['S -> a', 'S -> aS', 'S -> b']), True)

    def test_8(self):
        earley = Earley()
        self.assertEqual(earley.check('abadfasdf', ['S -> a', 'S -> Aa', 'A -> b']), False)

    def test_9(self):
        earley = Earley()
        self.assertEqual(earley.check('(a+a)', ['S -> T+S', 'S -> T', 'T -> F*T', 'T -> F', 'F -> (S)', 'F -> a']),
                         True)
        

class PredictTest(unittest.TestCase):
    def test_1(self):
        earley = Earley()
        earley.word = 'a'
        earley.rulesConvert(['S -> a'])
        earley.D[0] = set()
        earley.D[0].add(States('S#', 'S', 0, 0))
        for i in range(1, len(earley.word) + 1):
            earley.D[i] = set()
        earley.predict(0)

        is_added = False
        add = States('S', 'a', 0, 0)
        for situation in earley.D[0]:
            if (situation.left == add.left and situation.right == add.right and
                    situation.i == add.i and situation.point == add.point):
                is_added = True

        self.assertEqual(is_added, True)

    def test_2(self):
        earley = Earley()
        earley.word = '(a+a)'
        earley.rulesConvert(['S -> T+S', 'S -> T', 'T -> F*T', 'T -> F', 'F -> (S)', 'F -> a'])
        earley.D[0] = set()
        earley.D[0].add(States('S#', 'S', 0, 0))
        for i in range(1, len(earley.word) + 1):
            earley.D[i] = set()
        earley.predict(0)

        is_added = False
        add = States('S', 'T', 0, 0)
        for situation in earley.D[0]:
            if (situation.left == add.left and situation.right == add.right and
                    situation.i == add.i and situation.point == add.point):
                is_added = True

        self.assertEqual(is_added, True)

    def test_3(self):
        earley = Earley()
        earley.word = '(a+a)'
        earley.rulesConvert(['S -> T+S', 'S -> T', 'T -> F*T', 'T -> F', 'F -> (S)', 'F -> a'])
        earley.D[0] = set()
        earley.D[0].add(States('S#', 'S', 0, 0))
        for i in range(1, len(earley.word) + 1):
            earley.D[i] = set()
        earley.predict(0)

        is_added = False
        add = States('S', 'T+S', 0, 0)
        for situation in earley.D[0]:
            if (situation.left == add.left and situation.right == add.right and
                    situation.i == add.i and situation.point == add.point):
                is_added = True

        self.assertEqual(is_added, True)


class ScanTest(unittest.TestCase):
    def test_1(self):
        earley = Earley()
        earley.word = 'a'
        earley.rulesConvert(['S -> a'])
        earley.D[0] = set()
        earley.D[0].add(States('S#', 'S', 0, 0))
        for i in range(1, len(earley.word) + 1):
            earley.D[i] = set()
        earley.D[0].add(States('S', 'a', 0, 0))
        earley.scan(0)

        is_added = False
        add = States('S', 'a', 0, 1)
        for situation in earley.D[1]:
            if (situation.left == add.left and situation.right == add.right and
                    situation.i == add.i and situation.point == add.point):
                is_added = True

        self.assertEqual(is_added, True)

    def test_2(self):
        earley = Earley()
        earley.word = '(a+a)'
        earley.rulesConvert(['S -> T+S', 'S -> T', 'T -> F*T', 'T -> F', 'F -> (S)', 'F -> a'])
        earley.D[0] = set()
        earley.D[0].add(States('S#', 'S', 0, 0))
        for i in range(1, len(earley.word) + 1):
            earley.D[i] = set()
        earley.D[2].add(States('S', 'T+S', 1, 1))
        earley.scan(2)

        is_added = False
        add = States('S', 'T+S', 1, 2)
        for situation in earley.D[3]:
            if (situation.left == add.left and situation.right == add.right and
                    situation.i == add.i and situation.point == add.point):
                is_added = True

        self.assertEqual(is_added, True)


if __name__ == '__main__':
    unittest.main()
