# from base.box import Base, Info
#
# info = Info()
# cap = {'platformName': 'Android'}
# cap['platformVersion'] = info.get_platform_version()
# cap['deviceName'] = info.get_device_name()
# apk_path = r'apkpath\wangyiyun.apk'
# apk_info = info.get_package_and_activity(apk_path)
# info.install_app(apk_path)
# info.clear_app(apk_info[0])
# driver = Base(cap)
# driver.implicitly_wait(50)
# driver.open_app(*apk_info)
# driver.get_element('t,同意').click()
# driver.sleep(5)
# driver.get_element('i,com.netease.cloudmusic:id/agreeCheckbox').click()
# driver.get_element('t,立即体验').click()
#
# # driver.keyevent(4)
#
# driver.get_element('x,//android.widget.TextView[@content-desc="搜索"]').click()
#
# driver.get_element('i,com.netease.cloudmusic:id/search_src_text').send_keys('灵笼')
#
# driver.sleep(3)
#
# driver.keyevent(66)
#
# driver.get_element('x,/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.ImageView[2]').click()
#
# driver.get_element('x,/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[4]').click()
#
# driver.sleep(3)
#
#
# result = driver.get_elements('r,com.netease.cloudmusic:id/commentContent')
# com.netease.cloudmusic:id/commentContent
# com.netease.cloudmusic:id/tv_content
#
#
# for i in result:
#     print(i.text)
#

print(153//100)
print(153%10)
print((153%100//10)**3)