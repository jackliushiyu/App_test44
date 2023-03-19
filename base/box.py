import os
import time
from appium import webdriver
from selenium.webdriver.common.by import By


class Base:
    def __init__(self, cap: dict, host='localhost', port=4723):
        if 'platformName' in cap:
            self.__driver = webdriver.Remote('http://%s:%d/wd/hub' % (host, port), cap)
        else:
            raise Exception('传入参数不合理')

    def open_app(self, package, activity):
        """
        启动app
        :param package:
        :param activity:
        :return:
        """
        self.__driver.start_activity(package, activity)

    def __convert_selector_to_locator(self, selector):
        selector_key = selector.split(',')[0]
        selector_value = selector.split(',')[1]
        if selector_key in ['i', 'id']:
            locator = (By.ID, selector_value)
        elif selector_key in ['x', 'xpath']:
            locator = (By.XPATH, selector_value)
        else:
            raise Exception("暂时不支持除id和xpath以外的选择器")
        return locator

    def get_element(self, selector):

        if selector.split(',')[0] in ["i", "id"]:
            element = self.__driver.find_element(*self.__convert_selector_to_locator(selector))
        elif selector.split(',')[0] in ["x", "xpath"]:
            element = self.__driver.find_element(*self.__convert_selector_to_locator(selector))
        elif selector.split(',')[0] in ['t', 'text']:
            # 新版本，driver进行了重新封装
            element = self.__driver.find_element('-android uiautomator',
                                                 'new UiSelector().text("%s")' % selector.split(',')[1])
            # 旧版本方法
            # element = self.__driver.find_element_by_android_uiautomator(
            #     'new UiSelector().text("%s")' % selector.split(',')[1])
        elif selector.split(',')[0] in ['c', 'className']:
            element = self.__driver.find_element('-android uiautomator',
                                                 'new UiSelector().className("%s")' % selector.split(',')[1])
            # 旧版本方法
            # element = self.__driver.find_element_by_android_uiautomator(
            #     'new UiSelector().className("%s")' % selector.split(',')[1])
        elif selector.split(',')[0] in ['r', 'resourceId']:
            element = self.__driver.find_element('-android uiautomator',
                                                 'new UiSelector().resourceId("%s")' % selector.split(',')[1])
            # 旧版本方法
            # element = self.__driver.find_element_by_android_uiautomator(
            #     'new UiSelector().resourceId("%s")' % selector.split(',')[1])
        else:
            raise Exception('请输入正确的选择器')
        return element

    def swipe(self, direction):
        size = self.__driver.get_window_size()
        if direction in ['u', 'up']:
            self.__driver.swipe(start_x=int(size['width'] / 2), start_y=int(size['height'] * 0.2),
                                end_x=int(size['width'] / 2), end_y=int(size['height'] * 0.8))
        elif direction in ['d', 'down']:
            self.__driver.swipe(start_x=int(size['width'] / 2), start_y=int(size['height'] * 0.8),
                                end_x=int(size['width'] / 2), end_y=int(size['height'] * 0.2))
        elif direction in ['l', 'left']:
            self.__driver.swipe(start_x=int(size['width'] * 0.8), start_y=int(size['height'] / 2),
                                end_x=int(size['width'] * 0.2), end_y=int(size['height'] / 2))
        elif direction in ['r', 'right']:
            self.__driver.swipe(start_x=int(size['width'] * 0.2), start_y=int(size['height'] / 2),
                                end_x=int(size['width'] * 0.8), end_y=int(size['height'] / 2))
        else:
            raise Exception('请给正确的方向')

    def sleep(self, second):
        time.sleep(second)

    def close(self):
        self.__driver.close_app()

    def keyevent(self, keycode):
        self.__driver.keyevent(keycode)

    def implicitly_wait(self, second):
        self.__driver.implicitly_wait(second)

    def click_screen(self, location):
        """

        :param location: 500 500
        :return:
        """
        os.system('adb shell input tap %s' % location)

    def get_elements(self, selector):
        if selector.split(',')[0] in ["i", "id"]:
            elements = self.__driver.find_elements(*self.__convert_selector_to_locator(selector))
        elif selector.split(',')[0] in ["x", "xpath"]:
            elements = self.__driver.find_elements(*self.__convert_selector_to_locator(selector))
        elif selector.split(',')[0] in ['t', 'text']:
            # 新版本，driver进行了重新封装
            elements = self.__driver.find_element('-android uiautomator',
                                                  'new UiSelector().text("%s")' % selector.split(',')[1])
            # 旧版本方法
            # elements = self.__driver.find_elements_by_android_uiautomator(
            #     'new UiSelector().text("%s")' % selector.split(',')[1])
        elif selector.split(',')[0] in ['c', 'className']:
            elements = self.__driver.find_element('-android uiautomator',
                                                  'new UiSelector().className("%s")' % selector.split(',')[1])
            # 旧版本方法
            # elements = self.__driver.find_elements_by_android_uiautomator(
            #     'new UiSelector().className("%s")' % selector.split(',')[1])
        elif selector.split(',')[0] in ['r', 'resourceId']:
            elements = self.__driver.find_element('-android uiautomator',
                                                  'new UiSelector().resourceId("%s")' % selector.split(',')[1])
            # 旧版本方法
            # elements = self.__driver.find_elements_by_android_uiautomator(
            #     'new UiSelector().resourceId("%s")' % selector.split(',')[1])
        else:
            raise Exception('请输入正确的选择器')
        return elements


