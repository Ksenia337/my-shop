import time
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.support.select import Select
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0, 600);")
rm_btn = driver.find_element_by_xpath("//div[@id='text-22-sub_row_1-0-2-0-0']//a")
rm_btn.click()
reviews = driver.find_element_by_xpath("//li[@class='reviews_tab']/a")
reviews.click()
driver.execute_script("window.scrollBy(0, 400);")
stars = driver.find_element_by_xpath("//p[@class='stars']//a[5]")
stars.click()
comment = driver.find_element_by_id("comment")
comment.send_keys("Nice book!")
name = driver.find_element_by_id("author")
name.send_keys("Abc")
mail = driver.find_element_by_id("email")
mail.send_keys("mail123@mail.ru")
submit = driver.find_element_by_class_name("submit")
submit.click()
driver.quit()