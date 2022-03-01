from pages.login_page import LoginPage
from utilities.customLogger import LogGeneration
from utilities.jsonReader import ReadFromJSON
from utilities.readProperties import ReadConfig

class Test_002_LoginValidUsers():

    baseURL = ReadConfig.get_application_url()
    jsonPath = '.\\TestData\\loginusersmultiple.json'
    logger = LogGeneration.custom_logger()

    def test_multiple_login(self,setup,):

        self.logger.info("*************** TEST 002 ***************")
        self.logger.info("Verifying Logging functionality")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        test_data = ReadFromJSON.get_json_data(self.jsonPath)
        for item in test_data:
            self.username = item['username']
            self.password = item['password']
            self.status = item['status']

            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            # time.sleep(5)
            actual_title = self.driver.title
            expected_title = "Dashboard / nopCommerce administration"

            if actual_title == expected_title:
                if self.status == "Pass":
                    assert True
                    self.logger.info("Test has PASSED for user: "+self.username)
                    self.driver.save_screenshot(".\\Screenshots\\" + "test_loginMultipleUsers.png")
                    self.lp.clickLogout()
                elif self.status == "Fail":
                    self.logger.info("Test has FAILED for user: "+self.username)
                    self.driver.save_screenshot(".\\Screenshots\\" + "test_loginMultipleUsers.png")
                    # self.lp.clickLogout()
                    # assert False
            elif actual_title != expected_title:
                self.logger.info("Test has FAILED for user: "+self.username)
                self.driver.save_screenshot(".\\Screenshots\\" + "test_loginMultipleUsers.png")
                # self.lp.clickLogout()
                # assert False
