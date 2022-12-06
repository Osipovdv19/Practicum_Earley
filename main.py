from Algorithm_Earley import Earley
from InputParser import InputParser as Parser


def main():
    rules = []
    while True:
        line = input()
        if line == '':
            break
        rules.append(line)
    algo = Earley()
    print('The word is deducible' if algo.check(input(), Parser().parse(rules)) else print('The word is not deducible'))


if __name__ == "__main__":
    main()
