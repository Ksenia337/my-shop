import time
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.support.select import Select
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
myacc = driver.find_element_by_xpath("//li[@id='menu-item-50']/a")
myacc.click()
mail = driver.find_element_by_id("reg_email")
mail.send_keys("mail123@mail.ru")
password = driver.find_element_by_id("reg_password")
password.send_keys("Abcabc123abc!!!abc**")
reg = driver.find_element_by_name("register")
reg.click()
time.sleep(5)
driver.quit()