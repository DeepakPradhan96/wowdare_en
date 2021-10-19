from selenium.webdriver import Chrome
from selenium import webdriver
#context= global/use entair project

def before_all(context):
    path='C:\\Driver\\chromedriver_win32\\chromedriver.exe'
    context.driver =Chrome(executable_path=path)

    Path="C:\Users\deepaak\PycharmProjects\Wowdare_en\Feature\Driver\geckodriver.exe"
    context.driver2=webdriver.Firefox(executable_path=Path)


def after_all(context):
    context.driver.close()
    context.driver2.quit()