from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Настройка параметров Chrome
chrome_options = Options()
chrome_options.add_argument("--log-level=3")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

# Создаем сервис и драйвер
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Устанавливаем явное ожидание
    wait = WebDriverWait(driver, 10)

    # Открываем страницу
    driver.get("http://uitestingplayground.com/dynamicid")

    # Ждем появления синей кнопки и кликаем (игнорируя динамический ID)
    blue_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, '//button[contains(@class, "btn-primary")]')
        )
    )
    blue_button.click()

    print("✅ Скрипт успешно выполнен. Кнопка с динамическим ID нажата.")

except Exception as e:
    print(f"❌ Произошла ошибка: {e}")

finally:
    # Закрываем браузер
    driver.quit()
