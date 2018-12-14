import page
from base.base import Base


class PageSetting(Base):

    def page_click_shousuo(self):
        self.base_click(page.set_shousuo)

    def page_input(self,shuru):
        self.base_input(page.set_shuru, shuru)

    def page_click_fanhui(self):
        self.base_click(page.set_fanhui)