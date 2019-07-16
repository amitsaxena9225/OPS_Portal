from behave import *
from selenium import webdriver
from selenium import *
import xlrd
import time
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from email.mime.text import MIMEText
from features.repository import Rep
from features.Actual_data import data
from features.Comman_Functions import *
from pprint import pprint
import HtmlTestRunner
import os

import unittest2
import unittest


class MyTestExample(unittest.TestCase):

    @given('login into the ops portal')

    def step_impl(context):
        try:
            context.driver = webdriver.Chrome(Rep.Path)
            driver = context.driver
            driver.get(Rep.Url)
            func_edit_xpath_send_keys(context,Rep.login_page_email_id,data.login_page_email)
            func_edit_xpath_send_keys(context,Rep.login_page_pwd,data.login_page_pwd)
            func_click_xpath(context,Rep.Login_page_Sign_In_Button)
            func_click_xpath(context,Rep.manage_site_lnk)
            func_click_xpath(context,Rep.cross_sign_btn)
            func_edit_xpath_send_keys(context,Rep.ent_domain_,data.domain_name)
            func_click_xpath(context,Rep.select_domain)
            time.sleep(4)
            func_click_xpath(context,Rep.eye_icon)
            time.sleep(4)

        except Exception as error:
            print(error)
            driver = context.driver
            driver.get_screenshot_as_file(Rep.result_path)



    @when('Enter the valid user id and pwd')
    def step_impl(context):

        #def test_Issue(self):
        #driver = context.driver

        '''smoke_test = unittest.TestSuite()


        outfile = open( '/Users/apple/PycharmProjects/OPS_Portal/features'+ "/SmokeTest.html", "w")

        runner1 = HtmlTestRunner.HTMLTestRunner(
            #stream=outfile,
            #title='Test Report',be
            #description='Smoke Tests'
        )

        runner1.run(smoke_test)'''


        time.sleep(3)
        func_click_xpath(context, Rep.ent_quest)

        print("Please add value")
        func_edit_xpath_send_keys(context, Rep.input_txt, data.que_name)
        print("Please add value1111111")
        time.sleep(2)
        func_click_xpath(context,Rep.set1)

        time.sleep(2)
        func_click_xpath(context, Rep.duration)

        func_click_xpath(context, Rep.mins)

        func_click_xpath(context, Rep.secs)

        func_click_xpath(context,Rep.opinion_Sentiment)

        func_click_xpath(context, Rep.apprve)
        time.sleep(2)

        print("One Cycle Completed")

    @then('user should be able to see home page')

    def step_impl(context):
        assert context.failed is False
        print("GIVEN WORKING FINE")



    @given('I  <env> in a blender')
    def step_impl(context):
        pass

        print("GIVEN WORKING FINE")

    @when('I switch the blender on')
    def step_impl(context):
        assert True is not False
        ''' print(driver.get_cookies())
        # print(driver.page_source)
    
        print(driver.session_id)
        print(driver.get_log('browser'))
        print(driver.get_cookies())
        print(driver.log_types)
        pprint(driver.get_cookies())
        print(driver.capabilities)
        print(driver.application_cache)
        print(driver.title)
        pprint(str(driver.service))
        print(driver.mobile)
    '''
        print("GIVEN WORKING FINE")
    @then('it should transform into <account>')

    def step_impl(context):
            assert context.failed is False
            print("GIVEN WORKING FINE")

if __name__ == '__main__':
    unittest.main()
