from base.box import Base, Info


class TTLogin:
    info = Info()
    cap = {}
    cap['platformName'] = 'Android'
    cap['platformVersion'] = info.get_platform_version()
    cap['deviceName'] = info.get_device_name()
    apk_path = r'..\apkpath\smon_603.apk'
    apk_info = info.get_package_and_activity(apk_path)
    info.clear_app(apk_info[0])

    def tou_tiao_login(self, user, password):
        driver = Base(self.cap)
        driver.open_app(*self.apk_info)
        while True:
            try:
                driver.get_element('t,申请独家号').click()
                break
            except:
                driver.swipe('l')
                driver.sleep(2)
        driver.get_element('i,io.manong.developerdaily:id/login_btn').click()
        driver.sleep(2)
        driver.get_element('t,密码登录').click()
        driver.sleep(2)
        driver.get_element('i,io.manong.developerdaily:id/edt_phone').send_keys(user)
        driver.get_element('i,io.manong.developerdaily:id/edt_password').send_keys(password)
        driver.get_element('i,io.manong.developerdaily:id/btn_login').click()

if __name__ == '__main__':
    login = TTLogin()
    login.tou_tiao_login('15333606956', '420151175')