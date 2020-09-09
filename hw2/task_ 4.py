# homework lesson: 2, task: 4
"""
В первом ящике находится 10 мячей, из которых 7 - белые.
Во втором ящике - 11 мячей, из которых 9 белых.
Из каждого ящика вытаскивают случайным образом по два мяча.
Какова вероятность того, что все мячи белые?
Какова вероятность того, что ровно два мяча белые?
Какова вероятность того, что хотя бы один мяч белый?
"""


from hw1.task_1 import combinations


balls_1 = 10
b1_white = 7
balls_2 = 11
b2_white = 9

# Вероятность того, что все мячи белые = 30.55%
all_white_b1 = combinations(2, b1_white) / combinations(2, balls_1)
all_white_b2 = combinations(2, b2_white) / combinations(2, balls_2)
all_white = all_white_b1 * all_white_b2
print(f'{all_white*100:.2f}%')

# Вероятность того, что хотя бы один мяч белый = 99.88%
none_white_b1 = combinations(2, balls_1 - b1_white) / combinations(2, balls_1)
none_white_b2 = combinations(2, balls_2 - b2_white) / combinations(2, balls_2)
none_white = none_white_b1 * none_white_b2
print(f'{(1 - none_white)*100:.2f}%')

# Два белых только из первой = 0.85%
only_b1_white = all_white_b1 * none_white_b2
print(f'{only_b1_white*100:.2f}%')

# Два белых только из второй = 4.36%
only_b2_white = all_white_b2 * none_white_b1
print(f'{only_b2_white*100:.2f}%')

# По одному белому из каждой = 15.27%
one_white_b1 = (b1_white / balls_1) * (balls_1 - b1_white) / (balls_1 - 1)
one_white_b1 += (balls_1 - b1_white) / balls_1 * b1_white / (balls_1 - 1)
one_white_b2 = (b2_white / balls_2) * (balls_2 - b2_white) / (balls_2 - 1)
one_white_b2 += (balls_2 - b2_white) / balls_2 * b2_white / (balls_2 - 1)
one_white_of_each = one_white_b1 * one_white_b2
print(f'{one_white_of_each*100:.2f}%')

# Вероятность того, что ровно два мяча белые = 20.48%
two_white = only_b1_white + only_b2_white + one_white_of_each
print(f'{two_white*100:.2f}%')
