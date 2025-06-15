def square(side):

    area = side ** 2
    if not isinstance(side, int):
        # Ручное округление вверх:
        # Если есть дробная часть, увеличиваем на 1
        area = int(area) + (1 if area > int(area) else 0)
    return area


# Ввод стороны квадрата от пользователя
side_input = input("Введите длину стороны квадрата: ")
side = float(side_input)  # Преобразуем в число

# Вычисление площади
area = square(side)

# Вывод результата
print(f"Площадь квадрата со стороной {side} равна {area}")
