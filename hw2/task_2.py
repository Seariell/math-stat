# homework lesson: 2, task: 2
"""
Вероятность того, что лампочка перегорит в течение первого дня эксплуатации, равна 0.0004.
В жилом комплексе после ремонта в один день включили 5000 новых лампочек.
Какова вероятность, что ни одна из них не перегорит в первый день?
Какова вероятность, что перегорят ровно две?
"""


from math import factorial
from math import exp


def puasson(m: int, n: int, p: float) -> float:
    """
    Calculation of probability using the Poisson formula
    :param m: int
    :param n: int
    :param p: float
    :return: float
    """
    lmbda = p * n
    return lmbda ** m / factorial(m) * exp(-lmbda)


if __name__ == '__main__':
    # Вероятность мала, число испытаний большое, нужна формула Пуассона.
    burnout_0 = 0
    burnout_2 = 2
    switches = 5000
    prob_of_burnout = 0.0004
    # Вероятность, что ни одна из них не перегорит в первый день = 13.53%
    p_0 = puasson(burnout_0, switches, prob_of_burnout)
    print(f'{p_0 * 100:.2f}%')

    # Вероятность, что перегорят ровно две = 27.07%
    p_2 = puasson(burnout_2, switches, prob_of_burnout)
    print(f'{p_2*100:.2f}%')
