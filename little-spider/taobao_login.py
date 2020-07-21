# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec


class TaobaoInfo:
    url = 'https://login.taobao.com/member/login.jhtml'

    def __init__(self, chrome_path, username, password):
        options = webdriver.ChromeOptions
        options.add_experimental_option("prefs",
                                        {"profile.managed_default_content_settings.images": 2})  # 不加载图片, 加快访问速度
        options.add_experimental_option('excludeSwitches',
                                        ['enable-automation'])  # 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
        self.browser = webdriver.Chrome(executable_path=chrome_path)
        self.username = username
        self.password = password
        self.wait = WebDriverWait(self.browser, 10)  # timeout 10s

    # 登录淘宝
    def login(self):
        # 打开网页
        self.browser.get(self.url)

        # 等待 密码登录选项 出现
        password_login = self.wait.until(
            Ec.presence_of_element_located((By.CSS_SELECTOR, '.qrcode-login > .login-links > .forget-pwd')))
        password_login.click()

        # 等待 微博登录选项 出现
        weibo_login = self.wait.until(Ec.presence_of_element_located((By.CSS_SELECTOR, '.weibo-login')))
        weibo_login.click()

        # 等待 微博账号 出现
        weibo_user = self.wait.until(Ec.presence_of_element_located((By.CSS_SELECTOR, '.username > .W_input')))
        weibo_user.send_keys(self.username)

        # 等待 微博密码 出现
        weibo_pwd = self.wait.until(Ec.presence_of_element_located((By.CSS_SELECTOR, '.password > .W_input')))
        weibo_pwd.send_keys(self.username)

        # 等待 登录按钮 出现
        submit = self.wait.until(Ec.presence_of_element_located((By.CSS_SELECTOR, '.btn_tip > a > span')))
        submit.click()

        # 直到获取到淘宝会员昵称才能确定是登录成功
        taobao_name = self.wait.until(Ec.presence_of_element_located((By.CSS_SELECTOR,
                                                                      '.site-nav-bd > ul.site-nav-bd-l > '
                                                                      'li#J_SiteNavLogin > div.site-nav-menu-hd > '
                                                                      'div.site-nav-user > a.site-nav-login-info-nick '
                                                                      '')))
        # 输出淘宝昵称
        print(taobao_name.text)


if __name__ == '__main__':
    taobao = TaobaoInfo('', '', '')
    taobao.login()
