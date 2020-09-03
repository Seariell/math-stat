# homework lesson: 2, task: 3
"""
Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?
"""


from hw2.task_1 import bernul


throw = 144
eagle = 70
prob_of_eagle = 0.5

# Вероятность, что орел выпадет ровно 70 раз = 6.28%
p_70 = bernul(eagle, throw, prob_of_eagle)
print(f'{p_70*100:.2f}%')
