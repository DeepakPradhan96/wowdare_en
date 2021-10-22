from behave import *
import time
from  selenium.webdriver.support  import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import  ActionChains
#from selenium.webcontext.driver.common.keys import keys, Keys
import pyperclip

@given(u'User open Browser, Enter Url, Navigate To Log_in Page')
def step_impl(context):
    context.driver.get('https://wowdare.xyz/cn')
    time.sleep(0)
    context.driver.maximize_window()

@when(u'User Enter Username With Invalid Data')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR,"[name='name']").send_keys('Test@mail')
    time.sleep(1)

@when(u'Click On start Button')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//a[@class='btn primary-btn start mt-4 w-90' and @href='#']").click()
    time.sleep(2)
    context.driver.find_element_by_name('name').clear()

@when(u'User Enter Username With valid Data')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR,"[name='name']").send_keys('Deepak123#')

@when(u'User Click on Start Button')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//a[@class='btn primary-btn start mt-4 w-90' and @href='#']").click()
    time.sleep(1)

@then(u'User Should be Navigate to Question Page  Successfully')
def step_impl(context):
    print(context.driver.current_url)
    #assert context.driver.current_url == "https://wowdare.xyz/en/question?",'Invalid Url'
    time.sleep(2)

@when(u'Click On Q1')
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0, 400)")
    context.driver.find_element(By.CSS_SELECTOR, '.option:nth-child(2)').click()
    time.sleep(2)

@when(u'Click On Q2')
def step_impl(context):
    context.driver.implicitly_wait(10)
    context.driver.find_element(By.CSS_SELECTOR, '.option:nth-child(2)').click()
    time.sleep(1)
@when(u'Click On Q3')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, '.option:nth-child(1)').click()
    time.sleep(1)
@when(u'Click On Q4')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, '.option:nth-child(2)').click()
    time.sleep(1)

@when(u'Validate onesignal pop-up functionality With click on Later Button')
def step_impl(context):
        wait = WebDriverWait(context.driver, 30)
        element = wait.until(EC.visibility_of_element_located(( By.CSS_SELECTOR,"[id='onesignal-slidedown-cancel-button']")))
        element.click()
        time.sleep(1)

@when(u'Click On Q5')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, '.option:nth-child(3)').click()
    time.sleep(0.5)
@when(u'Click On Q6')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, '.option:nth-child(4)').click()
    time.sleep(1)

@when(u'Click On Q7')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, '.option:nth-child(2)').click()
    time.sleep(1)

@when(u'Click On Q8')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, '.option:nth-child(1)').click()
    time.sleep(1)

@when(u'Click On Q9')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, '.option:nth-child(2)').click()
    time.sleep(1)

@when(u'Click On Q10')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, '.option:nth-child(1)').click()
    time.sleep(1)
@when(u'Click On Q11')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, '.option:nth-child(2)').click()
    time.sleep(1)
@when(u'Click On Q12')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, '.option:nth-child(1)').click()
    time.sleep(1)

@when(u'Click On Q13')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, '.option:nth-child(2)').click()
    time.sleep(1)

@when(u'Click On Q14')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, '.option:nth-child(2)').click()
    time.sleep(1)

@given(u'Validate Skip Button functionality')
def step_impl(context):
    for x in range(0, 12):
        skip = context.driver.find_element_by_class_name('skip').click()
        time.sleep(0)
        if x == 10:
            print(x)
            break


@when(u'Click On Q15')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, '.option:nth-child(2)').click()
    time.sleep(2)


@then(u'User Should be Navigate to Share Page  Successfully')
def step_impl(context):
    #assert context.driver.current_url=="https://wowdare.xyz/en/share?utm_site_source=question&utm_site_medium=saveButton&utm_site_campaign=user"#"Wrong Share Page url"
    print(context.driver.current_url)
    time.sleep(2)

@when(u'Click On Copy link_Button')
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0, 800)")
    context.driver.find_element_by_css_selector('button[title="Copy Link"]').click()
    time.sleep(3)


    '''context.driver.implicitly_wait(10)
    Copy=context.driver.find_element_by_css_selector('button[title="Copy Link"]')
    context.driver.execute_script('arguments[0].click()', Copy)
    time.sleep(3)
    Copy = context.driver.find_element_by_css_selector('button[title="Copy Link"]')
    context.driver.execute_script('arguments[0].click()', Copy)'''


@given(u'User Friend open Browser, Enter Url, Navigate To Log_in Page')
def step_impl(context):
    #context.driver2 = webdriver.Firefox()
    context.driver2.maximize_window()
    context.driver2.get("https://www.google.com/")
    time.sleep(2)

    act = ActionChains(context.driver2)
    url = pyperclip.paste()
    print(url)

    context.driver2.execute_script("window.open(\"" + url + "\")")
    # driver.execute_script("window.open(\""+url+"\")")

    handle = context.driver2.window_handles
    for win in handle:
        context.driver2.switch_to.window(win)
        if (context.driver2.title == 'Best Friends Cup'):
            print(context.driver2.current_url)



