import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from utils.constants import (FB_URL, FIRST_NAME, SUR_NAME, EMAIL_ADDRESS, NEW_PASSWORD)

class SignUpForm():
     "This class contains functions"

     def find_element(self, css_selector='')

         if css_selector:
             return self.driver.find_element_by_css_selector(css_selector)

     def clear_value_of_element(self, CSS_SELECTOR):

         element = self.find_element(css_selector=CSS_SELECTOR)
         element.clear()
         return element

     def enter_credentials_in_signUp_form(self, first_name='', last_name='',
                                         email_address='', new_password=''):

        selector_name = 'firstname'
        selector_surname = 'lastname'
        selector_email_id = 'u_0_r'
        selector_password_id = 'u_0_w'
        selector_reenter_id = 'u_0_u'
        if first_name:
        self.clear_value_of_element(CSS_SELECTOR=selector_name).send_keys(first_name)
        if last_name:
        self.clear_value_of_element(CSS_SELECTOR=selector_surname).send_keys(last_name)
        if email_address:
        self.clear_value_of_element(CSS_SELECTOR=selector_email_id).send_keys(email_address)
        if email_address:
        self.clear_value_of_element(CSS_SELECTOR=selector_reenter_id).send_keys(email_address)
        if new_password:
        self.clear_value_of_element(CSS_SELECTOR=selector_password_id).send_keys(new_password)


        birth_day_select = Select(driver.find_element_by_css_selector('#day'))
        birth_day_select.select_by_value('16')
        birth_month_select = Select(driver.find_element_by_css_selector('#month'))
        birth_month_select.select_by_value('12')
        birth_year_select = Select(driver.find_element_by_css_selector('#year'))
        birth_year_select.select_by_value('1991')

        driver.find_element_by_xpath("//*[contains(text(),'Female')]").click()
        driver.find_element_by_xpath("//*[contains(text(),'Male')]").click()
        driver.find_element_by_xpath("//*[contains(text(),'Custom')]").click()

        pronoun_select = Select(driver.find_element_by_xpath("//select[@name='preferred_pronoun']"))
        pronoun_select.select_by_value("2")
        custom_gender_elem = driver.find_element_by_xpath("//input[@name='custom_gender']").send_keys('Null')
        custom_gender_elem.clear()

        time.sleep(5)

    def click_on_sign_up_button(self):

        button_elem = self.driver.find_element_by_xpath("//button[@type='submit']")
        button_elem.click()



class SignUpTest(unittest.TestCase):
    "This class contains test cases"

    def setUp(self):

        self.driver= webdriver.Firefox(executable_path="/home/ruttaba/PycharmProjects/geckodriver")
        self.driver.get(FB_URL)
        self.driver.maximize_window()

    def test_is_title_matches(self):

        self.assertIn("Facebook", self.driver.title)


    #def test_user_fill_form_successfully(self):

     #   self.enter_credentials_in_signUp_form(first_name=FIRST_NAME, last_name=SUR_NAME,
                                              #email_address=EMAIL_ADDRESS, new_password=NEW_PASSWORD)

    def test_create_an_account_with_new_email_successfully(self):

        self.enter_credentials_in_signUp_form(first_name=FIRST_NAME, last_name=SUR_NAME,
                                              email_address=EMAIL_ADDRESS, new_password=NEW_PASSWORD)

        self.click_on_submit_button()
        self.assertIn('you have successfully confirm your email account, you use your email to login')


    def test_already_registered_and_shows_error(self):

        self.enter_credentials_in_signUp_form(first_name=FIRST_NAME, last_name=SUR_NAME,
                                              email_address=EMAIL_ADDRESS, new_password=NEW_PASSWORD)
        self.click_on_submit_button()
        self.assertIn('You already have facebook account')


    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
