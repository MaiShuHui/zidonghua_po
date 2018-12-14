import page
from base.base import Base


class PageTpshop(Base):

    def page_click_login(self):
        self.base_click(page.tp_login)

    def page_input_number(self,number):
        self.base_input(page.tp_number,number)

    def page_input_password(self,password):
        self.base_input(page.tp_password,password)

    def page_input_verify(self,verify):
        self.base_input(page.tp_verify,verify)

    def page_click_btn(self):
        self.base_click(page.tp_btn)