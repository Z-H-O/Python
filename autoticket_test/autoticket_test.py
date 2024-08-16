#导入所需要的必要库
import time
import selenium
import requests
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# heasder = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
# }
class auto_login_cookie():
    #保存cookie
    def save_cookies():
        with open('autoticket_test\\Cookies', 'w') as f:
            f.write(json.dumps(browser.get_cookies()))

    #加载cookie
    def load_cookies():
        with open('autoticket_test\\Cookies', 'r') as f:
            cookies = json.loads(f.read())
        return cookies

    #加入cookie
    def cookies_login(cookies:list):
        for cookie in cookies:
            browser.add_cookie(cookie)
        
    
    def login():
        #输入账号
        username=browser.find_element(By.ID,'phoneNumInput')
        username.send_keys('18813179751')
        #输入密码
        time.sleep(1)
        browser.find_element(By.ID,'sendCodeBtnText').click()
        code=input('请输入验证码：')
        password=browser.find_element(By.ID,'codeInput')
        password.send_keys(code)
        #同意协议
        browser.find_element(By.XPATH,'//*[@id="iloginUserConfirm"]/i').click()
        time.sleep(1)
        #登录按钮
        browser.find_element(By.XPATH,'//*[@id="iloginBtn"]').click()

if __name__ == '__main__':
    
    #登录网页
    browser = webdriver.Chrome()
    #browser.add_cookie(cookie_dict)
    browser.get('https://passport.maoyan.com/login')
    time.sleep(100)
    auto_login_cookie.save_cookies()
    browser.quit()