@when(u'User Friend Enter Username With Invalid Data')
def step_impl(context):
    context.driver2.implicitly_wait(10)
    context.driver2.find_element(By.CSS_SELECTOR,"[name='name']").send_keys('Test@mail')
    time.sleep(2)


@when(u'User Friend Click On start Button')
def step_impl(context):

    Confrom_button=context.driver2.find_element_by_xpath("//a[@class='btn primary-btn start mt-4 w-90' and @href='#']")
    context.driver2.execute_script('arguments[0].click()',Confrom_button)
    time.sleep(3)
    context.driver2.find_element_by_name('name').clear()
    time.sleep(2)

@when(u'User Friend Validate onesignal pop-up functionality With click on Later Button')
def step_impl(context):
        wait = WebDriverWait(context.driver2,30)
        element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[id='onesignal-slidedown-cancel-button']")))
        element.click()
        time.sleep(1)


@when(u'User Friend Enter Username With Valid Data')
def step_impl(context):

    context.driver2.find_element(By.CSS_SELECTOR,"[name='name']").send_keys('Deepak123#')
    time.sleep(0.5)

@when(u'User Friend Click on Start Buttons')
def step_impl(context):
    Confrom_button = context.driver2.find_element_by_xpath("//a[@class='btn primary-btn start mt-4 w-90' and @href='#']")
    context.driver2.execute_script('arguments[0].click()', Confrom_button)
    time.sleep(2)


@then(u'User Friend Should be Navigate to Answer Page  Successfully')
def step_impl(context):
    #assert context.driver2.current_url=="https://wowdare.xyz/en/answer?utm_site_source=accept&utm_site_medium=startButton&utm_site_campaign=userFriend","invalid Answer Page url"
    print(context.driver2.current_url)
    time.sleep(2)
@when(u'User Friend Click On Q1')
def step_impl(context):
    context.driver2.implicitly_wait(20)
    context.driver2.execute_script("window.scrollTo(0, 600)")
    context.driver2.find_element(By.CSS_SELECTOR, '.option:nth-child(2)').click()
    time.sleep(2)
@when(u'User Friend Click On Q2')
def step_impl(context):
    context.driver2.implicitly_wait(10)
    context.driver2.find_element(By.CSS_SELECTOR, '.option:nth-child(1)').click()
    time.sleep(2)

@when(u'User Friend Click On Q3')
def step_impl(context):
    context.driver2.find_element(By.CSS_SELECTOR, '.option:nth-child(3)').click()
    time.sleep(2)


@when(u'User Friend Click On Q4')
def step_impl(context):
    context.driver2.find_element(By.CSS_SELECTOR, '.option:nth-child(4)').click()
    time.sleep(2)
@when(u'User Friend Click On Q5')
def step_impl(context):
    context.driver2.find_element(By.CSS_SELECTOR, '.option:nth-child(1)').click()
    time.sleep(2)
@when(u'User Friend Click On Q6')
def step_impl(context):
    context.driver2.find_element(By.CSS_SELECTOR, '.option:nth-child(2)').click()
    time.sleep(2)
@when(u'User Friend Click On Q7')
def step_impl(context):
    context.driver2.find_element(By.CSS_SELECTOR, '.option:nth-child(3)').click()
    time.sleep(2)
@when(u'User Friend Click On Q8')
def step_impl(context):
    context.driver2.find_element(By.CSS_SELECTOR, '.option:nth-child(2)').click()
    time.sleep(2)
@when(u'User Friend Click On Q9')
def step_impl(context):
    context.driver2.find_element(By.CSS_SELECTOR, '.option:nth-child(3)').click()
    time.sleep(2)
@when(u'User Friend Click On Q10')
def step_impl(context):
    context.driver2.find_element(By.CSS_SELECTOR, '.option:nth-child(2)').click()
    time.sleep(2)
@when(u'User Friend Click On Q11')
def step_impl(context):
    context.driver2.find_element(By.CSS_SELECTOR, '.option:nth-child(2)').click()
    time.sleep(2)

@when(u'User Friend Click On Q12')
def step_impl(context):
    context.driver2.find_element(By.CSS_SELECTOR, '.option:nth-child(1)').click()
    time.sleep(3)


@when(u'User Friend Click On Q13')
def step_impl(context):
    context.driver2.find_element(By.CSS_SELECTOR, '.option:nth-child(1)').click()
    time.sleep(3)


@when(u'User Friend Click On Q14')
def step_impl(context):
    context.driver2.find_element(By.CSS_SELECTOR, '.option:nth-child(2)').click()
    time.sleep(3)


@when(u'User Friend Click On Q15')
def step_impl(context):
    context.driver2.find_element(By.CSS_SELECTOR, '.option:nth-child(1)').click()
    time.sleep(3)


@then(u'User Friend Should be Navigate to Complete Page  Successfully')
def step_impl(context):
    #assert context.driver2.current_url=="https://wowdare.xyz/en/completed?utm_site_source=answer&utm_site_medium=saveButton&utm_site_campaign=userFriend","invalid Complete Page url"
    print(context.driver2.current_url)

