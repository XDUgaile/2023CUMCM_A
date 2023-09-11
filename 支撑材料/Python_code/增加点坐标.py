import math


def generate_points_on_circle(radius, num_points):
    points = []
    angle_interval = 360 / num_points

    for i in range(num_points):
        angle = i * angle_interval
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        points.append((x, y))

    return points


# 初始半径和点的数量
initial_radius = 108
initial_num_points = 62

# 外部循环，控制半径和点的数量的增加
for _ in range(43):  # 5轮循环，可以根据需要调整
    points = generate_points_on_circle(initial_radius, initial_num_points)

    # 输出点的坐标
    for point in points:
        print(point)

    # 增加半径和点的数量
    initial_radius += 12
    initial_num_points += 6
