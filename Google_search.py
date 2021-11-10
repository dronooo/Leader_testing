import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://google.com/")
search = driver.find_element_by_css_selector("input.gLFyf.gsfi")
search.send_keys("купить кофемашину bork c804")
time.sleep(1)
search = driver.find_element_by_css_selector("li.sbct:nth-child(1)").click()
mvideo = driver.find_element_by_partial_link_text('mvideo.ru')
mvideo_text = mvideo.text
assert "mvideo.ru" in mvideo_text
time.sleep(1)
items = driver.find_element_by_xpath("//div[contains(text(), 'Результатов: примерно')]")
items_text = items.text
numbers = ''.join([n for n in items_text if n.isdigit()])[:-3]
print(numbers)
assert int(numbers) > 10
driver.quit()