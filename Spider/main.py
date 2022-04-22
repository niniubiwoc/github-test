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
    sum = 0
    with open('account.txt', 'a') as f1:
        f1.write("\n#Start")
    while True:
        browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)
        if sum == 5:
            break
        try:
            username = ''.join(random.sample(string.ascii_letters, 10)).lower()
            browser.implicitly_wait(20)
            browser.get('http://mail.moekid.com/')
            browser.find_element(By.CSS_SELECTOR,"a#customShortid").click()
            browser.find_element(By.CSS_SELECTOR,"input#shortid").clear()
            browser.find_element(By.CSS_SELECTOR,"input#shortid").send_keys(username)
            browser.find_element(By.CSS_SELECTOR,"a#customShortid").click()
            browser.refresh()
            browser.execute_script('window.open("https://signup.heroku.com/");')
            handles = browser.window_handles
            browser.switch_to.window(handles[1])
            browser.find_element(By.NAME, "first_name").send_keys(''.join(random.sample(string.ascii_letters, 10)).upper())
            browser.find_element(By.NAME, "last_name").send_keys(''.join(random.sample(string.ascii_letters, 10)).upper())
            browser.find_element(By.NAME, "email").send_keys(username + "@mail.moekid.com")
            Select(browser.find_element(By.NAME, "role")).select_by_value("professional_developer")
            Select(browser.find_element(By.NAME, "self_declared_country")).select_by_value("United States")
            Select(browser.find_element(By.NAME, "main_programming_language")).select_by_value("go")
            html = str(browser.page_source.encode('utf-8'))
            datasitekey = getmidstring(html, "https://www.google.com/recaptcha/api2/anchor?ar=1&amp;k=", "&")
            print(datasitekey)
            getrandomdata = requests.get(
                "https://2captcha.com/in.php?key=5d9e13e461a60a913a107ad3e82c5719&method=userrecaptcha&googlekey={0}&pageurl=https://signup.heroku.com/&json=1".format(
                    datasitekey))
            print(getrandomdata.text)
            randomdata = getmidstring(getrandomdata.text, "request\":\"", "\"}")
            print(randomdata)
            getdataurl = "https://2captcha.com/res.php?key=5d9e13e461a60a913a107ad3e82c5719&action=get&id={0}&json=1".format(
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
                browser.find_element(By.ID,"onetrust-accept-btn-handler").click()
            except:
                pass
            browser.find_element(By.CSS_SELECTOR,
                                 "body > div.wrapper > div > div.signup-content > div.signup.page-sidebar > form > div:nth-child(14) > input").click()
            browser.switch_to.window(handles[0])
            browser.find_element(By.CSS_SELECTOR,"#epostalar > ul > li.mail.active > a > div.baslik").click()
            html = str(browser.page_source.encode('utf-8'))
            signup = getmidstring(html,"<a href=\"https://id.heroku.com/account/accept/","\"")
            signup = "https://id.heroku.com/account/accept/"+signup
            browser.get(signup)
            browser.find_element(By.ID,"user_password").send_keys("*Z8Y^ZUlW")
            browser.find_element(By.ID,"user_password_confirmation").send_keys("*Z8Y^ZUlW")
            browser.find_element(By.CSS_SELECTOR,"body > div.wrapper > div > div.account-content > div > form > div:nth-child(8) > input").click()
            browser.find_element(By.CSS_SELECTOR,"#final_login > div > input").click()
            browser.find_element(By.CSS_SELECTOR,"#ember15").click()
            a = []
            for i in range(1,6):
                tmp = ''.join(random.sample(string.ascii_letters, 16)).lower()
                browser.get("https://dashboard.heroku.com/new?template=https://github.com/niniubiwoc/azure-d")
                browser.find_element(By.CSS_SELECTOR,"#ember25").send_keys(tmp)
                html = str(browser.page_source.encode('utf-8'))
                emb = pregetmidstring(html.find("<div class=\"template-deploy\">")+len("<div class=\"template-deploy\">"),html,"<button id=\"","\"")
                browser.find_element(By.ID,emb).click()
                while True:
                    html = str(browser.page_source.encode('utf-8'))
                    if html.find("Your app was successfully deployed.") != -1:
                        break
                requests.get("http://119.28.43.199/nmsl.php?getgetget=https://%s.herokuapp.com/" % tmp)
                sum = sum + 1
            browser.quit()
        except:
            browser.quit()
