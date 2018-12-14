from selenium.webdriver.support.wait import WebDriverWait


class Base():
    # 初始化
    def __init__(self,driver):
        self.driver = driver
    # 查找元素方法
    def base_find(self,loc,timeout =30,poll=0.5):
        return WebDriverWait(self.driver,timeout,poll_frequency=poll).until(lambda x:x.find_element(*loc))
    #点击方法
    def base_click(self,loc):
        el = self.base_find(loc)
        el.click()
    #输入元素方法
    def base_input(self,loc,value):
        el = self.base_find(loc)
        el.clear()
        el.send_keys(value)










class Base02():

    def __init__(self):
        self.driver = driver

    def base_find_element(self,log,tim=30,poll=0.5):
        return WebDriverWait(self.driver,timeout=tim,poll_frequency=poll).until(lambda x:x.find.element(*log))

    def base_click(self,log):
        self.base_find_element(log).click()

    def base_input(self,log,value):
        element = self.base_find_element(log)
        element.clear()
        element.send_keys(value)