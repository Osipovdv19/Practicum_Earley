from Algorithm_Earley import Earley
from InputParser import InputParser as Parser


def main():
    rules = []
    while True:
        line = input()
        if line == '':
            break
        rules.append(line)
    if Earley().check(input(), Parser().parse(rules)):
        print('The word is deducible')
    else:
        print('The word is not deducible')


if __name__ == "__main__":
    main()
