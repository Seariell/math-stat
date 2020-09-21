std = 16
n = 256
m = 80
z_half_alfa = 1.96
interval = z_half_alfa * (std / (n**0.5))

print(f'Доверительный интервал = {m} ± {interval}')
1