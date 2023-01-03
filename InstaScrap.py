#doesn't stay open

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)


def login(driver):
    username = "artly.v"
    password = "Taehyung"
    driver.get("https://www.instagram.com/accounts/login/")

    driver.find_element("//div/input[@name='username']").send_keys(username)
    driver.find_element("//div/input[@name='password']").send_keys(password)
    driver.find_element("//span/button").click()

    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.LINK_TEXT, "See All")))


def scrape_followers(driver, account):
    driver.get("https://www.instagram.com/{0}/".format(account))

    driver.find_element_by_partial_link_text("follower").click()

    xpath = "//div[@style='position: relative; z-index: 1;']/div/div[2]/div/div[1]"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))

    xpath = "//div[@style='position: relative; z-index: 1;']//ul/li/div/div/div/div/a"
    followers_elems = driver.find_elements_by_xpath(xpath)

    return [e.text for e in followers_elems]


if __name__ == "__main__":
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        login(driver)
        followers = scrape_followers(driver, "instagram")
        print(followers)
    finally:
        driver.quit()