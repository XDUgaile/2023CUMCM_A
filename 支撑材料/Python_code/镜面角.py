import numpy as np
import pandas as pd
import math

dataset1 = pd.read_excel(r"F:\QQ_file\定日镜两角.xlsx")
dataset2 = pd.read_excel(r"C:\Users\path\Desktop\CUMCM2023Problems\CUMCM2023Problems\A题\余弦效率.xlsx")
phi1_values = dataset1.iloc[0:1746, 4].values
theta1_values = dataset1.iloc[0:1746, 7].values

# 输入值
phi3 = dataset2.iloc[24:29, 12].values
theta3 = dataset2.iloc[31:36, 12].values

for phi1, theta1 in zip(phi1_values, theta1_values):
    phi1 = float(phi1)
    theta1 = float(theta1)

    # 计算第一个公式
    phi3 = phi3.astype(float)  # 将phi3和theta3转换为浮点数类型
    theta3 = theta3.astype(float)
    numerator = np.cos(phi1) * np.sin(theta1) + np.cos(phi3) * np.sin(theta3)
    denominator = np.cos(phi1) * np.cos(theta1) + np.cos(phi3) * np.cos(theta3)
    tan_theta2 = numerator / denominator

    # print("phi1 =", phi1)
    # print("theta1 =", theta1)
    # print("tan(theta2) =", tan_theta2)
 # 计算反三角函数并转换为角度
    theta2_rad = np.arctan(tan_theta2)
    theta2_deg = np.degrees(theta2_rad)
    # print(theta2_deg)

 # 高度角与上面得出的方位角互余
    phi2_deg = 90 - theta2_deg
    print(phi2_deg)