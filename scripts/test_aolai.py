import os
import sys
sys.path.append(os.getcwd())

import pytest

from base.get_driver import get_driver
from page.page_aolai import PageAolai


class TestAolai():

    def setup_class(self):
        self.aolai = PageAolai(get_driver("com.yunmall.lc","com.yunmall.ymctoc.ui.activity.MainActivity"))

    def teardown_class(self):
        self.aolai.driver.quit()

    @pytest.mark.parametrize("number,password",[("13826920169","6666666")])
    def test_aolai(self,number,password):
        self.aolai.page_click_wo()
        self.aolai.page_click_qu()
        self.aolai.page_input_number(number)
        self.aolai.page_input_password(password)
        self.aolai.page_click_btn()