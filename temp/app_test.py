import time
from appium import webdriver
from selenium.webdriver.common.by import By

cap = {}
cap['platformName'] = 'Android'
cap['platformVersion'] = '5.1.1'
cap['deviceName'] = '127.0.0.1:62001 device'

user = '15333606956'
password = '420151175'

user_id = 'io.manong.developerdaily:id/edt_phone'
password_id = 'io.manong.developerdaily:id/edt_password'
pwd_login = 'io.manong.developerdaily:id/btn_login'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', cap)
driver.current_window_handle
package = 'io.manong.developerdaily'
# activity = 'io.toutiao.android.ui.activity.LaunchActivity'
activity = 'io.toutiao.android.ui.activity.MainActivity'
xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[5]'
driver.start_activity(package, activity)
time.sleep(2)
driver.find_element(By.XPATH, xpath).click()
#
driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
time.sleep(2)
#
driver.find_element(By.ID, 'io.manong.developerdaily:id/login_btn').click()
time.sleep(2)
driver.find_element_by_android_uiautomator('new UiSelector().text("密码登录")').click()
time.sleep(2)
driver.find_element(By.ID, user_id).send_keys(user)
driver.find_element(By.ID, password_id).send_keys(password)
driver.find_element(By.ID, pwd_login).click()
