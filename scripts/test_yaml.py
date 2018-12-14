import os
import sys
sys.path.append(os.getcwd())

import pytest
from page.page_in import PageIn
from base.read_yaml import ReadYaml, get_data


def get_data():
    datas = ReadYaml("data_login.yaml").read_yaml()
    run = []
    for data in datas.values():
        run.append((data.get("number"),data.get("password")))
    return run


class TestYaml():

    def setup_class(self):
        self.yaml = PageIn().page_get_login()

    def teardown_class(self):
        self.yaml.driver.quit()

    @pytest.mark.parametrize("number,password",get_data())
    def test_yaml(self,number,password):
        self.yaml.page_number(number)
        self.yaml.page_password(password)
        self.yaml.page_enter()

