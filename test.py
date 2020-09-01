from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

import time

# options = webdriver.ChromeOptions();

options = Options()
options.add_argument('--user-data-dir=./User_Data')
driver = webdriver.Chrome(options=options)
driver.get('https://web.whatsapp.com/')

# name = input('Enter the name of user or group : ')
name = 'hassan'
name_list = ['hassan', 'Group1']
# msg = input('Enter your message : ')
msg = "hello1"
# count = int(input('Enter the count : '))
count = 2
wait = WebDriverWait(driver = driver, timeout = 900)
time.sleep(30)

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

# msg_box = driver.find_element_by_class_name('_2S1VP')
# _2FbwG

# msg += '\n this is a system generated message'

for i in range(count):
	print("count->", i+1)
	wait = WebDriverWait(driver = driver, timeout = 90)
	time.sleep(10)
	msg_box = driver.find_element_by_class_name('_3uMse')
	msg_box.send_keys(msg)

	time.sleep(10)
	wait = WebDriverWait(driver = driver, timeout = 90)
	button = driver.find_element_by_class_name('_1U1xa')
	button.click()

wait = WebDriverWait(driver = driver, timeout = 600)

time.sleep(120)
driver.close()