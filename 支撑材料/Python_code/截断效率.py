import pandas as pd
import numpy as np
from scipy.integrate import nquad

# 读取Excel文件，假设数据存储在Sheet1中
excel_file = r"C:\Users\path\Desktop\deg.xlsx"
df = pd.read_excel(excel_file, sheet_name="Sheet1")
avg = 0
# 定义积分的被积函数
def integrand(x, y, sigma):
    return np.exp(-(x**2 + y**2) / (2 * sigma**2))

# 循环处理每一组数据
for index, row in df.iterrows():
    phi_1 = row['phi_1']  # 替换'phi_1'为Excel文件中的实际列名
    theta_1 = row['theta_1']  # 替换'theta_1'为Excel文件中的实际列名
    phi_2 = row['phi_14']  # 替换'phi_2'为Excel文件中的实际列名
    theta_2 = row['theta_14']  # 替换'theta_2'为Excel文件中的实际列名
    sigma = 0.26

    # 定义积分范围（根据限制条件）
    R = np.sqrt(49/np.pi)
    x_min = -4
    x_max = 4
    y_min = -R * np.cos(phi_1) * np.cos(theta_2 - theta_1) * np.cos(np.pi/2 - phi_2 - theta_1)
    y_max = R * np.cos(phi_1) * np.cos(theta_2 - theta_1) * np.cos(np.pi/2 - phi_2 - theta_1)

    # 执行二重积分计算
    result, _ = nquad(integrand, [[x_min, x_max], [y_min, y_max]], args=(sigma,))

    # 计算 eta
    eta = 1 / (2 * np.pi * sigma**2) * result

    eta = np.abs(eta)
    avg += eta
    # 输出结果
    print(f"Result for Row {index+1}: {eta}")
avg = avg/1745/5
print(avg)