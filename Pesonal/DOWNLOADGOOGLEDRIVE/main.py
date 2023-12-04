from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
options = Options()
# Đường dẫn đến ChromeDriver
s = Service('/sbin/chromedriver')

# Khởi tạo WebDriver với Service
driver = webdriver.Chrome(service=s)

driver.get('https://drive.google.com/drive/folders/1Ml-_t0pT1TBaeLbzcqgmQnPLgbXB4Yvn')
username = driver.find_element(By.ID, 'username_field_id')
password = driver.find_element(By.ID, 'password_field_id')
