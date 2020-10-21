from selenium import webdriver
import time

#字串前面的r是轉譯字符
driver=webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver")
time.sleep(1) #強制等待
driver.get("https://tixcraft.com/")
time.sleep(1)
#找到查詢鈕
login=driver.find_elements_by_class_name("login-notice visible-desktop")
time.sleep(1)
#點擊
login.click()
driver.close()
