#not working for profile page n followers list



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, urllib.request
import requests
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


#to keep page open
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)



driver = webdriver.Chrome()

driver.get("https://www.instagram.com/")

#to login
# username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
username = driver.find_elements(By.XPATH,"/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input")[0]
# password = driver.find_element("input[name='password']")


username.clear()
password.clear()
username.send_keys("artly.v")
password.send_keys("Taehyung")


Login_button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
# login = driver.find_element("button[type='submit']").click()

#for save info n notification
not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
## <button class="_acan _aiit _acao _aija _acas _aj1-" type="button">Not Now</button>
# f = driver.find_elements(By.XPATH, "x6s0dn4 x78zum5 xvs91rp xl56j7k x2b8uid x1ltjmfc x2pgyrj x4tmyev")
# stroy = driver.find_element_by_partial_link_text('').clicl()
#click on profile page
# print(f)


driver.get("https://www.instagram.com/artly.v")
#<li class="x6s0dn4 x78zum5 xvs91rp xl56j7k x2b8uid x1ltjmfc x2pgyrj x4tmyev">flex
# page = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/section/div[3]/div[1]/div/div/div[2]/div[1]/div/div/a"))).click()
# Follower = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(href, '/following')]"))).click()


time.sleep(2)

    # # copy the xpath of scrollbar
    # scroll_box =
# driver.find_element_by_link_text("/artly.v/")
time.sleep(2)


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