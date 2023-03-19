from ddt import ddt, data, unpack
from base.box import Info, Base
import unittest


@ddt
class TTLogin(unittest.TestCase):
    user_data = [('15333606956', '420151175')]
    info = Info()
    cap = {}
    cap['platformName'] = 'Android'
    cap['platformVersion'] = info.get_platform_version()
    cap['deviceName'] = info.get_device_name()
    apk_path = r'apkpath\toutiao359.apk'
    apk_info = info.get_package_and_activity(apk_path)
    info.clear_app(apk_info[0])

    @classmethod
    def setUpClass(self):
        self.info.install_app(self.apk_path)
        pass

    @classmethod
    def tearDownClass(self):
        self.info.uninstall_app(self.apk_info[0])

    def setUp(self):
        self.driver = Base(self.cap)
        self.driver.open_app(*self.apk_info)
        self.driver.sleep(2)

    def tearDown(self):
        self.driver.close()

    @data(*user_data)
    @unpack
    def test_login(self, user, password):
        while True:
            try:
                self.driver.get_element('t,申请独家号').click()
                break
            except:
                self.driver.swipe('l')
                self.driver.sleep(2)
        self.driver.get_element('i,io.manong.developerdaily:id/login_btn').click()
        self.driver.sleep(2)
        self.driver.get_element('t,密码登录').click()
        self.driver.sleep(2)
        self.driver.get_element('i,io.manong.developerdaily:id/edt_phone').send_keys(user)
        self.driver.get_element('i,io.manong.developerdaily:id/edt_password').send_keys(password)
        self.driver.get_element('i,io.manong.developerdaily:id/btn_login').click()
        self.driver.sleep(1)
        result = self.driver.get_element('r,io.manong.developerdaily:id/nav_tv_name').text
        self.assertEqual('u571511', result, msg='登录失败')
