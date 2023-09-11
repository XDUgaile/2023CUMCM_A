import pandas as pd

# 读取Excel文件
df = pd.read_excel(r"C:\Users\path\Desktop\测试1.xlsx")

# 设置阈值
# threshold_value = 1811.5942  # 你可以替换为你需要的阈值
threshold_value = 2000

# 从Excel文件中获取物品的价值和xy坐标
values = df['eta'].tolist()  # 请替换'价值列名'为你的数据集中的价值列名称
xy_coordinates = df[['x', 'y']].values.tolist()  # 假设xy坐标列名为'x'和'y'

# 根据价值从高到低排序
sorted_items = sorted(enumerate(values), key=lambda x: x[1], reverse=True)

# 寻找选择的物品序号和对应的xy坐标
selected_items = []
selected_coordinates = []
current_value = 0
for item in sorted_items:
    item_index, item_value = item
    if current_value + item_value <= threshold_value:
        selected_items.append(item_index)
        current_value += item_value
        selected_coordinates.append(xy_coordinates[item_index])

# 创建一个包含选定坐标和eta的新数据框
selected_df = pd.DataFrame(selected_coordinates, columns=['x', 'y'])
selected_df['eta'] = [values[i] for i in selected_items]

# 保存新数据框到Excel文件
selected_df.to_excel(r"C:\Users\path\Desktop\666选定坐标与eta.xlsx", index=False)

print("选定的坐标和对应的eta已保存到 Excel 文件。")

print("选择的物品序号：", selected_items)
# print("对应的xy坐标：", selected_coordinates)
# print(selected_items,selected_coordinates)
