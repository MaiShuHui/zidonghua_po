import os
import sys
sys.path.append(os.getcwd())

from base.read_txt import ReadTxt

import pytest
from page.page_in import PageIn

get = ReadTxt("data.txt")

class TestAike():

    def setup_class(self):
        self.aike = PageIn().page_get_login()

    def teardown_class(self):
        self.aike.driver.quit()

    @pytest.mark.parametrize("username,password",get.read_txt())
    def test_aike(self,username,password):
        self.aike.page_number(username)
        self.aike.page_password(password)
        self.aike.page_enter()
