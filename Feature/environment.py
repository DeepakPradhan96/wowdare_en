from selenium.webdriver import Chrome
from selenium import webdriver
#context= global/use entair project

def before_all(context):
    path='C:\\Driver\\chromedriver_win32\\chromedriver.exe'
    context.driver =Chrome(executable_path=path)

    context.driver2=webdriver.Firefox()


def after_all(context):
    context.driver.close()
    context.driver2.quit()