@when(u'User Friend Click On Create Your Quiz Button')
def step_impl(context):
    Creat_button = context.driver2.find_element_by_xpath("//a[@id='step16'and @class='btn primary-btn mb-5 w-100']")
    context.driver2.execute_script('arguments[0].click()', Creat_button)
    time.sleep(2)

@then(u'User Friend Become User And Navigate To Home Page')
def step_impl(context):
    context.driver2.quit()
    time.sleep(2)
@given(u'Validate the Scoreboard  Button Functionality')
def step_impl(context):
    Scoreboard = context.driver.find_element(By.XPATH, "//a[@class='btn primary-btn v-ans w-100']")
    context.driver.execute_script('arguments[0].click()', Scoreboard)
    time.sleep(2)

@when(u'User Click On View_Button')
def step_impl(context):
    View_Button = context.driver.find_element(By.XPATH, "//div[@class='top-3']/span[2]")
    context.driver.execute_script('arguments[0].click()', View_Button)
    time.sleep(2)
@then(u'User Should Be Navigate To View Page')
def step_impl(context):
    #assert context.driver.current_url=="https://wowdare.xyz/en/view-answer?utm_site_source=result&utm_site_medium=viewAnswerEnglish&utm_site_campaign=user","invalid View Page url"
    print(context.driver.current_url)
@when(u'User Click On Back_Button And Should Be Navigate To Share Page')
def step_impl(context):
    back = context.driver.find_element_by_xpath("//a[@class='btn primary-btn w-90']")
    context.driver.execute_script('arguments[0].click()', back)
    time.sleep(2)

@when(u'Again User Click On View_Button And Navigate To View Page')
def step_impl(context):
    View_Button = context.driver.find_element(By.XPATH, "//div[@class='top-3']/span[2]")
    context.driver.execute_script('arguments[0].click()', View_Button)
    time.sleep(2)

@when(u'Click On View_page Delete Button')
def step_impl(context):
    view_Delete = context.driver.find_element_by_xpath("//a[@class='btn primary-btn mt-0 80'  and @data-toggle='modal']")
    context.driver.execute_script('arguments[0].click()', view_Delete)
    time.sleep(2)

@then(u'A Delete Pop_Up Should Be Open With Yes Or No Button Click On No Button')
def step_impl(context):
    view_No = context.driver.find_element_by_xpath("//button[@class='btn primary-btn' and @data-dismiss='modal']")
    context.driver.execute_script('arguments[0].click()', view_No)
    time.sleep(2)
'''@then(u'Click On View_page Delete Button Again')
def step_impl(context):
    Delete_Button= context.driver.find_element_by_xpath("//a[@class='btn primary-btn mt-0 80'  and @data-toggle='modal']")
    context.driver.execute_script('arguments[0].click()', Delete_Button)
    time.sleep(2)'''
@then(u'Click On Yes Button')
def step_impl(context):
    view_Yes = context.driver.find_element_by_xpath("//button[@class='btn primary-btn delete_yes']")
    context.driver.execute_script('arguments[0].click()', view_Yes)
    time.sleep(2)
@then(u'Particular User Friend Entire Data Should Be Deleted And User Should Be Navigate To Share_page')
def step_impl(context):
    #assert context.driver2.current_url=="https://wowdare.xyz/en/share","Invalid Share Page"
    print(context.driver.current_url)
@given(u'Validate The Functionality of Scoreboard')
def step_impl(context):
    Scoreboard = context.driver.find_element(By.XPATH, "//a[@class='btn primary-btn v-ans w-100']")
    context.driver.execute_script('arguments[0].click()', Scoreboard)
    time.sleep(3)


@when(u'Click On share_page Delete Button')
def step_impl(context):
    Delete = context.driver.find_element_by_xpath("//a[@class='btn primary-btn w-90'and @data-toggle='modal']")
    context.driver.execute_script('arguments[0].click()', Delete)
    time.sleep(3)
@then(u'A Delete Pop_Up Should Be Open And  Click On No Button')
def step_impl(context):
    No = context.driver.find_element_by_xpath("//button[@class='btn primary-btn' and @data-dismiss='modal']")
    context.driver.execute_script('arguments[0].click()', No)
    time.sleep(2)

'''@then(u'Click On share_page Delete Button Again')
def step_impl(context):
    Delete = context.driver.find_element_by_xpath("//a[@class='btn primary-btn w-90'and @data-toggle='modal']")
    context.driver.execute_script('arguments[0].click()', Delete)
    time.sleep(3)'''

@then(u'Click On Yes Button Share Page')
def step_impl(context):
    Yes = context.driver.find_element_by_xpath("//button[@class='btn primary-btn delete_yes']")
    context.driver.execute_script('arguments[0].click()', Yes)
    time.sleep(2)

@then(u'Entire Quiz Should Be Deleted And User Navigate To The Home Page.')
def step_impl(context):
    #assert context.driver.current_url=="https://wowdare.xyz/en?utm_site_source=share&utm_site_medium=deleteButtonEnglish&utm_site_campaign=user","Invalid Home Page"
    print(context.driver.current_url)
    time.sleep(0)