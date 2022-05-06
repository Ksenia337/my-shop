import time
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
book = driver.find_element_by_xpath("//ul[@class='products masonry-done']/li[1]//img")
book.click()
oldprice = driver.find_element_by_xpath("//div[@class='summary entry-summary']//span[1]")
oldprice_get_text = oldprice.text
assert "600" in oldprice_get_text
newprice = driver.find_element_by_xpath("//div[@class='summary entry-summary']//ins/span")
newprice_get_text = newprice.text
assert "450" in newprice_get_text
image_btn = driver.find_element_by_class_name("attachment-shop_single.size-shop_single.wp-post-image")
image_btn.click()
image = WebDriverWait(driver, 10).until(
EC.invisibility_of_element_located((By.ID, "fullResImage")))
close = WebDriverWait(driver, 5).until(
EC.invisibility_of_element_located((By.CLASS_NAME, "pp_close")))
time.sleep(5)
close_btn = driver.find_element_by_class_name("pp_close")
close_btn.click()
driver.quit()