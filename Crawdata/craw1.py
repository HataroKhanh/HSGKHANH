from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("--disable-gpu")
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)

link = "https://www.1sttheworld.com/collections/leather-tote-bag-collection/products/ireland-quirke-or-o-quirke-irish-family-crest-leather-tote-bag-pretty-green-plaid-irish-shamrock-a7?variant=1000011278869692"

driver.get(link)

# Wait for the element to be present on the page
class_name = "VueCarousel-slide"
img_tag = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, class_name)))

# Extract the src attribute from the img tag
src_attribute = img_tag.find_element(By.TAG_NAME, 'img').get_attribute('src')

print(src_attribute)

driver.quit()
