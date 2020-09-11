# from base.box import Info, Base
#
# info = Info()
# cap = {}
# cap['platformName'] = 'Android'
# cap['platformVersion'] = info.get_platform_version()
# cap['deviceName'] = info.get_device_name()
# apk_path = r'apkpath\smon_603.apk'
# apk_info = info.get_package_and_activity(apk_path)
# driver = Base(cap)
# driver.open_app(*apk_info)
# driver.implicitly_wait(50)
# # 点击登录界面
# while True:
#     driver.click_screen('500 500')
#     # 进入游戏后停止
#     break
#


t = 0
sum_number = 0
for i in range(4):
    t += 10 ** i
    sum_number += t
print(sum_number)

t2 = ''
sum_number2 = 0
for i in range(4):
    t2 += '1'
    sum_number2 += int(t2)
print(sum_number2)
