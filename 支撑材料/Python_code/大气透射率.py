import numpy as np
import pandas as pd

# 读取Excel文件
dataset = pd.read_excel(r"C:\Users\path\Desktop\CUMCM2023Problems\CUMCM2023Problems\A题\附件.xlsx")

# 提取数据列
x_values = dataset.iloc[0:1746, 0].values
y_values = dataset.iloc[0:1746, 1].values
z_values = dataset.iloc[0:1746, 2].values


# 目标点坐标
target_point = np.array([0, 0, 84])

# 计算距离
distances = []

for x, y, z in zip(x_values, y_values, z_values):
    point = np.array([x, y, z])
    distance = np.linalg.norm(point - target_point)
    # distances.append(distance)
    # print(distance)
    at = 0.99321 - 0.0001176 * distance+1.97*10e-8*distance*distance
    print(at)
# # 将结果添加到数据集中
# dataset['距离'] = distances
#
# # 打印或保存计算结果
# print(dataset)

# 如果需要保存结果到新的Excel文件
# dataset.to_excel("结果文件路径.xlsx", index=False)
