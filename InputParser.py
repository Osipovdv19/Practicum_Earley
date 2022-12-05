from Algorithm_Earley import Rule


class InputParser:
    def __init__(self):
        self.rules = []

    def parse(self, rules):
        rules.append('S$ -> <S>')
        for rule in rules:
            parts = str(rule).split(' -> ')
            for i in str(parts[1]).split('|'):
                self.rules.append(Rule([str('<' + parts[0] + '>'), self.parseParts(i)]))
        return self.rules

    def parseParts(self, part):
        ans = []
        tmp = str()
        is_nonterminal = False
        for i in str(part):
            if i == '<':
                is_nonterminal = True
            elif i == '>':
                ans.append(str('<' + tmp + '>'))
                tmp = str()
                is_nonterminal = False
            elif is_nonterminal:
                tmp = tmp + i
            else:
                ans.append(i)
        return ans