class Info:
    def __init__(self):
        """
        确保adb服务启动
        """
        cmd = 'tasklist |findstr adb.exe'
        result = os.popen(cmd)
        adb_info = result.buffer.read().decode(encoding='utf8')
        if 'adb.exe' not in adb_info:
            os.popen('adb start-server')

    def get_platform_version(self):
        """
        获取安卓版本号
        :return:
        """
        l = []
        cmd = 'adb shell getprop ro.build.version.release'
        text = os.popen(cmd)
        for i in text:
            l.append(i.strip())
        return l[0]

    def get_device_name(self):
        """
        获取设备
        :return:
        """
        l = []
        cmd = 'adb devices'
        text = os.popen(cmd)
        for i in text:
            if i.strip().endswith('device'):
                l.append(i.strip())
        return l[0]

    def get_package_and_activity(self, apk_path):
        """
        通过安装包获取包名和activity
        :param apk_path: 安装包路径
        :return: (package,activity)
        """
        cmd_package = 'aapt dumpsys badging %s|findstr package' % apk_path
        cmd_activity = 'aapt dumpsys badging %s|findstr activity' % apk_path
        info_package = os.popen(cmd_package)
        info_activity = os.popen(cmd_activity)
        package = info_package.buffer.read().decode(encoding='utf8').split("'")[1]
        activity = info_activity.buffer.read().decode(encoding='utf8').split("'")[1]
        return package, activity

    def install_app(self, apk_path):
        """
        通过安装包路径安装app
        :param apk_path: 安装包路径
        :return:
        """
        package_name = self.get_package_and_activity(apk_path)[0]
        cmd = 'adb shell pm list packages|findstr %s' % package_name
        text = os.popen(cmd)
        result = text.buffer.read().decode(encoding='utf8')
        if package_name not in result:
            os.popen('adb install %s' % apk_path)
            print('程序安装成功')
        else:
            print('程序已安装')

    def uninstall_app(self, package_name):
        """
        通过包名卸载app
        :param package_name: 包名
        :return:
        """
        cmd = 'adb shell pm list packages|findstr %s' % package_name
        text = os.popen(cmd)
        result = text.buffer.read().decode(encoding='utf8')
        if package_name not in result:
            print('程序未安装')
        else:
            os.popen('adb uninstall %s' % package_name)
            print('程序卸载成功')

    def clear_app(self, package_name):
        """
        按包名清除app数据
        :param package_name: 包名
        :return:
        """
        cmd = 'adb shell pm clear %s' % package_name
        os.popen(cmd)

# info = Info()
# info.get_device_name()
# print(info.get_package_and_activity(r'C:\Users\THINK\Desktop\toutiao359.apk'))
# info.clear_app('io.manong.developerdaily')
# info.install_app(r'C:\Users\THINK\Desktop\toutiao359.apk')
# info.uninstall_app('io.manong.developerdaily')
