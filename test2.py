# _3FRCZ copyable-text selectable-text
import time 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def message(to,message=''):
    options = webdriver.ChromeOptions();
    options.add_argument('--user-data-dir=./User_Data')
    d = webdriver.Chrome(chrome_options=options)
    # d = webdriver.Chrome()      # directory to chromedriver
    d.get('https://web.whatsapp.com/')                  # URL to open whatsapp web
    wait = WebDriverWait(driver = d, timeout = 900)         # inscrease or decrease the timeout according to your net connection
    message += '\nthis is a system generated message'           # additional text to with your message to identify that it is send via software
    name_argument = f'//span[contains(@title,\'{to}\')]'        # HTML parse code to identify your reciever
    title = wait.until(EC.presence_of_element_located((By.XPATH,name_argument)))
    title.click()                           # to open the receiver messages page in the browser
    #
    # wait = WebDriverWait(driver = d, timeout = 90)
    # time.sleep(10)
    # msg_box = driver.find_element_by_class_name('_3uMse')
    # msg_box.send_keys(msg)
    
    # many a times class name or other HTML properties changes so keep a track of current class name for input box by using inspect elements
    input_path = '//div[@class="_3uMse"][@dir="auto"][@data-tab="1"]'
    print("trying to lookup")
    box = wait.until(EC.presence_of_element_located((By.XPATH,input_path)))
    box.send_keys(message + Keys.ENTER) 

message("hassan", "hello")