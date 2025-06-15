def is_year_leap(year):
    """Проверяет, является ли год високосным."""
    if year % 4 == 0:
        return True
    else:
        return False


# Вызываем функцию с примером года (2024) и сохраняем результат
year = 2024
result = is_year_leap(year)

# Выводим результат в формате "год <номер года>: <True|False>"
print(f"год {year}: {result}")
