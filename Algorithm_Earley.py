class Rule:
    def __init__(self, rule):
        # A -> B
        self.left = rule[0]  # A
        self.right = rule[1]  # B - в виде массива из нетерминалов/терминалов


class States:
    def __init__(self, left, right, index, point):
        # (A -> B•C, i)
        self.left = left  # нетерминал
        self.right = right  # правая часть правила
        self.i = index  # i
        self.point = point  # позиция точки

    def equals(self, other):
        return (self.left == other.left and
                self.right == other.right and
                self.i == other.i and
                self.point == other.point)


class Earley:
    def __init__(self):
        self.rules = []
        self.word = str
        self.legnth = 0
        self.D = {}

    # Проверка пренадлежности слова грамматике
    def check(self, word, rules):
        self.word = word
        self.D = {}
        self.length = int(len(word))
        self.rules = rules
        # Инициализация Dшек
        self.initD()

        # Основной цикл
        self.runWord()

        # Проверяем выводимость требуемого слова
        for state in self.D[self.length]:
            if state.equals(States('<S$>', ['<S>'], 0, 1)):
                return True
        return False

    def runWord(self):
        self.tryPredictAndComplete(0)
        while True:
            cntLen = len(self.D[0])
            self.tryPredictAndComplete(0)
            if cntLen == len(self.D[0]):
                break
        for i in range(1, self.length + 1):
            self.stage(i)

    def initD(self):
        for i in range(0, self.length + 1):
            self.D[i] = set()
        self.D[0].add(States('<S$>', ['<S>'], 0, 0))

    def stage(self, i):
        self.scan(i - 1)
        cntLen = len(self.D[i])
        self.tryPredictAndComplete(i)
        while len(self.D[i]) != cntLen:
            cntLen = len(self.D[i])
            self.tryPredictAndComplete(i)

    def scan(self, i):  # i - кол-во считанных символов в слове(номер рассматриваемого класса D)
        for state in self.D[i]:
            if state.point < len(state.right) and self.word[i] == state.right[state.point]:
                self.addState(States(state.left, state.right, state.i, state.point + 1), i + 1)

    def predict(self, i):  # i - кол-во считанных символов в слове(номер рассматриваемого класса D)
        new = []
        for state in self.D[i]:
            if state.point < len(state.right):
                unterminal = state.right[state.point]
                for rule in self.rules:
                    if rule.left == unterminal:
                        new.append(States(unterminal, rule.right, i, 0))

        for state in new:
            self.addState(state, i)

    def complete(self, i):  # i - кол-во считанных символов в слове(номер рассматриваемого класса D)
        new = []
        # Ищем все ситуации с точкой на конце
        for fstate in self.D[i]:
            if fstate.point == len(fstate.right):
                for state in self.D[fstate.i]:
                    if state.point < len(state.right) and state.right[state.point] == fstate.left:
                        new.append(States(state.left, state.right, state.i, state.point + 1))
        for state in new:
            self.addState(state, i)

    def tryPredictAndComplete(self, i):
        self.predict(i)
        self.complete(i)

    def addState(self, new, i):
        for state in self.D[i]:
            if state.equals(new):
                return
        self.D[i].add(new)
