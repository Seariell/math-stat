# homework lesson: 1, task: 1
"""
Из колоды в 52 карты извлекаются случайным образом 4 карты.
a) Найти вероятность того, что все карты – крести.
б) Найти вероятность, что среди 4-х карт окажется ХОТЯ БЫ один туз.
"""

from math import factorial


def combinations(k: int, n: int) -> int:
    """
    Calculates the number of combinations from k in n

    :param n: int
    :param k: int
    :return: int
    """
    return int(factorial(n)/(factorial(k)*factorial(n - k)))


if __name__ == '__main__':
    # Общее число наборов по 4 карты из 52:
    num = combinations(4, 52)

    # Из них число наборов из одной масти:
    clubs = combinations(4, 13)

    # Вероятность того, что все карты крести:
    p_clubs = clubs / num

    # Число наборов с тузами:
    aces = 0
    for i in range(1, 5):
        aces += combinations(i, 4) * combinations(4 - i, 48)

    # Вероятность появления набора с тузами:
    p_aces = aces / num

    print(f'Вероятность того, что все карты крести = {p_clubs * 100 :.2f}%')
    print(f'Вероятность того, что среди 4-х карт окажется ХОТЯ БЫ один туз = {p_aces * 100 :.2f}%')
