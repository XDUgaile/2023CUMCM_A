import numpy as np
import pandas as pd

# 读取数据
dataset1 = pd.read_csv(r"C:\Users\path\Desktop\余弦效率.csv")
dataset2 = pd.read_excel(r"C:\Users\path\Desktop\8084.xlsx")
z = 4
H = 88
avg = 0
r_x_values = dataset2.iloc[0:, 0].values
r_y_values = dataset2.iloc[0:, 1].values
# 存储余弦效率的列表
cosine_efficiencies = []

# 遍历sina_values和cosr_values
for i in range(12):  # 从0到11遍历
    sina_values = dataset1.iloc[i, 0:5].values
    cosr_values = dataset1.iloc[i, 6:11].values

    # 遍历r_x_values和r_y_values
    for r_x, r_y in zip(r_x_values, r_y_values):
        # 计算定日镜到吸热器中心点的反射光线单位向量
        r = np.array([-r_x, -r_y, H - z]) / np.sqrt(r_x ** 2 + r_y ** 2 + (H - z) ** 2)

        for sina, cosr in zip(sina_values, cosr_values):
            sina = float(sina)
            cosr = float(cosr)
            s = np.array([-np.sqrt(1 - sina * sina) * np.sqrt(1 - cosr * cosr),
                          -np.sqrt(1 - sina * sina) * cosr,
                          -sina])

            # 计算余弦效率
            cosine_efficiency = abs(np.sqrt((1 - np.dot(s, r))/ 2 ))
            cosine_efficiencies.append(cosine_efficiency)

# 打印余弦效率列表
for i, cosine_efficiency in enumerate(cosine_efficiencies, start=1):
    print(cosine_efficiency)

# 创建一个DataFrame来存储余弦效率数据
data = {'余弦效率': cosine_efficiencies}
df = pd.DataFrame(data)

# 将DataFrame保存到Excel文件
df.to_excel(r"C:\Users\path\Desktop\余弦效率结果8084.xlsx", index=False)
