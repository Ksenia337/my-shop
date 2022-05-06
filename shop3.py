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
check1 = driver.find_element_by_class_name("orderby")
element_check1 = check1.get_attribute("value")
assert  element_check1 == "menu_order"
price = driver.find_element_by_class_name("orderby")
select = Select(price)
select.select_by_value("price-desc")
check2 = driver.find_element_by_class_name("orderby")
element_check2 = check2.get_attribute("value")
assert  element_check2 == "price-desc"
driver.quit()