import os
import sys
sys.path.append(os.getcwd())

from base.read_aike import ReadAike
import pytest
from page.page_in import PageIn

def get_data():
    list=[]
    datas = ReadAike("data_aike.yaml").read_aike()
    for data in datas.values():
        list.append((data.get("username"),data.get("password")))
    return list

class TestAike():

    def setup_class(self):
        self.aike = PageIn().page_get_login()

    def teardown_class(self):
        self.aike.driver.quit()

    @pytest.mark.parametrize("username,password",get_data())
    def test_aike(self,username,password):
        self.aike.page_number(username)
        self.aike.page_password(password)
        self.aike.page_enter()
