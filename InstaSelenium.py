# not working for profile page n followers list


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, urllib.request
import requests
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# to keep page open
from selenium.webdriver.chrome.options import Options

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


# chrome_options.add_argument(r"--user-data-dir=C:\Users\Vidhi\AppData\Local\Google\Chrome\User Data\Default")
# chrome_options.add_argument = ('user-data-dir'='C:\Users\Vidhi\AppData\Local\Google\Chrome\User Data\Default')
chrome_options.add_argument(r"--user-data-dir=C:\Users\Vidhi\AppData\Local\Google\Chrome\User Data")
chrome_options.add_argument(r"--profile-directory=Default")
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.instagram.com/")

# to login
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
username = driver.find_elements(By.XPATH,"/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input")[0]
# password = driver.find_element("input[name='password']")


username.clear()
password.clear()
username.send_keys("artly.v")
password.send_keys("Taehyung")

Login_button = WebDriverWait(driver, 2).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
# login = driver.find_element("button[type='submit']").click()

# for save info n notification
not_now = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Save Info")]'))).click()
time.sleep(3)
not_now2 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()


# click on profile page
driver.get("https://www.instagram.com/artly.v")
driver.get("https://www.instagram.com/artly.v/followers")
# <button class="_acan _aiit _acap _aijb _acas _aj1-" type="button">Save Info</button>
# copy the xpath of scrollbar
# scroll_box = driver.find_elements(By.XPATH, '//*[@id="mount_0_0_wv"]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
# driver.find_element_by_link_text("/artly.v/")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# driver.find_element("//a[contains(href, '/{}')]".format(username)).click()
# Page=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mount_0_0_Lo"]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[6]/div/div'))).click

# Follower=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mount_0_0_t9"]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div'))).click


# <li class=" x6s0dn4 x78zum5 xvs91rp xl56j7k x2b8uid x1ltjmfc x2pgyrj x4tmyev">…</li>flex
# <a class="x1i10hfl" href="/artly.v/followers/?next=%2F" role="link" tabindex="0">

# Search = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "//input[placeholder='Search']"))).click
# Search.clear()
# keyword = "thv"
# Search.send_keys(keyword)
# time.sleep(5)
# Search.send_keys(Keys.ENTER)
# time.sleep(5)
# Search.send_keys(Keys.ENTER)
# # <input aria-label="Search input" autocapitalize="none" class="_aauy" placeholder="Search" type="text" value>
# time.sleep(5)
#
