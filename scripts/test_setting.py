import os
import sys
sys.path.append(os.getcwd())

import pytest

from base.get_driver import get_driver
from page.page_setting import PageSetting


class TestSetting():

    def setup_class(self):
        self.setting = PageSetting(get_driver())

    def teardown_class(self):
        self.setting.driver.quit()

    @pytest.mark.parametrize("number",["白菜"])
    def test_setting(self,number):
        self.setting.page_click_shousuo()
        self.setting.page_input(number)
        self.setting.page_click_fanhui()
