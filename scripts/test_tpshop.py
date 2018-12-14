import os
import sys
sys.path.append(os.getcwd())

import pytest
from time import sleep
from base.get_driver_tpshop import get_driver_tpshop
from page.page_tpshop import PageTpshop


class TestTpshop():

    def setup_class(self):
        self.tpshop = PageTpshop(get_driver_tpshop())

    def teardown_class(self):
        self.tpshop.driver.quit()

    @pytest.mark.parametrize("number,password,verify",[("13826920169","6666666","8888")])
    def test_tpshop(self,number,password,verify):
        sleep(3)
        self.tpshop.page_click_login()
        sleep(3)
        self.tpshop.page_input_number(number)
        sleep(3)
        self.tpshop.page_input_password(password)
        sleep(3)
        self.tpshop.page_input_verify(verify)
        sleep(3)
        self.tpshop.page_click_btn()
        sleep(3)


