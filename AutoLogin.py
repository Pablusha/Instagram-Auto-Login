from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import LoginInfo

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.instagram.com/")

login = browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[2]/p/a")
login.click()
time.sleep(3)

username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")

username.send_keys(LoginInfo.username)
password.send_keys(LoginInfo.password)

loginButton = browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[4]/button")
loginButton.click()

time.sleep(10)
browser.close()