from base.get_driver import get_driver
from page.page_aolai import PageAolai
from page.page_login import PageLogin
from page.page_setting import PageSetting


class PageIn():


    # 艾克
    def page_get_login(self):
        driver = get_driver("com.vcooline.aike",".umanager.LoginActivity")
        return PageLogin(driver)

    # 百年奥莱
    def page_get_aolai(self):
        driver = get_driver("com.yunmall.lc","com.yunmall.ymctoc.ui.activity.MainActivity")
        return PageAolai(driver)

    #设置页面
    def page_get_shezhi(self):
        return PageSetting(get_driver())