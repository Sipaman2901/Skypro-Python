def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 15 == 0:  # Проверка делимости на 3 и 5 (15 = НОК 3 и 5)
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


n = int(input("Введите число n: "))
fizz_buzz(n)
