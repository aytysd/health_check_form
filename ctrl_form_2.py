import time
from selenium import webdriver
import pyautogui

class Health_check:
    def __init__(self, step_number):
        driver_path = r'C:\python\Lib\site-packages\chromedriver_binary\chromedriver.exe'
        driver =webdriver.Chrome(driver_path)
        driver.get('https://login.microsoftonline.com/common/oauth2/authorize?response_mode=form_post&response_type=id_token+code&scope=openid&msafed=0&nonce=4891191f-7684-4f58-bb04-79dfb5ee3261.637520956469031810&state=https%3a%2f%2fforms.office.com%2fPages%2fResponsePage.aspx%3fid%3dXYP-cpVeEkWK4KezivJfyAF57WIGdqVMh4kFMucIpIVUQjgyV1NORDdEMUxUWkZMVVZNS1lRRjhONS4u&client_id=c9a559d2-7aab-4f13-a6ed-e7e9c52aec87&redirect_uri=https%3a%2f%2fforms.office.com%2fauth%2fsignin&sso_reload=true')

health_check = Health_Check(3)
