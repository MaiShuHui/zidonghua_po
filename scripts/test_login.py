import os
import sys
sys.path.append(os.getcwd())

import pytest

from base.get_driver import get_driver
from page.page_login import PageLogin


class TestLogin():

    def setup_class(self):
        self.login = PageLogin(get_driver("com.vcooline.aike",".umanager.LoginActivity"))

    def teardown_class(self):
        self.login.driver.quit()

    @pytest.mark.parametrize("number,password",[("13826920169","123456")])
    def test_login(self,number,password):
        self.login.page_number(number)
        self.login.page_password(password)
        self.login.page_enter()