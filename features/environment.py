from selenium import webdriver

def before_all(context):
    context.browser = webdriver.Edge(r"C:\Users\Admin\LBG7-Python-API\webdrivers\msedgedriver.exe")
    context.browser.maximize_window()

def after_all(context):
    context.browser.quit()
    