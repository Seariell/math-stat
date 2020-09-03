# homework lesson: 2, task: 1
"""
Вероятность того, что стрелок попадет в мишень, выстрелив один раз, равна 0.8.
Стрелок выстрелил 100 раз. Найдите вероятность того, что стрелок попадет в цель ровно 85 раз.
"""


from hw1.task_1 import combinations


def bernul(k: int, n: int, p: float) -> float:
    """
    Сalculation of probability using the Bernoulli formula

    :param k: int
    :param n: int
    :param p: float
    :return: float
    """
    q = 1 - p
    return combinations(k, n) * (p ** k) * (q ** (n - k))


if __name__ == '__main__':
    # Вероятность попадания высока, используем формулу Бернулли:
    p_shooter = 0.8
    n_of_shoots = 100
    n_of_hits = 85
    p_85 = bernul(n_of_hits, n_of_shoots, p_shooter)

    # Результат = 4.81%
    print(f'{p_85 * 100:.2f}%')
