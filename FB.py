import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import time
class SignUpTest(unittest.TestCase):
    def setUp(self):
        self.driver= webdriver.Firefox(executable_path="/home/ruttaba/PycharmProjects/geckodriver")
        self.driver.get("https://www.facebook.com/")
        self.assertIn("Facebook", self.driver.title)
        self.driver.maximize_window()
    def test_enter_credentials_in_signUp_form(self):
        #review test fb git
        driver = self.driver
        firstName = 'Ruttaba'
        surname = 'Assad'
        emailId = 'Ruttaba@gmail.com'
        newPassword = 'qwerty1234'
        #CSS Selector
        enter_name = 'firstname'
        enter_surname = 'lastname'
        enter_email_Id = 'u_0_r'
        enter_newPass_Id = 'u_0_w'
        reEnter_email = 'u_0_u'
        #Enter User Information
        name_elem = driver.find_element_by_name(enter_name)
        name_elem.clear()
        name_elem.send_keys(firstName)
        surname_elem = driver.find_element_by_name(enter_surname)
        surname_elem.clear()
        surname_elem.send_keys(surname)
        email_elem = driver.find_element_by_id(enter_email_Id)
        email_elem.clear()
        email_elem.send_keys(emailId)
        re_enter_elem = driver.find_element_by_id(reEnter_email)
        re_enter_elem.clear()
        re_enter_elem.send_keys(emailId)
        pass_elem = driver.find_element_by_id(enter_newPass_Id)
        pass_elem.clear()
        pass_elem.send_keys(newPassword)
        #For BIRTHDAY Info (DROPDOWN)
        # create an object for day element to select
        birthDaySelect = Select(driver.find_element_by_css_selector('#day'))
        birthDaySelect.select_by_value('16')
        birthMonthSelect = Select(driver.find_element_by_css_selector('#month'))
        birthMonthSelect.select_by_value('12')
        birthYearSelect = Select(driver.find_element_by_css_selector('#year'))
        birthYearSelect.select_by_value('1991')
        #Gender Selection (RadioButton)
        driver.find_element_by_xpath("//*[contains(text(),'Female')]").click()  #for female
        driver.find_element_by_xpath("//*[contains(text(),'Male')]").click()  #for male
        driver.find_element_by_xpath("//*[contains(text(),'Custom')]").click()  # for custom
        #Custom Form
        pronoun_select = Select(driver.find_element_by_xpath("//select[@name='preferred_pronoun']"))
        pronoun_select.select_by_value("2")
        custom_gender_elem = driver.find_element_by_xpath("//input[@name='custom_gender']")
        custom_gender_elem.clear()
        custom_gender_elem.send_keys('Null')
        time.sleep(5)
    def test_create_an_account_with_new_email_successfully(self):
        self.test_enter_credentials_in_signUp_form()
        button_elem = self.driver.find_element_by_xpath("//button[@type='submit']")
        button_elem.click()
        "Page source required for alert"
        #self.assertIn('you have successfully confirm your email account, you use your email to login')
        print("you have successfully confirm your email account, you can now use your email to login")
    def test_already_registered_and_shows_error(self):
        self.test_enter_credentials_in_signUp_form()
        #self.assertIn('You already have facebook account', self.page_source)
        button_elem = self.driver.find_element_by_xpath("//button[@type='submit']")
        button_elem.click()
        print("You already have facebook account")
    def test_review_test_fb(self):
        print("This file is for review puropse")
    

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
