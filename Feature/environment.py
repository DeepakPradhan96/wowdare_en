from selenium.webdriver import Chrome
from selenium import webdriver
#context= global/use entair project

def before_all(context):
    path='C:\\Driver\\chromedriver_win32\\chromedriver.exe'
    context.driver2 =Chrome(executable_path=path)

    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_argument("--incognito")
    context.driver = webdriver.Chrome(chrome_options=chrome_option)


    '''Path=".\\Feature\\Driver\\geckodriver.exe"
    context.driver2=webdriver.Firefox(executable_path=Path)'''


def after_all(context):
    context.driver.close()
    context.driver2.quit()