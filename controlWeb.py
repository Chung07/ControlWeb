from selenium import webdriver
import time

#字串前面的r是轉譯字符
driver=webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver")
time.sleep(1) #強制等待
driver.get("https://www.google.com")
time.sleep(1)
#找到搜尋框
input=driver.find_element_by_name("q")
#在搜尋框輸入hebe
input.send_keys("hebe")
#找到查詢鈕
search=driver.find_element_by_name("btnK")
#點擊
search.click()
htmltext=driver.page_source
driver.close()
