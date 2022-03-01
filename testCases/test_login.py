import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage
from utilities.customLogger import LogGeneration
from utilities.readProperties import ReadConfig


class Test_001_LoginAndVerify():

    baseURL = ReadConfig.get_application_url()
    username = ReadConfig.get_application_username()
    password = ReadConfig.get_application_password()

    # logger = LogGeneration.get_log_login()
    logger = LogGeneration.custom_logger()
    def test_login_page_check(self,setup):

        self.logger.info("*************** TEST 001 ***************")
        self.logger.info("Verifying Home Page")
        # self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("Home Page test is PASSED")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_pageTitle.png")
            self.driver.close()
            self.logger.error("Home Page test is FAILED")
            assert False

    def test_login_function(self,setup):

        self.logger.info("Verifying Logging functionality")
        # self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        actual_title = self.driver.title
        self.driver.close()
        if actual_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("Login Test is PASSED")
        else:
            self.logger.error("Login Test is FAILED")
            assert False