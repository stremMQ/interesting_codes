import random
from random import choice

def id_create():
    spis = list("АВЕКМНОРСТУХ")
    number = list(range(10))
    reg = list("⁰¹²³⁴⁵⁶⁷⁸⁹")
    print(choice(spis).lower() + str(choice(number)) + str(choice(number)) + str(choice(number)) + choice(spis).lower() + choice(spis).lower() + choice(reg) + choice(reg))
    a = input()
    if a == '':
        id_create()

if __name__ == '__main__':
    id_create()