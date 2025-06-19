import math


def square(side):
    area = side ** 2
    if not isinstance(side, int):
        area = math.ceil(area)
    return area


# Ввод стороны квадрата от пользователя
side_input = input("Введите длину стороны квадрата: ")
side = float(side_input)  # Преобразуем в число (дробное или целое)

# Вычисление площади
area = square(side)

# Вывод результата
print(f"Площадь квадрата со стороной {side} равна {area}")
