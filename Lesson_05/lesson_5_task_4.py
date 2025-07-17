from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

# Создаем сервис и драйвер для Firefox
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

try:
    # Переходим на страницу логина
    driver.get("http://the-internet.herokuapp.com/login")

    # Находим и заполняем поле username
    username = driver.find_element(By.ID, "username")
    username.send_keys("MrAnderson")

    # Находим и заполняем поле password
    password = driver.find_element(By.ID, "password")
    password.send_keys("TakeBluePill")

    # Находим и нажимаем кнопку Login
    login_button = driver.find_element(By.CSS_SELECTOR,
                                       "button[type='submit']")
    login_button.click()

    # Находим зеленую плашку и выводим ее текст
    flash_message = driver.find_element(By.ID, "flash")
    message_text = flash_message.text.strip()

    # Выводим только текст без кнопки закрытия [×]
    if message_text.endswith("×"):
        message_text = message_text[:-1].strip()

    print("Текст из зеленой плашки:")
    print(message_text)

    print("✅ Скрипт успешно выполнен")

except Exception as e:
    print(f"❌ Произошла ошибка: {e}")

finally:
    # Закрываем браузер
    driver.quit()
