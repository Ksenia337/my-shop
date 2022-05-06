import time
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
shop = driver.find_element_by_xpath("//li[@id='menu-item-40']/a")
shop.click()
driver.execute_script("window.scrollBy(0, 300);")
book1 = driver.find_element_by_xpath("//ul[@class='products masonry-done']/li[4]/a[2]")
book1.click()
time.sleep(3)
driver.execute_script("window.scrollBy(0, 300);")
book2 = driver.find_element_by_xpath("//ul[@class='products masonry-done']/li[5]/a[2]")
book2.click()
cart = driver.find_element_by_class_name("cartcontents")
cart.click()
time.sleep(1)
remove = driver.find_element_by_xpath("//table[@class='shop_table shop_table_responsive cart']//tr[@class='cart_item']//a")
remove.click()
time.sleep(1)
undo = driver.find_element_by_xpath("//div[@class='woocommerce-message']//a")
undo.click()
quan = driver.find_element_by_xpath("//table[@class='shop_table shop_table_responsive cart']//tr[1]//input")
quan.clear()
time.sleep(1)
quan.send_keys("3")
update = driver.find_element_by_name("update_cart")
update.click()
check = quan.get_attribute("value")
assert  check == "3"
time.sleep(1)
coupon = driver.find_element_by_xpath("//td[@class='actions']//input[2]")
coupon.click()
time.sleep(1)
check2 = driver.find_element_by_xpath("//ul[@class='woocommerce-error']/li")
check2_get_text = check2.text
assert "Please enter a coupon code." in check2_get_text
driver.quit()