from Algorithm_Earley import Earley
from InputParser import InputParser


def main():
    print("Введите все правила грамматики в виде A -> B, конец ввода ваших правил - пустая строка.\n"
          "При этом каждый нетерминал в правой части правила(в В) заключите в <>.\n"
          "Пример: S -> <A>abs<S><T>\n"
          "Можете использовать | при вводе нескольких правил для одного и того же нетерминала:\n"
          "Пример, как можно задать таким образом: ПСП S -> |<S><S>|(<S>)\n"
          "Стартовым нетерминалом должен быть S")
    rules = []
    line = ''
    while True:
        line = input()
        if line == '':
            break
        rules.append(line)

    # Приведение правил к удобному для работы виду
    parser = InputParser()
    rules = parser.parse(rules)

    print("Введите слово для проверки на выводимость в представленной грамматике")
    algorithm = Earley()
    if algorithm.check(input(), rules):
        print('Слово выводится')
        exit()
    print('Слово не выводится')


if __name__ == "__main__":
    main()
