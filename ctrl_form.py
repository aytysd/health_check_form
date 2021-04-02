import time
from selenium import webdriver
import pyautogui



driver_path = r'C:\python\Lib\site-packages\chromedriver_binary\chromedriver.exe'
driver =webdriver.Chrome(driver_path)
driver.get('https://login.microsoftonline.com/common/oauth2/authorize?response_mode=form_post&response_type=id_token+code&scope=openid&msafed=0&nonce=4891191f-7684-4f58-bb04-79dfb5ee3261.637520956469031810&state=https%3a%2f%2fforms.office.com%2fPages%2fResponsePage.aspx%3fid%3dXYP-cpVeEkWK4KezivJfyAF57WIGdqVMh4kFMucIpIVUQjgyV1NORDdEMUxUWkZMVVZNS1lRRjhONS4u&client_id=c9a559d2-7aab-4f13-a6ed-e7e9c52aec87&redirect_uri=https%3a%2f%2fforms.office.com%2fauth%2fsignin&sso_reload=true')



search = driver.find_element_by_name("loginfmt")
#.click()
search.send_keys('I10795@nara.kosen-ac.jp')
#search.submit()
#search.find_element_by_id('idSIButton9').click()
pyautogui.press('enter')

time.sleep(3)

search_2 = driver.find_element_by_name('passwd')

search_2.send_keys('AYTysd/0926')

time.sleep(1)

pyautogui.press('enter')

yes_no = driver.find_element_by_id('idBtn_Back')



pyautogui.press('enter')

reload = driver.refresh()


select = driver.find_element_by_id('SelectId_0_placeholder').click()

for i in range(0,1):
    pyautogui.press('down')
pyautogui.press('enter')

select_2 = driver.find_element_by_id('SelectId_1_placeholder').click()

for i in range(0,17):
    pyautogui.press('down')
pyautogui.press('enter')

""" select_3 = driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div[3]/div/div[2]/div/div/input').click()

pyautogui.write('40')
 """

select_4 = driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[3]/div/div[2]/div/div[3]/div').click()
#select_5 = driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div[5]/div/div[2]/div/div[4]/div/label/input').click()

time.sleep(3)

#driver.quit()