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
logout = driver.find_element_by_xpath("//nav[@class='woocommerce-MyAccount-navigation']//li[6]/a")
logout_get_text = logout.text
assert "Logout" in logout_get_text
driver.quit()