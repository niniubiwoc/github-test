import sys

from selenium import webdriver
import string
import time
import random
import requests
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os

options = webdriver.ChromeOptions()
options.add_argument('User-Agent=Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36')
options.add_argument('--incognito')
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
chromedriver = "/usr/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver

def getmidstring(html, start_str, end):
    start = html.find(start_str)
    if start >= 0:
        start += len(start_str)
        end = html.find(end, start)
        if end >= 0:
            return html[start:end].strip()

def pregetmidstring(pre, html, start_str, end):
    start = html.find(start_str, pre)
    if start >= 0:
        start += len(start_str)
        end = html.find(end, start)
        if end >= 0:
            return html[start:end].strip()

if __name__ == '__main__':
    for i in range(100):
        try:
            browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)
            username = ''.join(random.sample(string.ascii_letters, 10)).lower()
            browser.implicitly_wait(20)
            browser.get('http://u.mp3520.cn/')
            browser.find_element(By.CSS_SELECTOR, "a#customShortid").click()
            time.sleep(0.5)
            browser.find_element(By.CSS_SELECTOR, "input#shortid").clear()
            time.sleep(0.5)
            browser.find_element(By.CSS_SELECTOR, "input#shortid").send_keys(username)
            time.sleep(0.5)
            browser.find_element(By.CSS_SELECTOR, "a#customShortid").click()
            browser.execute_script('window.open("https://signup.heroku.com/");')
            handles = browser.window_handles
            browser.switch_to.window(handles[1])
            browser.find_element(By.NAME, "first_name").send_keys(
                ''.join(random.sample(string.ascii_letters, 10)).upper())
            browser.find_element(By.NAME, "last_name").send_keys(
                ''.join(random.sample(string.ascii_letters, 10)).upper())
            browser.find_element(By.NAME, "email").send_keys(username + "@u.mp3520.cn")
            Select(browser.find_element(By.NAME, "role")).select_by_value("professional_developer")
            Select(browser.find_element(By.NAME, "self_declared_country")).select_by_value("United States")
            Select(browser.find_element(By.NAME, "main_programming_language")).select_by_value("go")
            html = str(browser.page_source.encode('utf-8'))
            datasitekey = getmidstring(html, "https://www.google.com/recaptcha/api2/anchor?ar=1&amp;k=", "&")
            print(datasitekey)
            getrandomdata = requests.get(
                "https://2captcha.com/in.php?key=3067ef0088ec380b2e8338f673669476&method=userrecaptcha&googlekey={0}&pageurl=https://signup.heroku.com/&json=1".format(
                    datasitekey))
            print(getrandomdata.text)
            randomdata = getmidstring(getrandomdata.text, "request\":\"", "\"}")
            print(randomdata)
            getdataurl = "https://2captcha.com/res.php?key=3067ef0088ec380b2e8338f673669476&action=get&id={0}&json=1".format(
                randomdata)
            requestdata = ""
            while True:
                result = eval(requests.get(getdataurl).text)
                print(result)
                if result['status'] == 1:
                    requestdata = result['request']
                    break
            browser.execute_script('document.getElementById("g-recaptcha-response").innerHTML="%s";' % requestdata)
            try:
                browser.find_element(By.ID, "onetrust-accept-btn-handler").click()
            except:
                pass
            browser.find_element(By.CSS_SELECTOR,
                                 "body > div.wrapper > div > div.signup-content > div.signup.page-sidebar > form > div:nth-child(14) > input").click()
            browser.switch_to.window(handles[0])
            browser.find_element(By.CSS_SELECTOR, "#epostalar > ul > li.mail.active > a > div.baslik").click()
            html = str(browser.page_source.encode('utf-8'))
            signup = getmidstring(html, "<a href=\"https://id.heroku.com/account/accept/", "\"")
            signup = "https://id.heroku.com/account/accept/" + signup
            browser.get(signup)
            browser.find_element(By.ID, "user_password").send_keys("*Z8Y^ZUlW")
            browser.find_element(By.ID, "user_password_confirmation").send_keys("*Z8Y^ZUlW")
            browser.find_element(By.CSS_SELECTOR,
                                 "body > div.wrapper > div > div.account-content > div > form > div:nth-child(8) > input").click()
            browser.find_element(By.CSS_SELECTOR, "#final_login > div > input").click()
            browser.find_element(By.CSS_SELECTOR, "#ember15").click()
            time.sleep(1)
            browser.get("https://dashboard.heroku.com/account")
            browser.find_element(By.CSS_SELECTOR, "#ember46").click()
            apikey = browser.find_element(By.CSS_SELECTOR, "#ember47").get_attribute("value")
            requests.get("http://119.28.43.199/nmsl.php?getgetget=%s" % apikey)
            browser.quit()
        except:
            browser.quit()
