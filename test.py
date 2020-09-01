from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

import time

options = Options()
options.add_argument('--user-data-dir=./User_Data')
driver = webdriver.Chrome(options=options)
driver.get('https://web.whatsapp.com/')

def send_message(name, msg):
	flag = True

	try:
		user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
		user.click()

		print("Writing msg")
		wait = WebDriverWait(driver = driver, timeout = 90)
		time.sleep(5)
		msg_box = driver.find_element_by_class_name('_3uMse')
		msg_box.send_keys(msg)

		print("Pressing send button")
		time.sleep(5)
		wait = WebDriverWait(driver = driver, timeout = 90)
		button = driver.find_element_by_class_name('_1U1xa')
		button.click()

	except:
		flag = False
		return False
		
	return flag

#####
name_list = ['hassan', 'Group1']
msg = "hello1"

swait = WebDriverWait(driver = driver, timeout = 900)
time.sleep(30)

for name in name_list:
	print(name)
	resp = send_message(name, msg)
	if(resp == False):
		print("Not done->", name,". Will try again")
		name = name_list.append(name)
	else:
		print("Done->", name)

time.sleep(120)
driver.close()