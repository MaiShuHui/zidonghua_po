import allure
import pytest


class TestAllure():

    @allure.step("新增步骤")
    def test_allure_01(self):
        allure.attach("描述:","我是新增步骤")
        print("01被执行")

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    @allure.step("修改步骤")
    def test_allure_02(self):
        allure.attach("描述:我是修改步骤", "")
        print("02被执行")

    @allure.step("查询步骤")
    def test_allure_03(self):
        print("03被执行")
        assert 0

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step("删除步骤")
    def test_allure_04(self):
        print("04被执行")