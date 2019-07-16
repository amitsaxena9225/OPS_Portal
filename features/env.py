
from selenium import webdriver

import behave_webdriver


def before_all(context):
    context.behave_driver = behave_webdriver.Chrome.headless()


def after_all(context):
    pass

    #context.browser.quit()


def before_feature(context, feature):
    context.config.setup_logging()
    #pass
    context.init(environment='test')

#from allure_behave.hooks import allure_report

### your code

#allure_report("/Users/apple/PycharmProjects/OPS_Portal/%allure_result_folder%")