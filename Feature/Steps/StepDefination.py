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
    context.driver.get('https://wowdare.xyz')
    time.sleep(0)
    context.driver.maximize_window()

@when(u'User Enter Username With Invalid Data')
def step_impl(context):
    context.driver.find_element_by_name('name').send_keys('Test@mail')

@when(u'Click On start Button')
def step_impl(context):
    context.driver.find_element_by_xpath("//a[text()='Start']").click()
    time.sleep(3)
    context.driver.find_element_by_name('name').clear()

@when(u'User Enter Username With valid Data')
def step_impl(context):
    context.driver.find_element_by_name('name').send_keys('Deepak123#')

@when(u'User Click on Start Button')
def step_impl(context):
    context.driver.find_element_by_xpath("//a[text()='Start']").click()


@then(u'User Should be Navigate to Question Page  Successfully')
def step_impl(context):
    print(context.driver.current_url)
    assert context.driver.current_url == "https://wowdare.xyz/en/question?utm_site_source=start&utm_site_medium=createButton&utm_site_campaign=user" ,\
        print(context.driver.current_url)
    time.sleep(2)



@when(u'Click On Q1')
def step_impl(context):
    #context.driver.execute_script("window.scrollTo(0, 800)")
    context.driver.find_element_by_xpath("//div[@data-file-id='197']").click()


@when(u'Validate onesignal pop-up functionality With click on Later Button')
def step_impl(context):
        wait = WebDriverWait(context.driver, 30)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Later"]')))
        element.click()
        time.sleep(1)




@when(u'Click On Q2')
def step_impl(context):
    context.driver.implicitly_wait(10)
    context.driver.find_element_by_xpath("//div[@data-file-id='160']").click()

@when(u'Click On Q3')
def step_impl(context):
    context.driver.find_element_by_xpath("//div[@value='Green']").click()


@when(u'Click On Q4')
def step_impl(context):
    context.driver.find_element_by_xpath("//div[@data-file-id='46']").click()



@when(u'Click On Q5')
def step_impl(context):
    context.driver.find_element_by_xpath("//div[@value='Beautiful Life Partner']").click()


@when(u'Click On Q6')
def step_impl(context):
    context.driver.find_element_by_xpath("//div[@data-file-id='164']").click()


@when(u'Click On Q7')
def step_impl(context):
    context.driver.find_element_by_xpath("//div[@value='Action']").click()

@when(u'Click On Q8')
def step_impl(context):
    context.driver.find_element_by_xpath("//div[@data-file-id='194']").click()


@when(u'Click On Q9')
def step_impl(context):
    context.driver.find_element_by_xpath("//div[@data-file-id='144']").click()


@when(u'Click On Q10')
def step_impl(context):
    context.driver.find_element_by_xpath("//div[@value='A Dinner with family']").click()

@when(u'Click On Q11')
def step_impl(context):
    context.driver.find_element_by_xpath("//div[@data-file-id='188']").click()

@when(u'Click On Q12')
def step_impl(context):
    context.driver.find_element_by_xpath("//div[@value='The Creative One']").click()


@when(u'Click On Q13')
def step_impl(context):
    context.driver.find_element_by_xpath("//div[@data-file-id='138']").click()


@when(u'Click On Q14')
def step_impl(context):
    context.driver.find_element_by_xpath("//div[@value='Two']").click()


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
    context.driver.find_element(By.CSS_SELECTOR, 'div[data-file-id="177"]').click()
    time.sleep(2)


@then(u'User Should be Navigate to Share Page  Successfully')
def step_impl(context):
    assert context.driver.current_url=="https://wowdare.xyz/en/share?utm_site_source=question&utm_site_medium=saveButton&utm_site_campaign=user"#"Wrong Share Page url"
    print(context.driver.current_url)
@when(u'Click On Copy link_Button')
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0, 700)")
    context.driver.find_element_by_css_selector('button[title="Copy Link"]').click()
    context.driver.find_element_by_css_selector('button[title="Copy Link"]').click()
    time.sleep(2)

