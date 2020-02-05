import unittest
from selenium import webdriver
import time
from Pages.home_page import Home_Page
from Pages.login_page import Login_Page
import HtmlTestRunner

class login_test(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        print("hellooooo")

    def test_login(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        
        login = Login_Page(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()
        

        homepage = Home_Page(driver)  
        homepage.click_welcome
        homepage.click_logout

    @classmethod
    def tearDownClass(cls):
        print("ready to shut down")
        cls.driver.close()
        print("closed")
        cls.driver.quit()
        print("Quit")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/zanba/OneDrive/Desktop/Project/Page Object Model/Reports"))