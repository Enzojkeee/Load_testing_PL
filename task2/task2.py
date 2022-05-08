import math
import sys


def position_of_the_point(x_circle, y_circle, r_circle, x, y):
    # Вычисляем длинну отрезка от центра окружности до заданных координат
    d = math.sqrt((x_circle - x) ** 2 + (y_circle - y) ** 2)
    if d > r_circle:
        return 2
    elif d == r_circle:
        return 0
    elif d < r_circle:
        return 1


def read_file(file_name):
    a = []
    with open(f"{file_name}", "r") as f:
        for line in f:
            a.append([float(x) for x in line.split()])
    return a


if __name__ == "__main__":
    # Считываем входные данные
    circle_arr = read_file(sys.argv[1])
    point_arr = read_file(sys.argv[2])

    if len(circle_arr[0]) == 2 and len(circle_arr[1]) == 1:
        # Координаты окружности
        x_circle = circle_arr[0][0]
        y_circle = circle_arr[0][1]
        r_circle = circle_arr[1][0]
        for i in range(len(point_arr)):
            if len(point_arr[i]) == 2 and len(point_arr) >= 1 and len(point_arr) <= 100:
                # Координаты точек
                x = point_arr[i][0]
                y = point_arr[i][1]
                print(position_of_the_point(x_circle, y_circle, r_circle, x, y))
            else:
                print("Ошибка входных данных точки")
    else:
        print("Ошибка входных данных окружность ")