@given(u'User Friend open Browser, Enter Url, Navigate To Log_in Page')
def step_impl(context):
    #context.driver2 = webdriver.Firefox()
    context.driver2.maximize_window()
    context.driver2.get("https://www.google.com/")
    time.sleep(1)
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
    context.driver2.find_element_by_name('name').send_keys('Test@mail')
    time.sleep(1)


@when(u'User Friend Click On start Button')
def step_impl(context):

    Confrom_button=context.driver2.find_element_by_xpath("//a[text()='Confirm']")
    context.driver2.execute_script('arguments[0].click()',Confrom_button)

    time.sleep(0)

@when(u'User Friend Validate onesignal pop-up functionality With click on Later Button')
def step_impl(context):
        wait = WebDriverWait(context.driver2, 30)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Later"]')))
        element.click()
        time.sleep(1)


@when(u'User Friend Enter Username With Valid Data')
def step_impl(context):
    context.driver2.find_element_by_name('name').clear()

    context.driver2.find_element_by_name('name').send_keys('Deepak123#')

@when(u'User Friend Click on Start Buttons')
def step_impl(context):
    Confrom_button = context.driver2.find_element_by_xpath("//a[text()='Confirm']")
    context.driver2.execute_script('arguments[0].click()', Confrom_button)
    time.sleep(2)


@then(u'User Friend Should be Navigate to Answer Page  Successfully')
def step_impl(context):
    assert context.driver2.current_url=="https://wowdare.xyz/en/answer?utm_site_source=accept&utm_site_medium=startButton&utm_site_campaign=userFriend","invalid Answer Page url"

@when(u'User Friend Click On Q1')
def step_impl(context):
    context.driver2.implicitly_wait(20)
    context.driver2.execute_script("window.scrollTo(0, 600)")
    context.driver2.find_element_by_xpath("//div[@data-file-id='197']").click()

@when(u'User Friend Click On Q2')
def step_impl(context):
    context.driver2.implicitly_wait(10)
    context.driver2.find_element_by_xpath("//div[@data-file-id='159']").click()


@when(u'User Friend Click On Q3')
def step_impl(context):
    context.driver2.find_element_by_xpath("//div[@value='Blue']").click()


@when(u'User Friend Click On Q4')
def step_impl(context):
    
    context.driver2.find_element_by_xpath("//div[@data-file-id='46']").click()

@when(u'User Friend Click On Q5')
def step_impl(context):
    context.driver2.find_element_by_xpath("//div[@value='A Billion Dollars']").click()

@when(u'User Friend Click On Q6')
def step_impl(context):
    context.driver2.find_element_by_xpath("//div[@data-file-id='164']").click()
    
@when(u'User Friend Click On Q7')
def step_impl(context):
    context.driver2.find_element_by_xpath("//div[@value='Action']").click()
        
@when(u'User Friend Click On Q8')
def step_impl(context):
    context.driver2.find_element_by_xpath("//div[@data-file-id='194']").click()

@when(u'User Friend Click On Q9')
def step_impl(context):
    context.driver2.find_element_by_xpath("//div[@data-file-id='144']").click()
@when(u'User Friend Click On Q10')
def step_impl(context):
    context.driver2.find_element_by_xpath("//div[@value='A Dinner with family']").click()

@when(u'User Friend Click On Q11')
def step_impl(context):
    context.driver2.find_element_by_xpath("//div[@data-file-id='190']").click()


@when(u'User Friend Click On Q12')
def step_impl(context):
    context.driver2.find_element_by_xpath("//div[@value='The Creative One']").click()
   

@when(u'User Friend Click On Q13')
def step_impl(context):
    context.driver2.find_element_by_xpath("//div[@data-file-id='136']").click()
        
@when(u'User Friend Click On Q14')
def step_impl(context):
    context.driver2.find_element_by_xpath("//div[@value='One']").click()
    
@when(u'User Friend Click On Q15')
def step_impl(context):
    context.driver2.find_element(By.CSS_SELECTOR, 'div[data-file-id="177"]').click()
    time.sleep(1)

