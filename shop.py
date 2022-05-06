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
book = driver.find_element_by_xpath("//ul[@class='products masonry-done']/li[3]/a")
book.click()
bookname = driver.find_element_by_class_name("product_title.entry-title")
bookname_get_text = bookname.text
assert "HTML5 Forms" in bookname_get_text
driver.quit()