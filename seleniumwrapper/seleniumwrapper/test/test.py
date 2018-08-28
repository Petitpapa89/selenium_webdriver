import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://www.google.com")

time.sleep(2)

search_box = driver.find_element_by_name('q')

search_box.send_keys('chance the rapper')

search_box.submit()

time.sleep(2)

driver.quit()