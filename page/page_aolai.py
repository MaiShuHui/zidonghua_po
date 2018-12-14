import page
from base.base import Base

#登录百年奥莱
class PageAolai(Base):
    #点击我
    def page_click_wo(self):
        self.base_click(page.al_wo)

    # 点击去登录
    def page_click_qu(self):
        self.base_click(page.al_qu)

    # 输入账号
    def page_input_number(self,number):
        self.base_input(page.al_number,number)

    # 输入密码
    def page_input_password(self,password):
        self.base_input(page.al_password,password)

    #点击登录
    def page_click_btn(self):
        self.base_click(page.al_btn)


