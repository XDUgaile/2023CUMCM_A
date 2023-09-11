import csv


# 从CSV文件中读取数据
def read_csv_file(file_path):
    data = []
    with open(file_path, mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row:  # 跳过空行
                data.append(row[0])  # 假设数据在CSV文件的第一列
    return data


# 输出每个数据值12次
def output_data_multiple_times(data, num_times):
    for value in data:
        for _ in range(num_times):
            print(value)


if __name__ == "__main__":
    file_path = r"C:\Users\path\Desktop\新建 XLSX 工作表.csv"  # 替换为你的CSV文件路径
    data = read_csv_file(file_path)
    output_data_multiple_times(data, 5)

