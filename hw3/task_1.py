# homework lesson: 3, task: 1
"""
Даны значения зарплат из выборки выпускников:
100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150.
Посчитать (желательно без использования статистических методов наподобие std, var, mean)
среднее арифметическое, среднее квадратичное отклонение, смещенную и несмещенную оценки дисперсий для данной выборки.
"""


def math_exp(sample):
    return sum(sample)/len(sample)


def mean_sq(sample):
    result = 0
    for itm in sample:
        result += (itm - math_exp(sample))**2
    result /= len(sample) - 1
    return result


def dispersion_offset(sample):
    result = 0
    for itm in sample:
        result += (itm - math_exp(sample))**2
    result /= len(sample)
    return result**0.5


def dispersion(sample):
    return mean_sq(sample)**0.5


salary = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]
print(f'Оценка математического ожидания ожидания (среднее арифметическое) = {math_exp(salary)}%')
print(f'Среднее квадратичное отклонение = {mean_sq(salary):.2f}%')
print(f'Смещенная оценка дисперсии = {dispersion_offset(salary):.2f}%')
print(f'Несмещенная оценка дисперсии = {dispersion(salary):.2f}%')
