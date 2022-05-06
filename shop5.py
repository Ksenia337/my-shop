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
book = driver.find_element_by_xpath("//ul[@class='products masonry-done']/li[4]/a[2]")
book.click()
time.sleep(3)
check1 = driver.find_element_by_class_name("cartcontents")
check1_get_text = check1.text
assert "1 Item" in check1_get_text
check2 = driver.find_element_by_xpath("//a[@class='wpmenucart-contents']//span[2]")
check2_get_text = check2.text
assert "₹180.00" in check2_get_text
check1.click()
check3 = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.XPATH, "//tr[@class='cart-subtotal']//span"), "₹180.00"))
check4 = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.XPATH, "//tr[@class='order-total']//span"), "₹189.00"))
driver.quit()