def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False


# Вызываем функцию с запросом года и сохраняем результат
year = int(input("Введите год: "))
result = is_year_leap(year)

# Выводим результат в формате "год <номер года>: <True|False>"
print(f"год {year}: {result}")
