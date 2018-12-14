import page
from base.base import Base


class PageLogin(Base):
    #输入账号
    def page_number(self,number):
        self.base_input(page.log_number, number)
    #输入密码
    def page_password(self,password):
        self.base_input(page.log_password,password)
    #点击登录
    def page_enter(self):
        self.base_click(page.log_enter)