from selenium import webdriver
import time
from  selenium.webdriver.support  import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import  ActionChains
#from selenium.webdriver.common.keys import keys, Keys
import pyperclip

driver=webdriver.Chrome(executable_path='C:\Driver\chromedriver_win32\chromedriver.exe')
driver.get('https://wowdare.xyz/cn')
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR,"[name='name']").send_keys("test")
time.sleep(0.2)
driver.find_element(By.XPATH,"//a[@class='btn primary-btn start mt-4 w-90' and @href='#']").click()
time.sleep(1)

driver.execute_script("window.scrollTo(0, 600)")
driver.find_element(By.CSS_SELECTOR, '.option:nth-child(2)').click()
time.sleep(1)

wait = WebDriverWait(driver,20)
element=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"[id='onesignal-slidedown-cancel-button']")))
element.click()
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, '.option:nth-child(2)').click()
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, '.option:nth-child(3)').click()
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, '.option:nth-child(4)').click()
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, '.option:nth-child(1)').click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '.option:nth-child(3)').click()
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, '.option:nth-child(2)').click()
time.sleep(1)


driver.find_element(By.CSS_SELECTOR, '.option:nth-child(3)').click()
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, '.option:nth-child(1)').click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '.option:nth-child(2)').click()
time.sleep(1)

time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '.option:nth-child(4)').click()

time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '.option:nth-child(1)').click()

time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '.option:nth-child(2)').click()
time.sleep(0.3)
driver.find_element(By.CSS_SELECTOR, '.option:nth-child(4)').click()
time.sleep(0.5)
for x in range(0,12):
    skip = driver.find_element_by_class_name('skip').click()
    time.sleep(0)
    if x==10:
        print(x)
        break

driver.find_element(By.CSS_SELECTOR, '.option:nth-child(3)').click()

driver.execute_script("window.scrollTo(0, 700)")
driver.find_element_by_css_selector('button[title="Copy Link"]').click()
time.sleep(3)


chrome_option=webdriver.ChromeOptions()
chrome_option.add_argument("--incognito")
y=webdriver.Chrome(chrome_options=chrome_option)
y.maximize_window()
y.get("https://www.google.com/")
time.sleep(3)

act = ActionChains(y)
url = pyperclip.paste()
print(url)

y.execute_script("window.open(\"" + url + "\")")
# driver.execute_script("window.open(\""+url+"\")")

handle = y.window_handles
for win in handle:
        y.switch_to.window(win)
        if (y.title == 'Best Friends Cup'):
            print(y.current_url)


'''act=ActionChains(y)
y.find_element_by_xpath('//input[@title="Search"]').send_keys(act.key_down(Keys.CONTROL).send_keys('v').perform())'''

wait = WebDriverWait(driver, 20)
element=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#onesignal-slidedown-cancel-button")))
element.click()
time.sleep(2)

y.implicitly_wait(10)

driver.find_elements_by_name('name')[0].send_keys('Test@gmasil,')
time.sleep(0.2)
y.find_element_by_xpath("//a[normalize-space()='Confirm']").click()
time.sleep(0)
y.find_element_by_name('name').clear()


y.find_element_by_name('name').send_keys('Deepak123#')
y.execute_script("window.scrollTo(0, 700)")
y.find_element_by_xpath("//a[text()='Confirm']").click()
time.sleep(1)

y.find_element_by_xpath("//div[@data-file-id='197']").click()
y.implicitly_wait(10)
y.find_element_by_xpath("//div[@data-file-id='160']").click()
y.find_element_by_xpath("//div[@value='Green']").click()
y.find_element_by_xpath("//div[@data-file-id='46']").click()
y.find_element_by_xpath("//div[@value='Beautiful Life Partner']").click()
y.find_element_by_xpath("//div[@data-file-id='164']").click()
y.find_element_by_xpath("//div[@value='Action']").click()
y.find_element_by_xpath("//div[@data-file-id='194']").click()
y.find_element_by_xpath("//div[@data-file-id='144']").click()
y.find_element_by_xpath("//div[@value='A Dinner with family']").click()
y.find_element_by_xpath("//div[@data-file-id='188']").click()
y.find_element_by_xpath("//div[@value='The Creative One']").click()
y.find_element_by_xpath("//div[@data-file-id='138']").click()
y.find_element_by_xpath("//div[@value='Two']").click()
y.find_element(By.CSS_SELECTOR, 'div[data-file-id="177"]').click()
time.sleep(2)


Creat_button=y.find_element_by_xpath("//a[text()='Create your quiz']")
y.execute_script('arguments[0].click()',Creat_button)

time.sleep(3)
y.quit()


Scoreboard =driver.find_element(By.XPATH,"//a[@class='btn primary-btn v-ans w-100']")
driver.execute_script('arguments[0].click()',Scoreboard )
time.sleep(4)

View_Button=driver.find_element(By.XPATH,"//div[@class='top-3']/span[2]")
driver.execute_script('arguments[0].click()',View_Button)
time.sleep(2)


back=driver.find_element_by_xpath("//a[text()='Back']")
driver.execute_script('arguments[0].click()',back)
time.sleep(2)

View_Button=driver.find_element(By.XPATH,"//div[@class='top-3']/span[2]")
driver.execute_script('arguments[0].click()',View_Button)
time.sleep(2)

view_Delete=driver.find_element_by_xpath("//a[text()='Delete']")
driver.execute_script('arguments[0].click()',view_Delete)
time.sleep(2)



view_No=driver.find_element_by_xpath("//button[text()='No']")
driver.execute_script('arguments[0].click()',view_No)
time.sleep(2)

view_Yes=driver.find_element_by_xpath("//button[text()='Yes']")
driver.execute_script('arguments[0].click()',view_Yes)
time.sleep(2)

Delete=driver.find_element_by_xpath("//a[text()='Delete']")
driver.execute_script('arguments[0].click()',Delete)
time.sleep(2)

No=driver.find_element_by_xpath("//button[text()='No']")
driver.execute_script('arguments[0].click()',No)
time.sleep(2)

Yes=driver.find_element_by_xpath("//button[text()='Yes']")
driver.execute_script('arguments[0].click()',Yes)


driver.execute_script("window.scrollTo(0, 700)")
driver.find_element_by_xpath("//span[@class='score']").click()
time.sleep(2)
driver.execute_script("window.scrollTo(0, 700)")
driver.find_element_by_xpath("//a[text()='Back']").click()
driver.execute_script("window.scrollTo(0, 700)")
driver.find_element_by_xpath("//span[@class='score']").click()
time.sleep(2)
driver.find_element_by_xpath("//a[text()='Delete']").click()
driver.find_element_by_xpath("//button[text()='No']").click()
driver.find_element_by_xpath("//a[text()='Delete']").click()
driver.find_element_by_xpath("//button[text()='Yes']")
driver.find_element_by_xpath("//a[text()='Delete']").click()
driver.find_element_by_xpath("//button[text()='No']").click()
driver.find_element_by_xpath("//button[text()='Yes']")