import math
import pandas as pd

dataset1 = pd.read_csv(r"C:\Users\path\Desktop\余弦效率.csv")
h = 3.004  # 站点海拔高度，单位km
sina_values = dataset1.iloc[0:12, 0].values

# 计算a、b、c
a = 0.4237 - 0.00821 * (6 - h) ** 2
b = 0.5055 + 0.00595 * (6.5 - h) ** 2
c = 0.2711 + 0.01858 * (2.5 - h) ** 2

# 遍历sina_values并计算DNI
for sina in sina_values:
    sina = float(sina)
    DNI = 1.366 * (a + b * math.exp(-c / sina))
    print(DNI)
