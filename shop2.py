import time
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.support.select import Select
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
myacc = driver.find_element_by_xpath("//li[@id='menu-item-50']/a")
myacc.click()
mail = driver.find_element_by_id("username")
mail.send_keys("mail123@mail.ru")
password = driver.find_element_by_id("password")
password.send_keys("Abcabc123abc!!!abc**")
log = driver.find_element_by_name("login")
log.click()
shop = driver.find_element_by_xpath("//li[@id='menu-item-40']/a")
shop.click()
html_btn = driver.find_element_by_xpath("//li[@class='cat-item cat-item-19']/a")
html_btn.click()
checkcount = driver.find_element_by_xpath("//li[@class='cat-item cat-item-19 current-cat']/span")
checkcount_get_text = checkcount.text
assert "3" in checkcount_get_text
driver.quit()