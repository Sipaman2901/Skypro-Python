from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

# Создаем сервис и драйвер для Firefox
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

try:
    # Переходим на страницу
    driver.get("http://the-internet.herokuapp.com/inputs")

    # Находим поле ввода
    input_field = driver.find_element(By.TAG_NAME, "input")

    # Вводим текст "Sky"
    input_field.send_keys("Sky")

    # Очищаем поле
    input_field.clear()

    # Вводим текст "Pro"
    input_field.send_keys("Pro")

    print("✅ Скрипт успешно выполнен")

except Exception as e:
    print(f"❌ Произошла ошибка: {e}")

finally:
    # Закрываем браузер
    driver.quit()