@then(u'User Friend Should be Navigate to Complete Page  Successfully')
def step_impl(context):
    assert context.driver2.current_url=="https://wowdare.xyz/en/completed?utm_site_source=answer&utm_site_medium=saveButton&utm_site_campaign=userFriend","invalid Complete Page url"


@when(u'User Friend Click On Create Your Quiz Button')
def step_impl(context):
    Creat_button = context.driver2.find_element_by_xpath("//a[text()='Create your quiz']")
    context.driver2.execute_script('arguments[0].click()', Creat_button)

@then(u'User Friend Become User And Navigate To Home Page')
def step_impl(context):
    assert context.driver2.current_url=="https://wowdare.xyz/en?utm_site_source=completed&utm_site_medium=createButtonEnglish&utm_site_campaign=userFriend"#"invalid Home Page url"
    context.driver2.quit()
@given(u'Validate the Scoreboard  Button Functionality')
def step_impl(context):
    Scoreboard = context.driver.find_element(By.XPATH, "//a[@class='btn primary-btn v-ans w-100']")
    context.driver.execute_script('arguments[0].click()', Scoreboard)
    time.sleep(1)

@when(u'User Click On View_Button')
def step_impl(context):
    View_Button = context.driver.find_element(By.XPATH, "//div[@class='top-3']/span[2]")
    context.driver.execute_script('arguments[0].click()', View_Button)
    time.sleep(2)
@then(u'User Should Be Navigate To View Page')
def step_impl(context):
    assert context.driver.current_url=="https://wowdare.xyz/en/view-answer?utm_site_source=result&utm_site_medium=viewAnswerEnglish&utm_site_campaign=user","invalid View Page url"

@when(u'User Click On Back_Button And Should Be Navigate To Share Page')
def step_impl(context):
    back = context.driver.find_element_by_xpath("//a[text()='Back']")
    context.driver.execute_script('arguments[0].click()', back)
    time.sleep(0)

@when(u'Again User Click On View_Button And Navigate To View Page')
def step_impl(context):
    View_Button = context.driver.find_element(By.XPATH, "//div[@class='top-3']/span[2]")
    context.driver.execute_script('arguments[0].click()', View_Button)
    time.sleep(2)

@when(u'Click On View_page Delete Button')
def step_impl(context):
    view_Delete = context.driver.find_element_by_xpath("//a[text()='Delete']")
    context.driver.execute_script('arguments[0].click()', view_Delete)
    time.sleep(2)
@then(u'A Delete Pop_Up Should Be Open With Yes Or No Button Click On No Button')
def step_impl(context):
    view_No = context.driver.find_element_by_xpath("//button[text()='No']")
    context.driver.execute_script('arguments[0].click()', view_No)
    time.sleep(2)
@then(u'Click On Yes Button')
def step_impl(context):
    view_Yes = context.driver.find_element_by_xpath("//button[text()='Yes']")
    context.driver.execute_script('arguments[0].click()', view_Yes)
    time.sleep(2)
@then(u'Particular User Friend Entire Data Should Be Deleted And User Should Be Navigate To Share_page')
def step_impl(context):
    assert context.driver2.current_url=="https://wowdare.xyz/en/share","Invalid Share Page"

@when(u'Click On share_page Delete Button')
def step_impl(context):
    Delete = context.driver.find_element_by_xpath("//a[text()='Delete']")
    context.driver.execute_script('arguments[0].click()', Delete)
    time.sleep(2)
@then(u'A Delete Pop_Up Should Be Open And  Click On No Button')
def step_impl(context):
    No = context.driver.find_element_by_xpath("//button[text()='No']")
    context.driver.execute_script('arguments[0].click()', No)
    time.sleep(2)

@then(u'Click On Yes Button Share Page')
def step_impl(context):
    Yes = context.driver.find_element_by_xpath("//button[text()='Yes']")
    context.driver.execute_script('arguments[0].click()', Yes)

@then(u'Entire Quiz Should Be Deleted And User Navigate To The Home Page.')
def step_impl(context):
    assert context.driver.current_url=="https://wowdare.xyz/en?utm_site_source=share&utm_site_medium=deleteButtonEnglish&utm_site_campaign=user","Invalid Home Page"
