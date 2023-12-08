import numpy as np
from itertools import product


def get_adjacent(part):
    (number, (radek, sloupec)), = part.items()
    zacatek = sloupec - 1 if sloupec > 0 else sloupec
    konec = sloupec + len(number) + 1 if sloupec + len(number) < sloupce else sloupec + len(number)

    odkud = radek if radek == 0 else radek - 1
    kam = radek + 2 if radek < radky - 1 else radek + 1
    adj = list(product(range(odkud, kam), range(zacatek, konec)))
    original = tuple((radek, i) for i in range(sloupec, sloupec + len(number)))
    orig = set(original)
    adjacent = [x for x in adj if x not in orig]
    return int(number), adjacent


with open('src/input3.txt', 'r') as source:
    plan = np.array([[j for j in i] for i in source.read().splitlines()])
radky, sloupce = plan.shape
cisla = {}
idx = 0
for radek in range(radky):
    cislo = ''
    for sloupec in range(sloupce):
        if plan[radek, sloupec].isdigit() and (not plan[radek, sloupec - 1].isdigit() or True):
            cislo += plan[radek, sloupec]
            if sloupec + 1 == sloupce or not plan[radek, sloupec + 1].isdigit():
                cisla[idx] = {cislo: tuple([radek, sloupec + 1 - len(cislo)])}
                idx += 1
                cislo = ''

sumA = 0
for k, part in cisla.items():
    number, adjacent = get_adjacent(part)
    if any((plan[i[0], i[1]] != '.' and not plan[i[0], i[1]].isdigit())for i in adjacent):
        sumA += number
print('sumA:', sumA)