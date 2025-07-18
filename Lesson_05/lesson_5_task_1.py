from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Настройка параметров Chrome для подавления лишних сообщений
chrome_options = Options()
# Устанавливаем уровень логирования только на FATAL ошибки
chrome_options.add_argument("--log-level=3")
# Отключаем логирование
chrome_options.add_argument("--disable-logging")
# Отключаем сообщения DevTools
chrome_options.add_experimental_option(
    'excludeSwitches',
    ['enable-logging']
)

# Создаем сервис и драйвер
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(
    service=service,
    options=chrome_options
)

try:
    # Устанавливаем явное ожидание
    wait = WebDriverWait(driver, 10)

    # Открываем страницу
    driver.get("http://uitestingplayground.com/classattr")

    # Ждем появления синей кнопки и кликаем
    blue_button = wait.until(
        EC.element_to_be_clickable(
            (By.CLASS_NAME, "btn-primary")
        )
    )
    blue_button.click()

    # Обрабатываем всплывающее окно, если оно появится
    try:
        alert = wait.until(EC.alert_is_present())
        alert.accept()
    except Exception:
        # Если алерт не появился, продолжаем выполнение
        pass

    print("✅ Скрипт успешно выполнен")

except Exception as e:
    print(f"❌ Произошла ошибка: {e}")

finally:
    # Закрываем браузер
    driver.quit()
