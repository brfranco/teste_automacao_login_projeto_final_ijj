from selenium import webdriver

def before_all(context):
    context.driver = webdriver.Firefox()

def after_all(context):
    context.driver.quit()

def before_scenario(context, scenario):
    context.driver.delete_all_cookies()

def after_scenario(context, scenario):
    context.driver.delete_all_cookies()