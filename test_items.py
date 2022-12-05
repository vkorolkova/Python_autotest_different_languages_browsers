# Использую вариант с find_elements, чтобы поймать ошибку через assert, 
# как это сказано в задании.
# Если бы эта функциональность была не нужна, использовала бы find_element
# Если использовать find_element, до assert дела доходить не будет,
# будет выбрасывааться исключение NoSuchElementException.

# Задание реализовано для работы в разных браузерах Chrome (по умолчанию) и Firefox

from selenium.webdriver.common.by import By
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"



def test_basket_button_exist(browser):
    browser.implicitly_wait(5)
    browser.get(link)
    button = browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert len(button) > 0, 'button not found'
    time.sleep(30)
    
