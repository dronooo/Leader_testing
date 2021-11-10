import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://yandex.ru/")
mail_btm = driver.find_element_by_xpath("//div[text()='Почта']").click()
window_login = driver.window_handles[1]
driver.switch_to.window(window_login)
login = driver.find_element_by_css_selector("span>input")
login.send_keys("leadertesting@yandex.ru")
login_btn = driver.find_element_by_css_selector("[id='passp:sign-in']").click()
time.sleep(1)
password = driver.find_element_by_css_selector("span>input")
password.send_keys("lead1234test")
login_btn = driver.find_element_by_css_selector("[id='passp:sign-in']").click()
time.sleep(3)
driver.quit()