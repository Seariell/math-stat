# homework lesson: 3, task: 3
"""
На соревновании по биатлону один из трех спортсменов стреляет и попадает в мишень.
Вероятность попадания для первого спортсмена равна 0.9, для второго — 0.8, для третьего — 0.6.
Найти вероятность того, что выстрел произведен:
a). первым спортсменом
б). вторым спортсменом
в). третьим спортсменом.
"""


def bayes(p_b, p_a_b, p_a):
    return p_b * p_a_b / p_a


if __name__ == '__main__':
    sport_1, sport_2, sport_3 = 0.9, 0.8, 0.6

    # Вероятность попадания в мишень одним из спортсменов:
    p_hit = sport_1 / 3 + sport_2 / 3 + sport_3 / 3
    print(f'Вероятность попадания в мишень одним из спортсменов = {p_hit*100:.2f}%')

    # Вероятность попадания в мишень первым спортсменом:
    p_sport_1 = bayes(1/3, sport_1, p_hit)
    print(f'Вероятность попадания в мишень первым спортсменом = {p_sport_1*100:.2f}%')

    # Вероятность попадания в мишень вторым спортсменом:
    p_sport_2 = bayes(1/3, sport_2, p_hit)
    print(f'Вероятность попадания в мишень вторым спортсменом = {p_sport_2*100:.2f}%')

    # Вероятность попадания в мишень третьим спортсменом:
    p_sport_3 = bayes(1/3, sport_3, p_hit)
    print(f'Вероятность попадания в мишень третьим спортсменом = {p_sport_3*100:.2f}%')