# homework lesson: 3, task: 2
"""
В первом ящике находится 8 мячей, из которых 5 - белые. Во втором ящике - 12 мячей, из которых 5 белых.
Из первого ящика вытаскивают случайным образом два мяча, из второго - 4.
Какова вероятность того, что 3 мяча белые?
"""


from hw1.task_1 import combinations


box_1, box_1_white = 8, 5
box_2, box_2_white = 12, 5
pull_b1, pull_b2 = 2, 4


# Два белых из первого и 1 белый из второго:
p1 = combinations(pull_b1, box_1_white) / combinations(pull_b1, box_1) * \
     combinations(1, box_2_white) / combinations(1, box_2) * \
     combinations(3, box_2 - box_2_white) / combinations(3, box_2)
print(f'Два белых из первого и 1 белый из второго = {p1*100:.2f}%')
# Один белый из первого и два белых из второго:
p2 = combinations(1, box_1_white) / combinations(1, box_1) * \
     combinations(1, box_1 - box_1_white) / combinations(1, box_1) * \
     combinations(2, box_2_white) / combinations(2, box_2) * \
     combinations(2, box_2 - box_2_white) / combinations(2, box_2)
print(f'Один белый из первого и два белых из второго = {p2*100:.2f}%')
# Три белых из второго:
p3 = combinations(2, box_1 - box_1_white) / combinations(2, box_1) * \
     combinations(3, box_2_white) / combinations(3, box_2) * \
     combinations(1, box_2 - box_2_white) / combinations(1, box_2)
print(f'Три белых из второго = {p3*100:.2f}%')
p = p1 + p2 + p3
print(f'Три белых = {p*100:.2f}%')